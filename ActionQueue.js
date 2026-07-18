/**
 * ============================================================
 * DriveMaintenance v1.0
 * Action Queue
 * ============================================================
 *
 * Responsible for writing recommendations into the
 * Action Queue worksheet.
 *
 * Responsibilities
 * ----------------
 * • Convert Recommendation objects into spreadsheet rows
 * • Delegate spreadsheet writing to ReportWriter
 *
 * This class contains NO recommendation logic.
 * ============================================================
 */

class ActionQueue {

  constructor() {

    this.reportWriter =
      new ReportWriter();

  }


  /**
   * Writes recommendations to the Action Queue sheet.
   *
   * @param {Recommendation[]} recommendations
   */
  write(recommendations = []) {

    const headers = [

      "Priority",
      "Group ID",
      "Action",
      "Confidence",
      "Risk",
      "Reason",
      "Status",
      "Created"

    ];


    const rows = recommendations.map(function(recommendation) {

      return recommendation.toRow();

    });


    this.reportWriter.appendRows(

      SHEETS.ACTION_QUEUE,

      headers,

      rows

    );


    Logger.log(

      rows.length +
      " recommendation(s) written to Action Queue."

    );

  }

}