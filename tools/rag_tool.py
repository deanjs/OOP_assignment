import os
from huggingface_hub import InferenceClient
from tools.base_tool import BaseTool
from exceptions import ToolException


class RAGTool(BaseTool):
    """Retrieves relevant documents using HuggingFace Inference API."""

    def __init__(self):
        super().__init__(
            name="RAGTool",
            description="Retrieves relevant information using HuggingFace Inference API"
        )
        self.api_token = os.getenv("HF_TOKEN")
        self.client = InferenceClient(
            provider="novita",
            api_key=self.api_token
        )

    def run(self, query: str) -> str:
        if not self.api_token:
            raise ToolException("RAGTool", "HF_TOKEN is not set")

        try:
            completion = self.client.chat.completions.create(
                model="meta-llama/llama-3.1-8b-instruct",
                messages=[{"role": "user", "content": query}],
                max_tokens=200
            )
            return completion.choices[0].message.content

        except Exception as e:
            raise ToolException("RAGTool", f"API request failed: {str(e)}")