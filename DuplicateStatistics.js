/**
 * ============================================================
 * DriveMaintenance v1.2
 * Duplicate Statistics
 * ============================================================
 *
 * Calculates storage impact of duplicate groups.
 *
 * Responsibilities
 * ----------------
 * • Calculate duplicate metrics
 * • Estimate recoverable space
 *
 * Contains NO:
 * • Spreadsheet logic
 * • Google Drive logic
 * • Recommendations
 * ============================================================
 */


class DuplicateStatistics {


  /**
   * @param {DuplicateGroup[]} groups
   */
  constructor(groups = []) {

    this.groups = groups;

  }



  /**
   * Returns duplicate storage summary.
   *
   * @returns {Object}
   */
  summary() {


    let duplicateGroups = 0;

    let duplicateFiles = 0;

    let duplicateStorage = 0;

    let recoverableSpace = 0;



    this.groups.forEach(function(group) {


      const members =
        group.members;


      if (!members || members.length < 2) {
        return;
      }


      duplicateGroups++;


      let groupSize = 0;


      members.forEach(function(object) {

        duplicateFiles++;

        groupSize += Number(object.size || 0);

      });



      duplicateStorage += groupSize;



      /*
       * Keep one copy.
       * Remaining copies are recoverable.
       */

      const retainedCopySize =
        members[0].size || 0;


      recoverableSpace +=
        groupSize - retainedCopySize;


    });



    return {

      duplicateGroups:
        duplicateGroups,


      duplicateFiles:
        duplicateFiles,


      duplicateStorage:
        duplicateStorage,


      recoverableSpace:
        recoverableSpace

    };


  }


}