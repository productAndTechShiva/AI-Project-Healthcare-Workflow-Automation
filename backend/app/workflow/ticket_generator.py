"""
Ticket generation utilities.
"""

import uuid


class TicketGenerator:
    """
    Generates ticket IDs and summaries.
    """

    @staticmethod
    def generate_ticket_id() -> str:
        """
        Example:
        TKT-A1B2C3D4
        """

        unique_id = str(uuid.uuid4())[:8].upper()

        return f"TKT-{unique_id}"

    @staticmethod
    def generate_summary(
        request_type: str,
        priority: str,
        department: str
    ) -> str:
        """
        Generate ticket summary.
        """

        return (
            f"Request classified as {request_type}. "
            f"Priority level is {priority}. "
            f"Routed to {department}."
        )