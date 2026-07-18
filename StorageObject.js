/**
 * ============================================================
 * DriveMaintenance v1.0
 * Storage Object
 * ============================================================
 * Canonical representation of a storage object.
 */

class StorageObject {

  constructor(data = {}) {

    // ---------- Identity ----------
    this.objectId = data.objectId || "";
    this.provider = data.provider || PROVIDER.GOOGLE_DRIVE;
    this.objectType = data.objectType || OBJECT_TYPE.UNKNOWN;

    // ---------- Metadata ----------
    this.name = data.name || "";
    this.mimeType = data.mimeType || "";
    this.size = Number(data.size || 0);
    this.checksum = data.checksum || "";

    this.createdAt = data.createdAt || "";
    this.modifiedAt = data.modifiedAt || "";

    // ---------- Location ----------
    this.parentId = data.parentId || "";
    this.path = data.path || "";

    this.isInBackup = Boolean(data.isInBackup);

    // ---------- Analysis ----------
    this.classification = CLASSIFICATION.UNKNOWN;

    // ---------- Planning ----------
    this.plannedAction = ACTION.NONE;

    // ---------- Execution ----------
    this.executionStatus = EXECUTION_STATUS.PENDING;

    // ---------- Audit ----------
    this.indexedAt = data.indexedAt || "";
  }

}