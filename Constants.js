/**
 * ============================================================
 * DriveMaintenance v1.0
 * Constants
 * ============================================================
 * Shared constants used throughout the project.
 * This file should contain only constant definitions.
 */

/**
 * Google Spreadsheet Configuration
 */
const SPREADSHEET_ID = "1X9Uov60kbo0mMppljpYe6P11S8RBi7cg4Vc7c8ukfas";

/**
 * Spreadsheet sheet names
 */
const SHEETS = Object.freeze({
  DRIVE_INDEX: "Drive Index",
  ANALYSIS: "Analysis",
  MIGRATION_PLAN: "Migration Plan",
  EXECUTION_LOG: "Execution Log",
  DASHBOARD: "Dashboard",
  DUPLICATE_REPORT: "Duplicate Report",
  ACTION_QUEUE: "Action Queue"
});

/**
 * Storage providers
 */
const PROVIDER = Object.freeze({
  GOOGLE_DRIVE: "GoogleDrive"
});

/**
 * Object types
 */
const OBJECT_TYPE = Object.freeze({
  FILE: "FILE",
  FOLDER: "FOLDER",
  SHORTCUT: "SHORTCUT",
  UNKNOWN: "UNKNOWN"
});

/**
 * Storage classification
 */
const CLASSIFICATION = Object.freeze({
  UNKNOWN: "UNKNOWN",
  SAFE: "SAFE",
  DUPLICATE: "DUPLICATE",
  MISSING_BACKUP: "MISSING_BACKUP",
  BACKUP_ONLY: "BACKUP_ONLY",
  CONFLICT: "CONFLICT",
  REVIEW_REQUIRED: "REVIEW_REQUIRED"
});

/**
 * Planned execution actions
 *
 * These represent physical actions that may eventually
 * be executed against Google Drive.
 */
const ACTION = Object.freeze({
  NONE: "NONE",
  KEEP: "KEEP",
  MOVE: "MOVE",
  TRASH: "TRASH",
  REVIEW: "REVIEW"
});

/**
 * Recommendation Engine actions
 *
 * These represent decisions produced by the
 * Recommendation Engine.
 */
const RECOMMENDATION_ACTION = Object.freeze({
  KEEP: "KEEP",
  VERIFY_CHECKSUM: "VERIFY_CHECKSUM",
  MOVE_TO_BACKUP: "MOVE_TO_BACKUP",
  MOVE_TO_REVIEW: "MOVE_TO_REVIEW",
  MANUAL_REVIEW: "MANUAL_REVIEW"
});

/**
 * Recommendation confidence
 */
const CONFIDENCE_LEVEL = Object.freeze({
  VERY_LOW: "VERY_LOW",
  LOW: "LOW",
  MEDIUM: "MEDIUM",
  HIGH: "HIGH",
  VERY_HIGH: "VERY_HIGH"
});

/**
 * Recommendation risk
 */
const RISK_LEVEL = Object.freeze({
  LOW: "LOW",
  MEDIUM: "MEDIUM",
  HIGH: "HIGH"
});

/**
 * Recommendation priority
 */
const PRIORITY = Object.freeze({
  HIGH: "HIGH",
  MEDIUM: "MEDIUM",
  LOW: "LOW"
});

/**
 * Duplicate verification status
 */
const VERIFICATION_STATUS = Object.freeze({
  UNVERIFIED: "UNVERIFIED",
  VERIFIED: "VERIFIED",
  FAILED: "FAILED"
});

/**
 * Execution status
 */
const EXECUTION_STATUS = Object.freeze({
  PENDING: "PENDING",
  SUCCESS: "SUCCESS",
  FAILED: "FAILED",
  SKIPPED: "SKIPPED",
  COMPLETED: "COMPLETED"
});