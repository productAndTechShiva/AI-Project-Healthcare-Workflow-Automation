"""
Response models.

These models define the structured output
returned by the workflow automation system.
"""

from typing import List, Optional

from pydantic import BaseModel


class ExtractedEntities(BaseModel):
    """
    Information extracted from the request.
    """

    symptoms: List[str] = []

    medications: List[str] = []

    specialty: Optional[str] = None

    issue_type: Optional[str] = None


class WorkflowResponse(BaseModel):
    """
    Final workflow response returned to frontend.
    """

    request_type: str

    entities: ExtractedEntities

    priority: str

    decision: str

    department: str

    queue_name: str

    ticket_id: str

    ticket_summary: str

    explanation: str

    timeline: List[str]