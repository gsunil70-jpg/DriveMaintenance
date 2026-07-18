/**
 * ============================================================
 * DriveMaintenance v1.0
 * Recommendation Runner
 * ============================================================
 *
 * Orchestrates the recommendation workflow.
 *
 * Workflow
 * --------
 * Duplicate Detector
 *        ↓
 * Recommendation Engine
 *        ↓
 * Action Queue
 *
 * This file contains NO business rules.
 * ============================================================
 */

function generateActionQueue() {

  Logger.log(
    "Recommendation workflow started."
  );


  // ----------------------------------------------------------
  // Detect duplicate groups
  // ----------------------------------------------------------

  const duplicateGroups =
    detectDuplicateGroups();


  Logger.log(
    duplicateGroups.length +
    " duplicate groups detected."
  );


  // ----------------------------------------------------------
  // Generate recommendations
  // ----------------------------------------------------------

  const engine =
    new RecommendationEngine();


  const recommendations =
    engine.generate(
      duplicateGroups
    );


  Logger.log(
    recommendations.length +
    " recommendations generated."
  );


  // ----------------------------------------------------------
  // Build Action Queue
  // ----------------------------------------------------------

  const queue =
    new ActionQueue();


  queue.write(
    recommendations
  );


  Logger.log(
    "Recommendation workflow completed."
  );

}