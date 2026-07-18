/**
 * ============================================================
 * DriveMaintenance v1.2
 * Storage Summary Report
 * ============================================================
 *
 * Generates a summary of the storage catalog.
 *
 * Responsibilities
 * ----------------
 * • Build StorageCatalog
 * • Generate StorageStatistics
 * • Write Storage Summary report
 *
 * Contains NO business logic.
 * ============================================================
 */

/**
 * Generates the Storage Summary report.
 */
function generateStorageSummary() {

  const catalog =
    buildStorageCatalog();

  const statistics =
    new StorageStatistics(catalog);

  const summary =
    statistics.summary();


  const rows = [

    ["Metric", "Value"],

    ["Total Objects", summary.totalObjects],

    ["Total Files", summary.totalFiles],

    ["Total Folders", summary.totalFolders],

    ["Objects Inside Backup", summary.backupObjects],

    ["Objects Outside Backup", summary.nonBackupObjects],

    ["Total Size (Bytes)", summary.totalSize],

    [
      "Largest File",
      summary.largestFile
        ? summary.largestFile.name
        : ""
    ],

    [
      "Largest File Size (Bytes)",
      summary.largestFile
        ? summary.largestFile.size
        : 0
    ]

  ];


  const writer =
    new ReportWriter();

  writer.writeTable(
    SHEETS.STORAGE_SUMMARY,
    rows
  );


  Logger.log(
    "Storage Summary report generated."
  );

}