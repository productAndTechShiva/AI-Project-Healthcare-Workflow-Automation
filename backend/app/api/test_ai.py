"""
Temporary AI test endpoint.

Used to verify communication
between FastAPI and Ollama.
"""

from fastapi import APIRouter

from app.ai.ollama_client import OllamaClient

router = APIRouter()


@router.get("/test-ai")
def test_ai():
    """
    Simple endpoint for testing Ollama.
    """

    client = OllamaClient()

    prompt = """
    Answer in one sentence.

    What is healthcare workflow automation?
    """

    response = client.generate(prompt)

    return {
        "response": response
    }