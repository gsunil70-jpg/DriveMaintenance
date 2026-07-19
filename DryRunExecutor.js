/**
 * ============================================================
 * DriveMaintenance
 * Dry Run Executor
 * ============================================================
 *
 * Simulates execution of the Execution Manifest.
 *
 * No Google Drive modifications are performed.
 *
 * Responsibilities
 * ----------------
 * • Read Execution Manifest
 * • Simulate execution
 * • Produce Dry Run Execution Log
 *
 * ============================================================
 */


class DryRunExecutor {

  constructor() {

    this.manifest =
      new ExecutionManifest();

    this.ss =
      SpreadsheetApp.openById(
        CONFIG.SPREADSHEET_ID
      );

    this.logSheet =
      this.getLogSheet();

  }



  run() {

    const records =
      this.manifest.getRecords();

    if (records.length === 0) {

      Logger.log(
        "Execution Manifest is empty."
      );

      return;

    }


    const runId =
      "DRYRUN-" +
      Utilities.formatDate(

        new Date(),

        Session.getScriptTimeZone(),

        "yyyyMMdd-HHmmss"

      );


    const timestamp =
      new Date();


    const output = [];


    records.forEach(record => {

      output.push(

        this.processRecord(

          record,

          runId,

          timestamp

        )

      );

    });


    this.writeLog(output);

    this.formatLogSheet();

    Logger.log(

      "Dry run completed. " +

      output.length +

      " records processed."

    );

  }



  getLogSheet() {

    let sheet =

      this.ss.getSheetByName(

        CONFIG.DRY_RUN_LOG_SHEET ||

        "Dry Run Execution Log"

      );


    if (!sheet) {

      sheet =

        this.ss.insertSheet(

          CONFIG.DRY_RUN_LOG_SHEET ||

          "Dry Run Execution Log"

        );

    }


    return sheet;

  }

    processRecord(

    record,

    runId,

    timestamp

  ) {

    let result = "";

    let message = "";


    switch (record.operation) {


      case EXECUTION.OPERATIONS.KEEP:

        result =
          EXECUTION.EXECUTION_RESULT.NO_ACTION;

        message =
          "Canonical file retained.";

        break;



      case EXECUTION.OPERATIONS.MANUAL_REVIEW:

        result =
          EXECUTION.EXECUTION_RESULT.WAITING;

        message =
          "Awaiting manual review.";

        break;



      case EXECUTION.OPERATIONS.REDIRECT_TO_CANONICAL:


        if (

          record.reviewStatus ===

          EXECUTION.REVIEW_STATUS.APPROVED

        ) {

          result =
            EXECUTION.EXECUTION_RESULT.SIMULATED;

          message =
            "Would redirect duplicate to canonical copy.";

        }

        else {

          result =
            EXECUTION.EXECUTION_RESULT.BLOCKED;

          message =
            "Approval required before execution.";

        }

        break;



      default:

        result =
          EXECUTION.EXECUTION_RESULT.FAILED;

        message =
          "Unknown operation.";

    }



    return [

      record.reviewStatus,

      result,

      record.operation,

      record.resolutionMode,

      record.fileName,

      record.currentPath,

      record.canonicalFileName,

      record.canonicalPath,

      record.reason,

      runId,

      timestamp,

      message

    ];

  }



  writeLog(rows) {

    if (rows.length === 0) {

      return;

    }


    const headers = [

      "Review Status",

      "Result",

      "Operation",

      "Resolution Mode",

      "File Name",

      "Current Path",

      "Canonical File Name",

      "Canonical Path",

      "Reason",

      "Run ID",

      "Timestamp",

      "Message"

    ];


    if (

      this.logSheet.getLastRow() === 0

    ) {

      this.logSheet

        .getRange(

          1,

          1,

          1,

          headers.length

        )

        .setValues(

          [headers]

        );

    }


    this.logSheet

      .getRange(

        this.logSheet.getLastRow() + 1,

        1,

        rows.length,

        headers.length

      )

      .setValues(rows);

  }

    formatLogSheet() {

    const widths = [

      140, // Review Status
      140, // Result
      180, // Operation
      200, // Resolution Mode
      240, // File Name
      320, // Current Path
      240, // Canonical File Name
      320, // Canonical Path
      320, // Reason
      180, // Run ID
      180, // Timestamp
      320  // Message

    ];


    this.logSheet.setFrozenRows(1);


    this.logSheet
      .getRange(
        1,
        1,
        this.logSheet.getLastRow(),
        widths.length
      )
      .setWrap(true);


    widths.forEach(

      (width, index) => {

        this.logSheet.setColumnWidth(

          index + 1,

          width

        );

      }

    );

  }

}