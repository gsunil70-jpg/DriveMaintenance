/**
 * ============================================================
 * DriveMaintenance v1.0
 * Storage Classifier
 * ============================================================
 * Classifies catalog objects and writes Analysis sheet.
 */

function generateAnalysis() {

  const catalog = buildStorageCatalog();

  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);

  const sheet = ss.getSheetByName(SHEETS.ANALYSIS);

  if (!sheet) {
    throw new Error("Analysis sheet not found.");
  }


  // Clear old analysis

  sheet.clear();


  // Header

  const output = [];

  output.push([
    "File ID",
    "Name",
    "Path",
    "Inside Backup",
    "Classification",
    "Recommendation",
    "Risk",
    "Reason"
  ]);


  // Classify objects

  catalog.getAll().forEach(function(object) {

    let classification;
    let recommendation;
    let risk;
    let reason;


    if (object.isInBackup) {

      classification = "BACKUP_OBJECT";
      recommendation = "KEEP";
      risk = "NONE";
      reason = "Object already exists inside backup.";

    } 
    else {

      classification = "NON_BACKUP_OBJECT";
      recommendation = "REVIEW";
      risk = "LOW";
      reason = "Object is outside backup location.";

    }


    output.push([

      object.objectId,
      object.name,
      object.path,
      object.isInBackup,
      classification,
      recommendation,
      risk,
      reason

    ]);

  });


  // Write output

  sheet
    .getRange(
      1,
      1,
      output.length,
      output[0].length
    )
    .setValues(output);


  Logger.log(
    "Analysis generated. Objects analysed: "
    + catalog.count()
  );

}