"""
DriveMaintenance
Execution Planner
"""

from analytics.src.execution_plan_builder import ExecutionPlanBuilder
from analytics.src.safety_validator import SafetyValidator
from analytics.src.execution_validator import ExecutionValidator
from analytics.src.cleanup_script_generator import CleanupScriptGenerator
from analytics.src.rollback_generator import RollbackGenerator


class ExecutionPlanner:
    """
    Coordinates the complete execution pipeline.
    """

    def __init__(self, cleanup_plan):

        self.cleanup_plan = cleanup_plan

    def build(self):

        execution_plan = (
            ExecutionPlanBuilder(
                self.cleanup_plan
            ).build()
        )

        execution_plan = (
            SafetyValidator(
                execution_plan
            ).validate()
        )

        validation = (
            ExecutionValidator(
                execution_plan
            ).validate()
        )

        cleanup_script = (
            CleanupScriptGenerator(
                execution_plan
            ).generate()
        )

        rollback = (
            RollbackGenerator(
                execution_plan
            ).generate()
        )

        return {

            "execution_plan": execution_plan,

            "validation": validation,

            "cleanup_script": cleanup_script,

            "rollback": rollback,

        }