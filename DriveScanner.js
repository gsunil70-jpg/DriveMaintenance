/**
 * ============================================================
 * DriveMaintenance v1.3
 * Drive Scanner
 * ============================================================
 *
 * Responsibilities
 * ----------------
 * • Scan Google Drive in resumable batches
 * • Save continuation token
 * • Populate DriveIndex only
 * • Never write to spreadsheets
 * ============================================================
 */

class DriveScanner {

  constructor(logger, index, stateManager) {

    this.logger = logger;
    this.index = index;
    this.stateManager = stateManager;
    this.pathResolver = new PathResolver();

  }

  scanBatch() {

    this.logger.log(
      "SCAN",
      "STARTED",
      "Starting scan batch"
    );

    let state =
      this.stateManager.get("SCAN_STATE") || {};

    let iterator;

    if (state.continuationToken) {

      iterator =
        DriveApp.continueFileIterator(
          state.continuationToken
        );

    } else {

      iterator =
        DriveApp.getFiles();

    }

    const startTime = Date.now();

    const MAX_RUNTIME = 330000;

    let processed = 0;

    while (iterator.hasNext()) {

      // Leave enough time for cleanup
      if (Date.now() - startTime >= MAX_RUNTIME) {

        this.logger.log(
          "SCAN",
          "CHECKPOINT",
          "Stopping before execution timeout"
        );

        break;

      }

      if (processed >= CONFIG.SCAN_BATCH_SIZE) {

        this.logger.log(
          "SCAN",
          "BATCH_LIMIT",
          "Batch limit reached"
        );

        break;

      }

      const file = iterator.next();

      const path =
        this.pathResolver.getFilePath(file);

      this.index.addFile({

        fileId: file.getId(),

        name: file.getName(),

        mimeType: file.getMimeType(),

        size: file.getSize(),

        checksum: "",

        createdDate: file.getDateCreated(),

        modifiedDate: file.getLastUpdated(),

        path: path,

        insideBackup:
          this.pathResolver.isInsideBackup(path)

      });

      processed++;

    }

    if (iterator.hasNext()) {

      state.continuationToken =
        iterator.getContinuationToken();

      state.completed = false;

    } else {

      state.continuationToken = null;

      state.completed = true;

    }
if (state.completed) {

  this.stateManager.clear(
    "SCAN_STATE"
  );

} else {

  this.stateManager.save(
    "SCAN_STATE",
    state
  );

}

this.logger.log(
  "SCAN",
  "BATCH_COMPLETED",
  "Processed " + processed + " file(s)"
);

if (state.completed) {

  this.logger.log(
    "SCAN",
    "COMPLETE",
    "Drive scan completed"
  );

}

return this.index;

  }

}