/**
 * ============================================================
 * DriveMaintenance
 * Execution Manifest Formatter
 * ============================================================
 *
 * Purpose:
 * --------
 * Makes Execution Manifest suitable for human approval review.
 *
 * No data modification.
 * No Drive modification.
 *
 * ============================================================
 */


function formatExecutionManifest() {


  const ss =
    SpreadsheetApp.openById(
      CONFIG.SPREADSHEET_ID
    );


  const sheet =
    ss.getSheetByName(
      "Execution Manifest"
    );


  if (!sheet) {

    throw new Error(
      "Execution Manifest sheet not found"
    );

  }


  const range =
    sheet.getDataRange();


  const headers =
    range
      .getValues()[0];


  const desiredOrder = [

    "Operation",
    "File Name",
    "Path",
    "Reason",
    "Approval Status",
    "Approved By",
    "Approval Date",
    "Approval Note",
    "File ID"

  ];


  const indexes =
    desiredOrder.map(
      h => headers.indexOf(h)
    );


  if (
    indexes.includes(-1)
  ) {

    throw new Error(
      "Required columns missing"
    );

  }


  const values =
    range.getValues();


  const reordered =
    values.map(row =>

    indexes.map(
      i => row[i]
    )

  );


  sheet.clear();


  sheet
    .getRange(
      1,
      1,
      reordered.length,
      reordered[0].length
    )
    .setValues(
      reordered
    );


  const header =
    sheet.getRange(
      1,
      1,
      1,
      desiredOrder.length
    );


  header
    .setFontWeight(
      "bold"
    );


  sheet
    .setFrozenRows(
      1
    );


  sheet
    .getDataRange()
    .createFilter();


  sheet
    .getRange(
      1,
      1,
      sheet.getLastRow(),
      sheet.getLastColumn()
    )
    .setWrap(
      true
    );


  const widths = [

    150, // Operation
    220, // File Name
    350, // Path
    300, // Reason
    130, // Approval Status
    150, // Approved By
    120, // Approval Date
    250, // Approval Note
    250  // File ID

  ];


  widths.forEach(
    (width, index) => {

      sheet.setColumnWidth(
        index + 1,
        width
      );

    }
  );


  Logger.log(
    "Execution Manifest formatted successfully"
  );


}