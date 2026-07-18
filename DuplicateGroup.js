/**
 * ============================================================
 * DriveMaintenance v1.0
 * Duplicate Group
 * ============================================================
 * Represents a relationship between possible duplicate objects.
 */

class DuplicateGroup {

  constructor(data = {}) {

    // Identity

    this.groupId = data.groupId || "";


    // Matching fingerprint

    this.fingerprint = data.fingerprint || "";


    // Files belonging to this group

    this.members = data.members || [];


    // Verification state

    this.verificationStatus =
      data.verificationStatus || "UNVERIFIED";


    // Confidence

    this.confidence =
      data.confidence || "LOW";


    // Preferred object

    this.primaryCandidate =
      data.primaryCandidate || null;


    // Decision

    this.recommendation =
      data.recommendation || "REVIEW";


    // Explanation

    this.reason =
      data.reason || "";

  }


  addMember(storageObject) {

    this.members.push(storageObject);

  }


  size() {

    return this.members.length;

  }

}