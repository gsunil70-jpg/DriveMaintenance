/**
 * ============================================================
 * DriveMaintenance v1.3
 * Constants
 * ============================================================
 *
 * Central configuration and sheet definitions.
 * This file should contain only constants.
 * ============================================================
 */


/**
 * Google Spreadsheet Configuration
 */
const SPREADSHEET_ID = "1X9Uov60kbo0mMppljpYe6P11S8RBi7cg4Vc7c8ukfas";


/**
 * Spreadsheet Sheet Names
 */
const SHEETS = {

  DRIVE_INDEX: "Drive Index",

  STORAGE_CATALOG: "Storage Catalog",

  DUPLICATE_REPORT: "Duplicate Report",

  ACTION_QUEUE: "Action Queue",

  ANALYSIS: "Analysis",

  AUDIT_LOG: "Audit Log"

};


/**
 * Backup Configuration
 */
const BACKUP_CONFIG = {

  BACKUP_FOLDER_NAME: "Drive Backup",

  MOVE_TO_TRASH_ONLY: true

};


/**
 * Scanner Configuration
 */
const SCAN_CONFIG = {

  VERSION: "1.3",

  // Number of files processed per execution
  SCAN_BATCH_SIZE: 500,

  // Maximum runtime safety margin
  MAX_RUNTIME_SECONDS: 300,

  // Continue token storage key
  STATE_KEY: "DRIVE_SCAN_STATE"

};


/**
 * Drive Index Columns
 *
 * Keep this aligned with Drive Index sheet.
 */
const DRIVE_INDEX_COLUMNS = {

  ID: "id",

  NAME: "name",

  MIME_TYPE: "mimeType",

  SIZE: "size",

  CREATED: "created",

  UPDATED: "updated",

  OWNER: "owner",

  PATH: "path",

  TRASHED: "trashed"

};


/**
 * Storage Classification
 */
const STORAGE_CLASS = {

  ACTIVE: "ACTIVE",

  ARCHIVE: "ARCHIVE",

  BACKUP: "BACKUP",

  REVIEW: "REVIEW",

  DUPLICATE: "DUPLICATE"

};


/**
 * Recommendation Actions
 */
const ACTIONS = {

  KEEP: "KEEP",

  REVIEW: "REVIEW",

  ARCHIVE: "ARCHIVE",

  MOVE_TO_BACKUP: "MOVE_TO_BACKUP",

  MOVE_TO_TRASH: "MOVE_TO_TRASH"

};


/**
 * Logging
 */
const LOG_CONFIG = {

  ENABLED: true,

  LEVEL: "INFO"

};