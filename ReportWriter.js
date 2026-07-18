/**
 * ============================================================
 * DriveMaintenance v1.3
 * Report Writer
 * ============================================================
 *
 * Centralized spreadsheet writing service.
 *
 * Responsibilities
 * ----------------
 * • Open reporting spreadsheet
 * • Create sheets when required
 * • Append rows
 * • Replace complete tables
 *
 * Contains NO business logic.
 * ============================================================
 */

class ReportWriter {

  constructor() {

    this.spreadsheet = this.getSpreadsheet();

  }

  getSpreadsheet() {

    if (
      typeof SPREADSHEET_ID === "undefined" ||
      !SPREADSHEET_ID
    ) {

      throw new Error(
        "SPREADSHEET_ID is not configured."
      );

    }

    return SpreadsheetApp.openById(
      SPREADSHEET_ID
    );

  }

  ensureSheet(sheetName) {

    let sheet =
      this.spreadsheet.getSheetByName(
        sheetName
      );

    if (!sheet) {

      sheet =
        this.spreadsheet.insertSheet(
          sheetName
        );

    }

    return sheet;

  }

  clearSheet(sheetName) {

    this.ensureSheet(sheetName).clearContents();

  }

  appendRows(sheetName, headers, rows) {

    if (!rows || rows.length === 0) {
      return;
    }

    const sheet =
      this.ensureSheet(sheetName);

    if (sheet.getLastRow() === 0) {

      sheet
        .getRange(
          1,
          1,
          1,
          headers.length
        )
        .setValues([headers]);

    }

    rows.forEach((row, index) => {

      if (row.length !== headers.length) {

        throw new Error(
          "Row " +
          (index + 1) +
          " has " +
          row.length +
          " columns. Expected " +
          headers.length
        );

      }

    });

    sheet
      .getRange(
        sheet.getLastRow() + 1,
        1,
        rows.length,
        headers.length
      )
      .setValues(rows);

  }

  writeTable(sheetName, rows) {

    if (!rows || rows.length === 0) {
      return;
    }

    const sheet =
      this.ensureSheet(sheetName);

    sheet.clearContents();

    sheet
      .getRange(
        1,
        1,
        rows.length,
        rows[0].length
      )
      .setValues(rows);

  }

}