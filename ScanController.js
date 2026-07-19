/**
 * ============================================================
 * DriveMaintenance v1.4
 * Scan Controller
 * ============================================================
 *
 * Executes one Drive scan batch.
 *
 * Responsibilities
 * ----------------
 * • Detect new vs resumed scan
 * • Reset Drive Index only for a new scan
 * • Invoke DriveScanner
 * • Append batch rows
 * • Never manage continuation tokens
 * ============================================================
 */

class ScanController {

  constructor() {

    this.logger = new AuditLogger();
    this.stateManager = new StateManager();

  }

  run() {

    this.logger.log(
      "CONTROLLER",
      "STARTED",
      "Scan execution started"
    );

    //----------------------------------------------------------
    // Detect whether this is a NEW scan or a RESUME
    //----------------------------------------------------------

    const existingState =
      this.stateManager.get("SCAN_STATE");

    const writer =
      new ReportWriter();

    if (!existingState) {

      writer.clearSheet(
        CONFIG.INDEX_SHEET_NAME
      );

      this.logger.log(
        "CONTROLLER",
        "NEW_SCAN",
        "Drive Index cleared for fresh scan"
      );

    }

    //----------------------------------------------------------
    // Scan one batch
    //----------------------------------------------------------

    const index =
      new DriveIndex();

    const scanner =
      new DriveScanner(
        this.logger,
        index,
        this.stateManager
      );

    scanner.scanBatch();

    //----------------------------------------------------------
    // Write scanned records
    //----------------------------------------------------------

    const files =
      index.getFiles();

    if (files.length > 0) {

      const rows =
        files.map(file => [

          file.fileId,
          file.name,
          file.mimeType,
          file.size,
          file.checksum,
          file.createdDate,
          file.modifiedDate,
          file.path,
          file.insideBackup

        ]);

      writer.appendRows(

        CONFIG.INDEX_SHEET_NAME,

        [
          "File ID",
          "Name",
          "MIME Type",
          "Size",
          "Checksum",
          "Created",
          "Modified",
          "Path",
          "Inside Backup"
        ],

        rows

      );

      this.logger.log(
        "CONTROLLER",
        "ROWS_WRITTEN",
        rows.length + " rows written"
      );

    } else {

      this.logger.log(
        "CONTROLLER",
        "NO_ROWS",
        "Nothing to write"
      );

    }

    //----------------------------------------------------------
    // Scan completion logging
    //----------------------------------------------------------

    if (!this.stateManager.get("SCAN_STATE")) {

      this.logger.log(
        "CONTROLLER",
        "SCAN_COMPLETE",
        "Entire Drive indexed successfully"
      );

    }

    //----------------------------------------------------------
    // Print audit log
    //----------------------------------------------------------

    this.logger.print();

  }

}