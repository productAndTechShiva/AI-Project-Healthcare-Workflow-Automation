"""
Ollama Client

Responsible for communicating with the local Ollama server.

This module will be reused by all AI workflow components.
"""

import requests


class OllamaClient:
    """
    Wrapper around Ollama REST API.
    """

    def __init__(
        self,
        model: str = "llama3.2",
        base_url: str = "http://localhost:11434"
    ):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str) -> str:
        """
        Send prompt to Ollama and return generated text.

        Parameters
        ----------
        prompt : str
            User/system prompt

        Returns
        -------
        str
            Generated response text
        """

        endpoint = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(
                endpoint,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "").strip()

        except requests.exceptions.RequestException as error:
            raise Exception(
                f"Error communicating with Ollama: {str(error)}"
            )