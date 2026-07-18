"""
DriveMaintenance
Execution Validator
"""


class ExecutionValidator:
    """
    Validates the complete execution batch before
    any execution artifacts are produced.
    """


    def __init__(self, execution_plan):

        self.execution_plan = execution_plan



    def validate(self):

        errors = []

        seen_ids = set()


        allowed_operations = {

            "KEEP",

            "MANUAL_REVIEW",

            "MOVE_TO_TRASH",

        }



        for index, record in enumerate(

            self.execution_plan,

            start=1,

        ):


            file_id = (

                record.get("File ID") or ""

            ).strip()


            operation = record.get(

                "Operation",

                ""

            )


            if not file_id:

                errors.append(

                    f"Row {index}: Missing File ID."

                )


            elif file_id in seen_ids:

                errors.append(

                    f"Duplicate File ID: {file_id}"

                )


            else:

                seen_ids.add(file_id)



            if operation not in allowed_operations:

                errors.append(

                    f"Invalid operation '{operation}' "
                    f"for {file_id}"

                )



            #
            # Canonical reference safety rule
            #

            if operation == "MOVE_TO_TRASH":


                canonical_id = (

                    record.get(
                        "Canonical File ID"
                    )

                    or ""

                ).strip()



                canonical_path = (

                    record.get(
                        "Canonical Path"
                    )

                    or ""

                ).strip()



                if not canonical_id:

                    errors.append(

                        f"Row {index}: "
                        "MOVE_TO_TRASH has no canonical reference."

                    )


                elif canonical_id == file_id:

                    errors.append(

                        f"Row {index}: "
                        "Removal candidate points to itself as canonical."

                    )


                if not canonical_path:

                    errors.append(

                        f"Row {index}: "
                        "Missing canonical path."

                    )



        return {

            "valid":

                len(errors) == 0,


            "errors":

                errors,


            "record_count":

                len(self.execution_plan),

        }