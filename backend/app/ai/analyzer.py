"""
Workflow Analyzer.

Responsible for:

- Classification
- Information Extraction
- Priority Assessment
- Decision Making
- Routing Recommendation
"""

import json

from app.ai.ollama_client import OllamaClient
from app.ai.prompts import WORKFLOW_ANALYSIS_PROMPT
from app.ai.output_validator import OutputValidator


class WorkflowAnalyzer:
    """
    Main AI analysis engine.
    """

    def __init__(self):
        self.client = OllamaClient()

    def analyze(self, user_request: str) -> dict:
        """
        Analyze healthcare request.
        """

        prompt = WORKFLOW_ANALYSIS_PROMPT.format(
            user_request=user_request
        )

        response = self.client.generate(prompt)

        # ----------------------------------
        # Attempt 1:
        # Direct JSON parsing
        # ----------------------------------

        try:

            result = json.loads(response)

            result = OutputValidator.validate(
                result
            )

            return result

        except json.JSONDecodeError:

            pass

        # ----------------------------------
        # Attempt 2:
        # Extract JSON block
        # ----------------------------------

        try:

            start = response.find("{")
            end = response.rfind("}")

            if start != -1 and end != -1:

                json_text = response[
                    start:end + 1
                ]

                result = json.loads(
                    json_text
                )

                result = OutputValidator.validate(
                    result
                )

                return result

        except Exception:

            pass

        # ----------------------------------
        # Attempt 3:
        # Safe fallback response
        # ----------------------------------

        fallback_result = {
            "request_type": "General Inquiry",
            "entities": {
                "symptoms": [],
                "medications": [],
                "specialty": None,
                "issue_type": None
            },
            "priority": "Medium",
            "decision": "Manual review required",
            "department": "General Support",
            "explanation": (
                "AI model returned an invalid "
                "response. Request routed "
                "for manual review."
            )
        }

        return OutputValidator.validate(
            fallback_result
        )