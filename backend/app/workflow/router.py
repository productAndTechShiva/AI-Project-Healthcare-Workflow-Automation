"""
Queue assignment logic.
"""


class QueueRouter:
    """
    Converts department into queue.
    """

    @staticmethod
    def get_queue_name(department: str) -> str:

        return f"{department} Queue"