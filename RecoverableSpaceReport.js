/**
 * ============================================================
 * DriveMaintenance v1.2
 * Recoverable Space Report
 * ============================================================
 *
 * Generates duplicate storage impact report.
 *
 * Responsibilities
 * ----------------
 * • Obtain duplicate groups
 * • Calculate recoverable space
 * • Write report
 *
 * Contains NO:
 * • Duplicate logic
 * • Spreadsheet calculations
 * ============================================================
 */


function generateRecoverableSpaceReport() {


  const groups =
    detectDuplicateGroups();



  const statistics =
    new DuplicateStatistics(groups);



  const summary =
    statistics.summary();



  const rows = [

    [
      "Metric",
      "Value"
    ],


    [
      "Duplicate Groups",
      summary.duplicateGroups
    ],


    [
      "Duplicate Files",
      summary.duplicateFiles
    ],


    [
      "Duplicate Storage (Bytes)",
      summary.duplicateStorage
    ],


    [
      "Estimated Recoverable Space (Bytes)",
      summary.recoverableSpace
    ]

  ];



  const writer =
    new ReportWriter();



  writer.writeTable(

    "Recoverable Space",

    rows

  );


  Logger.log(
    "Recoverable Space report generated."
  );


}