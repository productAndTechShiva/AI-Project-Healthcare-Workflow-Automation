"""
Request models.

These models define what data the frontend sends
to the backend.
"""

from pydantic import BaseModel


class WorkflowRequest(BaseModel):
    """
    User healthcare request.

    Example:
    {
        "message": "I have severe chest pain and difficulty breathing."
    }
    """

    message: str