"""
Workflow timeline generator.
"""


class TimelineGenerator:

    @staticmethod
    def generate(queue_name: str):

        return [
            "Request Submitted",
            "Request Classified",
            "Entities Extracted",
            "Priority Assessed",
            "Decision Generated",
            "Routing Decision Created",
            "Ticket Generated",
            f"Assigned to {queue_name}"
        ]