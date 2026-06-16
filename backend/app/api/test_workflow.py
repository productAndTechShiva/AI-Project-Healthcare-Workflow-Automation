"""
Temporary endpoint for testing
complete workflow automation.
"""

from fastapi import APIRouter

from app.ai.analyzer import WorkflowAnalyzer
from app.workflow.ticket_generator import TicketGenerator
from app.workflow.router import QueueRouter
from app.workflow.timeline_generator import TimelineGenerator

router = APIRouter()


@router.get("/test-workflow")
def test_workflow():

    analyzer = WorkflowAnalyzer()

    analysis = analyzer.analyze(
        "I have severe chest pain and difficulty breathing."
    )

    ticket_id = TicketGenerator.generate_ticket_id()

    summary = TicketGenerator.generate_summary(
        request_type=analysis["request_type"],
        priority=analysis["priority"],
        department=analysis["department"]
    )

    queue_name = QueueRouter.get_queue_name(
        analysis["department"]
    )

    timeline = TimelineGenerator.generate(
        queue_name
    )

    analysis["ticket_id"] = ticket_id
    analysis["ticket_summary"] = summary
    analysis["queue_name"] = queue_name
    analysis["timeline"] = timeline

    return analysis