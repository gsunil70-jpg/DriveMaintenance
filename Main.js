/**
 * ============================================================
 * DriveMaintenance v1.0
 * Main
 * ============================================================
 *
 * Entry points only.
 * No workflow implementations.
 * ============================================================
 */


function testDriveMaintenance() {

  Logger.log(
    "DriveMaintenance is running."
  );

}



function runDuplicateAnalysis() {

  generateDuplicateReport();

}



function runRecommendationWorkflow() {

  generateActionQueue();

}



function runDriveScan() {

  const controller = new ScanController();

  controller.run();

}

function clearScanState() {

  const stateManager = new StateManager();

  stateManager.clear("SCAN_STATE");

  Logger.log("Scan state cleared.");

}
