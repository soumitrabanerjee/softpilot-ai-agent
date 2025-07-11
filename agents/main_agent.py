# agents/main_agent.py
from core.llm_service import llm_service # Import the singleton instance

class MainAgent:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        # The llm_service is now initialized and configured in the core module
        print("Agent initialized.")

    def run(self, user_input: str) -> str:
        """
        The main loop for the agent.
        """
        print(f"User Input: {user_input}")

        # The service now handles the specific API call format.
        # This is much cleaner!
        response = llm_service.get_completion(
            system_prompt=self.system_prompt,
            user_prompt=user_input
        )

        print(f"Agent Response: {response}")
        return response