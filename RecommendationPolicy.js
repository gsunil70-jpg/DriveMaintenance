/**
 * ============================================================
 * DriveMaintenance v1.2
 * Recommendation Policy
 * ============================================================
 *
 * Converts Duplicate Groups into Recommendations.
 *
 * Responsibilities
 * ----------------
 * • Evaluate duplicate groups
 * • Calculate confidence
 * • Produce recommendations
 *
 * Contains NO:
 * • Spreadsheet logic
 * • Google Drive logic
 * ============================================================
 */

class RecommendationPolicy {


  /**
   * Evaluates a duplicate group.
   *
   * @param {DuplicateGroup} group
   * @returns {Recommendation}
   */
  evaluate(group) {


    if (!group) {

      return this.manualReview(
        "",
        "Duplicate group is missing."
      );

    }


    if (!group.members ||
        group.members.length < 2) {


      return this.manualReview(

        group.groupId,

        "Duplicate group contains fewer than two files."

      );

    }


    const evaluation =
      this.evaluateEvidence(group);



    if (evaluation.score >= 80) {


      return new Recommendation({

        groupId:
          group.groupId,

        action:
          RECOMMENDATION_ACTION.VERIFY_CHECKSUM,

        confidence:
          evaluation.score,

        risk:
          RISK_LEVEL.LOW,

        priority:
          PRIORITY.HIGH,

        reason:
          evaluation.reason

      });


    }



    if (evaluation.score >= 50) {


      return new Recommendation({

        groupId:
          group.groupId,

        action:
          RECOMMENDATION_ACTION.MANUAL_REVIEW,

        confidence:
          evaluation.score,

        risk:
          RISK_LEVEL.MEDIUM,

        priority:
          PRIORITY.MEDIUM,

        reason:
          evaluation.reason

      });


    }



    return this.manualReview(

      group.groupId,

      evaluation.reason

    );


  }



  /**
   * Calculates duplicate evidence.
   *
   * @param {DuplicateGroup} group
   * @returns {Object}
   */
  evaluateEvidence(group) {


    const files =
      group.members;


    const first =
      files[0];


    let score = 0;


    const reasons = [];



    const sameName =
      files.every(function(file) {

        return file.name === first.name;

      });



    if (sameName) {

      score += 30;

      reasons.push(
        "Same filename."
      );

    }



    const sameSize =
      files.every(function(file) {

        return file.size === first.size;

      });



    if (sameSize) {

      score += 30;

      reasons.push(
        "Same file size."
      );

    }



    const sameMime =
      files.every(function(file) {

        return file.mimeType === first.mimeType;

      });



    if (sameMime) {

      score += 15;

      reasons.push(
        "Same file type."
      );

    }



    const backupPresent =
      files.some(function(file) {

        return file.isInBackup;

      });



    if (backupPresent) {

      score += 15;

      reasons.push(
        "Backup copy exists."
      );

    }



    return {

      score: score,

      reason:
        reasons.join(" ")

    };


  }



  /**
   * Manual review recommendation.
   */
  manualReview(groupId, reason) {


    return new Recommendation({

      groupId: groupId,

      action:
        RECOMMENDATION_ACTION.MANUAL_REVIEW,

      confidence: 40,

      risk:
        RISK_LEVEL.MEDIUM,

      priority:
        PRIORITY.MEDIUM,

      reason: reason

    });


  }


}