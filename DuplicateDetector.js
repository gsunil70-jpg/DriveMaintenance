/**
 * ============================================================
 * DriveMaintenance v1.0
 * Duplicate Detector
 * ============================================================
 * Detects probable duplicate files using:
 *
 * Name + Size
 *
 * Output:
 * DuplicateGroup[]
 *
 * Future enhancements:
 * - Content checksum
 * - Version detection
 * - Similarity analysis
 * ============================================================
 */


/**
 * Detects duplicate groups from storage catalog.
 *
 * @returns {DuplicateGroup[]}
 */
function detectDuplicateGroups() {

  const catalog =
    buildStorageCatalog();


  const groups = {};


  /**
   * Group files by name + size
   */
  catalog.getAll().forEach(function(object) {


    // Ignore folders

    if (object.objectType === OBJECT_TYPE.FOLDER) {
      return;
    }


    const fingerprint =
      object.name +
      "|" +
      object.size;


    if (!groups[fingerprint]) {

      groups[fingerprint] = [];

    }


    groups[fingerprint].push(object);

  });


  const duplicateGroups = [];

  let groupNumber = 1;


  /**
   * Convert matching files into DuplicateGroup objects
   */
  Object.keys(groups).forEach(function(fingerprint) {


    const members =
      groups[fingerprint];


    if (members.length > 1) {


      duplicateGroups.push(

        new DuplicateGroup({

          groupId:
            "DUP-" + groupNumber,

          fingerprint:
            fingerprint,

          members:
            members

        })

      );


      groupNumber++;

    }

  });


  Logger.log(
    "Duplicate groups detected: "
    + duplicateGroups.length
  );


  return duplicateGroups;

}





/**
 * Generates the human-readable duplicate report.
 *
 * This function preserves the existing reporting workflow.
 */
function generateDuplicateReport() {


  const duplicateGroups =
    detectDuplicateGroups();


  const ss =
    SpreadsheetApp.openById(
      SPREADSHEET_ID
    );


  const sheet =
    ss.getSheetByName(
      SHEETS.DUPLICATE_REPORT
    );


  if (!sheet) {

    throw new Error(
      "Duplicate Report sheet not found."
    );

  }


  sheet.clear();


  const output = [];


  output.push([

    "Group ID",
    "File Name",
    "Size",
    "File ID",
    "Path",
    "Inside Backup"

  ]);



  duplicateGroups.forEach(function(group) {


    group.members.forEach(function(object) {


      output.push([

        group.groupId,

        object.name,

        object.size,

        object.objectId,

        object.path,

        object.isInBackup

      ]);

    });


  });



  if (output.length > 1) {


    sheet
      .getRange(
        1,
        1,
        output.length,
        output[0].length
      )
      .setValues(output);

  }


  Logger.log(
    "Duplicate report generated. Groups: "
    + duplicateGroups.length
  );


}