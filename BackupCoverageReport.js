/**
 * ============================================================
 * DriveMaintenance v1.2
 * Backup Coverage Report
 * ============================================================
 *
 * Generates backup coverage intelligence report.
 *
 * Responsibilities
 * ----------------
 * • Build catalog
 * • Calculate backup coverage
 * • Write report
 *
 * Contains NO:
 * • Google Drive logic
 * • Business rules
 * • Calculations
 * ============================================================
 */


function generateBackupCoverageReport() {


  const catalog =
    buildStorageCatalog();


  const statistics =
    new StorageStatistics(catalog);


  const coverage =
    statistics.backupCoverage();



  const rows = [

    [
      "Metric",
      "Value"
    ],


    [
      "Total Objects",
      coverage.totalObjects
    ],


    [
      "Backup Objects",
      coverage.backupObjects
    ],


    [
      "Non Backup Objects",
      coverage.nonBackupObjects
    ],


    [
      "Object Coverage %",
      coverage.objectCoveragePercent.toFixed(2)
    ],


    [
      "Total Size (Bytes)",
      coverage.totalSize
    ],


    [
      "Backup Size (Bytes)",
      coverage.backupSize
    ],


    [
      "Size Coverage %",
      coverage.sizeCoveragePercent.toFixed(2)
    ]

  ];



  const writer =
    new ReportWriter();


  writer.writeTable(

    "Backup Coverage",

    rows

  );


  Logger.log(
    "Backup Coverage report generated."
  );


}