/**
 * ============================================================
 * DriveMaintenance
 * Execution Manifest Repository
 * ============================================================
 *
 * Repository over the Execution Manifest sheet.
 *
 * Responsibilities
 * ----------------
 * • Read manifest records
 * • Locate columns
 * • Return records as objects
 * • Update execution metadata
 *
 * No execution logic belongs here.
 *
 * ============================================================
 */


class ExecutionManifest {

  constructor() {

    this.ss =
      SpreadsheetApp.openById(
        SPREADSHEET_ID
      );

    this.sheet =
      this.ss.getSheetByName(
        "Execution Manifest"
      );

    if (!this.sheet) {

      throw new Error(
        "Execution Manifest sheet not found."
      );

    }

    this.data =
      this.sheet
        .getDataRange()
        .getValues();

    this.headers =
      this.data.shift();

  }



  column(name) {

    const index =
      this.headers.indexOf(name);

    if (index === -1) {

      throw new Error(
        "Missing manifest column: " +
        name
      );

    }

    return index;

  }



  getRecords() {

    const c = EXECUTION.MANIFEST_COLUMNS;

    return this.data.map((row, i) => ({

      rowNumber:

        i + 2,

      reviewStatus:

        row[
          this.column(
            c.REVIEW_STATUS
          )
        ],

      operation:

        row[
          this.column(
            c.OPERATION
          )
        ],

      resolutionMode:

        row[
          this.column(
            c.RESOLUTION_MODE
          )
        ],

      fileName:

        row[
          this.column(
            c.FILE_NAME
          )
        ],

      currentPath:

        row[
          this.column(
            c.CURRENT_PATH
          )
        ],

      canonicalFileName:

        row[
          this.column(
            c.CANONICAL_FILE_NAME
          )
        ],

      canonicalPath:

        row[
          this.column(
            c.CANONICAL_PATH
          )
        ],

      reason:

        row[
          this.column(
            c.REASON
          )
        ],

      runId:

        row[
          this.column(
            c.RUN_ID
          )
        ],

      executionStatus:

        row[
          this.column(
            c.EXECUTION_STATUS
          )
        ],

      executedAt:

        row[
          this.column(
            c.EXECUTED_AT
          )
        ],

      fileId:

        row[
          this.column(
            c.FILE_ID
          )
        ],

      canonicalFileId:

        row[
          this.column(
            c.CANONICAL_FILE_ID
          )
        ],

      approvedBy:

        row[
          this.column(
            c.APPROVED_BY
          )
        ],

      approvalDate:

        row[
          this.column(
            c.APPROVAL_DATE
          )
        ],

      approvalNote:

        row[
          this.column(
            c.APPROVAL_NOTE
          )
        ]

    }));

  }


  getApprovedRecords() {

    return this
      .getRecords()
      .filter(

        record =>

          record.reviewStatus ===
          EXECUTION.REVIEW_STATUS.APPROVED

      );

  }

    findByFileId(fileId) {

    return this
      .getRecords()
      .find(

        record =>

          record.fileId === fileId

      );

  }


  updateExecution(

    rowNumber,

    runId,

    status,

    executedAt

  ) {

    const c =
      EXECUTION.MANIFEST_COLUMNS;

    this.sheet.getRange(

      rowNumber,

      this.column(
        c.RUN_ID
      ) + 1

    ).setValue(runId);

    this.sheet.getRange(

      rowNumber,

      this.column(
        c.EXECUTION_STATUS
      ) + 1

    ).setValue(status);

    this.sheet.getRange(

      rowNumber,

      this.column(
        c.EXECUTED_AT
      ) + 1

    ).setValue(executedAt);

  }

}
