"""
Production workflow endpoint.

This endpoint will be used by
the React frontend.
"""

from fastapi import APIRouter

from app.models.request_models import WorkflowRequest
from app.models.response_models import (
    WorkflowResponse,
    ExtractedEntities
)

from app.ai.analyzer import WorkflowAnalyzer

from app.workflow.ticket_generator import TicketGenerator
from app.workflow.router import QueueRouter
from app.workflow.timeline_generator import TimelineGenerator


router = APIRouter(
    prefix="/api/workflow",
    tags=["Workflow"]
)


@router.post(
    "/analyze",
    response_model=WorkflowResponse
)
def analyze_workflow(
    request: WorkflowRequest
):
    """
    Analyze healthcare request
    and execute workflow automation.
    """

    analyzer = WorkflowAnalyzer()

    # ----------------------------------
    # AI Analysis
    # ----------------------------------

    analysis = analyzer.analyze(
        request.message
    )

    # ----------------------------------
    # Ticket Generation
    # ----------------------------------

    ticket_id = (
        TicketGenerator.generate_ticket_id()
    )

    ticket_summary = (
        TicketGenerator.generate_summary(
            request_type=analysis["request_type"],
            priority=analysis["priority"],
            department=analysis["department"]
        )
    )

    # ----------------------------------
    # Queue Assignment
    # ----------------------------------

    queue_name = (
        QueueRouter.get_queue_name(
            analysis["department"]
        )
    )

    # ----------------------------------
    # Timeline
    # ----------------------------------

    timeline = (
        TimelineGenerator.generate(
            queue_name
        )
    )

    # ----------------------------------
    # Response
    # ----------------------------------

    return WorkflowResponse(
        request_type=analysis["request_type"],

        entities=ExtractedEntities(
            symptoms=analysis["entities"].get("symptoms", []),
            medications=analysis["entities"].get("medications", []),
            specialty=analysis["entities"].get("specialty"),
            issue_type=analysis["entities"].get("issue_type")
        ),

        priority=analysis["priority"],

        decision=analysis["decision"],

        department=analysis["department"],

        queue_name=queue_name,

        ticket_id=ticket_id,

        ticket_summary=ticket_summary,

        explanation=analysis["explanation"],

        timeline=timeline
    )