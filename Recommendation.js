/**
 * ============================================================
 * DriveMaintenance v1.0
 * Recommendation
 * ============================================================
 * Represents a single recommendation produced by the
 * Recommendation Engine.
 *
 * This class is intentionally independent of:
 * - Google Drive
 * - Google Sheets
 * - Duplicate Detection
 * - Recommendation Policy
 */

class Recommendation {

  constructor(data = {}) {

    // ---------- Identity ----------

    this.groupId =
      data.groupId || "";


    // ---------- Decision ----------

    this.action =
      data.action ||
      RECOMMENDATION_ACTION.MANUAL_REVIEW;

    this.confidence =
      Number(data.confidence ?? 0);

    this.risk =
      data.risk ||
      RISK_LEVEL.LOW;

    this.priority =
      data.priority ||
      PRIORITY.MEDIUM;


    // ---------- Explanation ----------

    this.reason =
      data.reason || "";


    // ---------- Workflow ----------

    this.status =
      data.status ||
      EXECUTION_STATUS.PENDING;


    // ---------- Audit ----------

    this.generatedAt =
      data.generatedAt || new Date();

  }


  /**
   * Returns a spreadsheet row.
   *
   * @returns {Array}
   */
  toRow() {

    return [

      this.priority,
      this.groupId,
      this.action,
      this.confidence,
      this.risk,
      this.reason,
      this.status,
      this.generatedAt

    ];

  }

}