import openai
import requests
import anthropic

from persistence import get_api_key

class AIClient:
    def __init__(self, api_type: str, max_tokens: int):
        self.api_type = api_type.lower()
        self.api_key = get_api_key(self.api_type)
        self.max_tokens = max_tokens

    def generate_commit_message(self, diff: str, prompt: str) -> str:
        """
        Generate commit message using the selected AI API.
        """
        if self.api_type == "gpt":
            return self._use_gpt(diff, prompt)
        elif self.api_type == "claude":
            return self._use_claude(diff, prompt)
        else:
            raise ValueError("Unsupported API type. Use 'gpt' or 'claude'.")

    def _use_gpt(self, diff: str, prompt: str) -> str:
        """
        Generate commit message using GPT (OpenAI API).
        """
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{prompt}\n\n{diff}"}
            ],
            max_tokens=self.max_tokens,
        )
        return response.choices[0].message.content

    def _use_claude(self, diff: str, prompt: str) -> str:
        """
        Generate commit message using Claude API.
        """
        client = anthropic.Anthropic(api_key=self.api_key)
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=self.max_tokens,
            messages=[
                {"role": "user", "content": f"{prompt}\n\n{diff}"}
            ]
        )
        return message.content[0].text