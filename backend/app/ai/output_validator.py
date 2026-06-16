"""
Validates and enriches LLM output.

Local LLMs occasionally return:
- Missing fields
- Empty fields
- Null values
- Incorrect entity structures

This validator ensures the workflow
always receives usable data.
"""


class OutputValidator:

    @staticmethod
    def validate(result: dict) -> dict:
        """
        Validate and enrich LLM output.
        """

        # ----------------------------------
        # Ensure entities object exists
        # ----------------------------------

        entities = result.get("entities")

        if not isinstance(entities, dict):
            entities = {}

        # ----------------------------------
        # Normalize entity fields
        # ----------------------------------

        symptoms = entities.get("symptoms")

        if symptoms is None:
            symptoms = []

        medications = entities.get("medications")

        if medications is None:
            medications = []

        specialty = entities.get("specialty")

        issue_type = entities.get("issue_type")

        entities = {
            "symptoms": symptoms,
            "medications": medications,
            "specialty": specialty,
            "issue_type": issue_type
        }

        result["entities"] = entities

        # ----------------------------------
        # Request Type
        # ----------------------------------

        request_type = result.get("request_type")

        if not request_type:
            request_type = "General Inquiry"

            result["request_type"] = request_type

        # ----------------------------------
        # Priority
        # ----------------------------------

        if not result.get("priority"):
            result["priority"] = "Medium"

        # ----------------------------------
        # Decision Fallback
        # ----------------------------------

        if not result.get("decision"):

            decision_map = {
                "Symptom Report":
                    "Medical review required",

                "Appointment Request":
                    "Appointment scheduling required",

                "Prescription Refill":
                    "Medication refill review required",

                "Billing Query":
                    "Billing review required",

                "Insurance Query":
                    "Insurance review required",

                "Lab Result Query":
                    "Lab result review required",

                "Medical Records Request":
                    "Records retrieval required",

                "General Inquiry":
                    "General support required"
            }

            result["decision"] = decision_map.get(
                request_type,
                "Manual review required"
            )

        # ----------------------------------
        # Department Fallback
        # ----------------------------------

        if not result.get("department"):

            department_map = {
                "Symptom Report":
                    "Emergency Department",

                "Appointment Request":
                    "Appointment Scheduling",

                "Prescription Refill":
                    "Pharmacy",

                "Billing Query":
                    "Billing Department",

                "Insurance Query":
                    "Insurance Desk",

                "Lab Result Query":
                    "Laboratory",

                "Medical Records Request":
                    "Medical Records Office",

                "General Inquiry":
                    "General Support"
            }

            result["department"] = department_map.get(
                request_type,
                "General Support"
            )

        # ----------------------------------
        # Explanation Fallback
        # ----------------------------------

        if not result.get("explanation"):

            result["explanation"] = (
                f"Request classified as "
                f"{result['request_type']} "
                f"and routed to "
                f"{result['department']}."
            )

        return result