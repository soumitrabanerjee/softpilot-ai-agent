# core/llm_service.py
import abc
import openai
import google.generativeai as genai
from config import LLM_PROVIDER, OPENAI_API_KEY, GOOGLE_API_KEY, DEFAULT_MODEL

class BaseLLMService(abc.ABC):
    """Abstract base class for all LLM services."""
    def __init__(self, api_key: str, model: str):
        if not api_key:
            raise ValueError(f"API key for {self.__class__.__name__} is not set in .env file.")
        self.model = model
        self._configure_client(api_key)

    @abc.abstractmethod
    def _configure_client(self, api_key: str):
        """Configures the API client."""
        pass

    @abc.abstractmethod
    def get_completion(self, system_prompt: str, user_prompt: str) -> str:
        """Gets a completion from the language model."""
        pass

class OpenAILLMService(BaseLLMService):
    """LLM Service implementation for OpenAI."""
    def _configure_client(self, api_key: str):
        openai.api_key = api_key

    def get_completion(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred while calling the OpenAI API: {e}")
            return "Error: Could not get a response from the model."

class GoogleLLMService(BaseLLMService):
    """LLM Service implementation for Google Gemini."""
    def _configure_client(self, api_key: str):
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model_name=self.model)

    def get_completion(self, system_prompt: str, user_prompt: str) -> str:
        # Gemini combines the system prompt with the first user message.
        full_prompt = f"{system_prompt}\n\n---\n\nUser Task: {user_prompt}"
        try:
            response = self.client.generate_content(full_prompt)
            # A safety check for cases where the model might return no content
            return response.text.strip() if response.text else "The model returned an empty response."
        except Exception as e:
            print(f"An error occurred while calling the Google Gemini API: {e}")
            return "Error: Could not get a response from the model."

# --- Factory Function ---
def get_llm_service() -> BaseLLMService:
    """
    Factory function to get the configured LLM service instance.
    This is the only function that needs to be called from outside this module.
    """
    provider = LLM_PROVIDER.lower()
    if provider == "openai":
        print("Using OpenAI service.")
        return OpenAILLMService(api_key=OPENAI_API_KEY, model=DEFAULT_MODEL)
    elif provider == "google":
        print("Using Google Gemini service.")
        return GoogleLLMService(api_key=GOOGLE_API_KEY, model=DEFAULT_MODEL)
    else:
        raise ValueError(f"Unsupported LLM provider configured: {LLM_PROVIDER}")

# Create a single, shared instance of the service to be used by the agent
llm_service = get_llm_service()