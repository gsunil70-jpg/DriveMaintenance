/**
 * ============================================================
 * DriveMaintenance v1.1
 * Catalog Builder
 * ============================================================
 *
 * Builds a StorageCatalog from the Drive Index sheet.
 *
 * Responsibilities
 * ----------------
 * • Read Drive Index
 * • Convert rows into StorageObjects
 * • Return StorageCatalog
 *
 * Contains NO:
 * • Google Drive scanning
 * • Spreadsheet writing
 * • Analysis logic
 * ============================================================
 */

function buildStorageCatalog() {

  // Open spreadsheet by ID

  const ss =
    SpreadsheetApp.openById(
      SPREADSHEET_ID
    );


  const sheet =
    ss.getSheetByName(
      SHEETS.DRIVE_INDEX
    );


  if (!sheet) {

    throw new Error(
      "Drive Index sheet not found."
    );

  }


  const values =
    sheet.getDataRange().getValues();


  if (values.length < 2) {

    Logger.log(
      "Drive Index is empty."
    );

    return new StorageCatalog();

  }


  // Build header lookup

  const headers =
    values[0];


  const col = {};


  headers.forEach(function(header, index) {

    col[String(header).trim()] = index;

  });



  const catalog =
    new StorageCatalog();



  // Read rows

  for (let i = 1; i < values.length; i++) {


    const row =
      values[i];


    const object =
      new StorageObject({


        objectId:
          row[col["File ID"]],


        name:
          row[col["Name"]],


        mimeType:
          row[col["MIME Type"]],


        size:
          row[col["Size"]],


        checksum:
          row[col["Checksum"]] || "",


        createdAt:
          row[col["Created"]],


        modifiedAt:
          row[col["Modified"]],


        path:
          row[col["Path"]],


        isInBackup:
          String(
            row[col["Inside Backup"]]
          ).toUpperCase() === "TRUE"


      });


    catalog.add(object);

  }



  Logger.log(
    "================================="
  );


  Logger.log(
    "Storage Catalog successfully built"
  );


  Logger.log(
    "Objects loaded: " + catalog.count()
  );


  Logger.log(
    "================================="
  );


  return catalog;

}