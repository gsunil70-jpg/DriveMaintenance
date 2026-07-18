"""
DriveMaintenance
Cleanup Decision Resolver

Converts recommendations into a proposed cleanup plan.

No Drive modification.
No deletion.
Human approval required.
"""


class CleanupDecisionResolver:


    PROTECTED_ACTIONS = {

        "REVIEW"

    }



    def resolve(
        self,
        groups,
        engine
    ):

        plan = []


        for group in groups:


            recommendation = engine.recommend(
                group
            )


            action = recommendation["action"]


            files = group["files"]


            canonical = (
                recommendation.get(
                    "canonical",
                    {}
                )
            )


            if action == "KEEP_BACKUP_REMOVE_NON_BACKUP":


                for file in files:


                    if file.get(
                        "Inside Backup"
                    ) == "TRUE":


                        decision = "KEEP"


                    else:


                        decision = "REVIEW_REMOVE"



                    plan.append(

                        self.create_record(

                            file,

                            decision,

                            recommendation["reason"],

                            canonical

                        )

                    )



            else:


                for file in files:


                    plan.append(

                        self.create_record(

                            file,

                            "REVIEW",

                            recommendation["reason"],

                            canonical

                        )

                    )


        return plan





    def create_record(

        self,

        file,

        decision,

        reason,

        canonical

    ):


        return {


            "Decision":

                decision,


            "File ID":

                file.get("File ID"),


            "File Name":

                file.get("Name"),


            "Path":

                file.get("Path"),


            "Size":

                file.get("Size"),


            "Inside Backup":

                file.get("Inside Backup"),


            "Reason":

                reason,


            #
            # Canonical reference
            #

            "Canonical File ID":

                canonical.get("File ID"),


            "Canonical File Name":

                canonical.get("File Name"),


            "Canonical Path":

                canonical.get("Path")

        }