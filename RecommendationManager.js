/**
 * ============================================================
 * DriveMaintenance v1.0
 * Recommendation Runner
 * ============================================================
 *
 * Workflow:
 *
 * Duplicate Detection
 *        ↓
 * Recommendation Engine
 *        ↓
 * Action Queue
 *
 * This file contains:
 * - workflow orchestration only
 *
 * This file does NOT contain:
 * - Recommendation rules
 * - ActionQueue class
 * ============================================================
 */


/**
 * Entry point:
 * Generates recommendations and populates Action Queue.
 */
function generateActionQueue() {

  Logger.log(
    "Starting recommendation workflow..."
  );


  // ----------------------------------------------------------
  // Step 1: Detect duplicate candidates
  // ----------------------------------------------------------

  const duplicateGroups =
    detectDuplicateGroups();


  Logger.log(
    "Duplicate groups found: " +
    duplicateGroups.length
  );


  // ----------------------------------------------------------
  // Step 2: Generate recommendations
  // ----------------------------------------------------------

  const recommendationEngine =
    new RecommendationEngine();


  const recommendations =
    recommendationEngine.generate(
      duplicateGroups
    );


  Logger.log(
    "Recommendations generated: " +
    recommendations.length
  );


  // ----------------------------------------------------------
  // Step 3: Write Action Queue
  // ----------------------------------------------------------

  const queue =
    new ActionQueue();


  queue.write(
    recommendations
  );


  Logger.log(
    "Action Queue generation completed."
  );

}