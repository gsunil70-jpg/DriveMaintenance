/**
 * ============================================================
 * DriveMaintenance v1.2
 * Storage Statistics
 * ============================================================
 *
 * Calculates inventory statistics for a StorageCatalog.
 *
 * Responsibilities
 * ----------------
 * • Calculate storage metrics
 * • Return plain data objects
 *
 * This class contains NO:
 * • Spreadsheet logic
 * • Google Drive logic
 * • Logging
 * • Formatting
 * ============================================================
 */

class StorageStatistics {

  /**
   * @param {StorageCatalog} catalog
   */
  constructor(catalog) {

    this.catalog = catalog;

  }


  /**
   * Returns a summary of the catalog.
   *
   * @returns {Object}
   */
  summary() {

    const files =
      this.catalog.getFiles();

    const folders =
      this.catalog.getFolders();

    const backupObjects =
      this.catalog.insideBackup();

    const nonBackupObjects =
      this.catalog.outsideBackup();

    return {

      totalObjects:
        this.catalog.count(),

      totalFiles:
        files.length,

      totalFolders:
        folders.length,

      backupObjects:
        backupObjects.length,

      nonBackupObjects:
        nonBackupObjects.length,

      totalSize:
        this.catalog.totalSize(),

      largestFile:
        this.catalog.largestFile()

    };

  }


  /**
   * Calculates backup coverage.
   *
   * Measures both:
   * - object count coverage
   * - storage size coverage
   *
   * @returns {Object}
   */
  backupCoverage() {

    const totalObjects =
      this.catalog.count();


    const backupObjects =
      this.catalog.insideBackup();


    const nonBackupObjects =
      this.catalog.outsideBackup();


    const totalSize =
      this.catalog.totalSize();


    const backupSize =
      backupObjects

        .filter(function(object) {

          return object.objectType === OBJECT_TYPE.FILE;

        })

        .reduce(function(total, object) {

          return total + object.size;

        }, 0);



    return {

      totalObjects:

        totalObjects,


      backupObjects:

        backupObjects.length,


      nonBackupObjects:

        nonBackupObjects.length,


      objectCoveragePercent:

        totalObjects === 0
          ? 0
          : (backupObjects.length / totalObjects) * 100,


      totalSize:

        totalSize,


      backupSize:

        backupSize,


      sizeCoveragePercent:

        totalSize === 0
          ? 0
          : (backupSize / totalSize) * 100

    };

  }


}