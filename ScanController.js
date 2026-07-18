/**
 * ============================================================
 * DriveMaintenance v1.3
 * Scan Controller
 * ============================================================
 *
 * Executes one Drive scan batch.
 * Orchestrates:
 *   DriveScanner
 *   DriveIndex
 *   ReportWriter
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

    const index = new DriveIndex();

    const scanner = new DriveScanner(
      this.logger,
      index,
      this.stateManager
    );

    scanner.scanBatch();

    const files = index.getFiles();

    if (files.length > 0) {

      const rows = files.map(file => [

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

      const writer = new ReportWriter();

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

    const state =
      this.stateManager.get("SCAN_STATE");

    if (state && state.completed) {

      this.logger.log(
        "CONTROLLER",
        "SCAN_COMPLETE",
        "Entire Drive has been indexed"
      );

    }

    this.logger.print();

  }

}