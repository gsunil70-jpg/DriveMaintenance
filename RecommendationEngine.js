/**
 * ============================================================
 * DriveMaintenance v1.0
 * Recommendation Engine
 * ============================================================
 * Coordinates recommendation generation.
 *
 * Responsibilities
 * ----------------
 * • Iterate through Duplicate Groups
 * • Delegate evaluation to RecommendationPolicy
 * • Return Recommendation objects
 *
 * This class contains NO business rules,
 * NO spreadsheet logic and NO Google Drive logic.
 */

class RecommendationEngine {

  constructor(policy = new RecommendationPolicy()) {

    this.policy = policy;

  }


  /**
   * Generates recommendations for all duplicate groups.
   *
   * @param {DuplicateGroup[]} groups
   * @returns {Recommendation[]}
   */
  generate(groups = []) {

    const recommendations = [];

    for (const group of groups) {

      recommendations.push(
        this.policy.evaluate(group)
      );

    }

    return recommendations;

  }

}