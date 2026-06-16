"""
Temporary endpoint for testing workflow analysis.
"""

from fastapi import APIRouter

from app.ai.analyzer import WorkflowAnalyzer

router = APIRouter()


@router.get("/test-analysis")
def test_analysis():
    """
    Analyze a sample request.
    """

    analyzer = WorkflowAnalyzer()

    result = analyzer.analyze(
        "I have severe chest pain and difficulty breathing."
    )

    return result