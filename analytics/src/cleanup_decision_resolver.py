"""
DriveMaintenance
Cleanup Decision Resolver

Converts recommendations into a proposed cleanup plan.

No Drive modification.
No deletion.
Human approval required.
"""


from pathlib import Path



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


            canonical = recommendation.get(
                "canonical",
                {}
            )


            if action == "KEEP_BACKUP_REMOVE_NON_BACKUP":


                for file in files:


                    if file.get(
                        "Inside Backup"
                    ) == "TRUE":


                        decision = "KEEP"

                        resolution = (
                            "KEEP_CANONICAL"
                        )


                    else:


                        decision = "REVIEW_REMOVE"


                        if self.same_folder(
                            file,
                            canonical
                        ):

                            resolution = (
                                "CONSOLIDATE"
                            )

                        else:

                            resolution = (
                                "REDIRECT_TO_CANONICAL"
                            )



                    plan.append(

                        self.create_record(

                            file,

                            decision,

                            recommendation["reason"],

                            canonical,

                            resolution

                        )

                    )



            else:


                for file in files:


                    plan.append(

                        self.create_record(

                            file,

                            "REVIEW",

                            recommendation["reason"],

                            canonical,

                            "MANUAL_REVIEW"

                        )

                    )



        return plan




    def same_folder(
        self,
        file,
        canonical
    ):

        file_path = Path(
            file.get("Path", "")
        )


        canonical_path = Path(
            canonical.get("Path", "")
        )


        return (

            file_path.parent
            ==
            canonical_path.parent

        )





    def create_record(

        self,

        file,

        decision,

        reason,

        canonical,

        resolution

    ):


        return {


            "Decision":

                decision,


            "Resolution Mode":

                resolution,


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


            "Canonical File ID":

                canonical.get("File ID"),


            "Canonical File Name":

                canonical.get("File Name"),


            "Canonical Path":

                canonical.get("Path")

        }