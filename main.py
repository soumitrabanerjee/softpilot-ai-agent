# main.py
from agents.main_agent import MainAgent
from app.cli import run_cli


def load_system_prompt() -> str:
    """Loads the system prompt from the prompts directory."""
    try:
        with open("prompts/system_prompt.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Warning: prompts/system_prompt.txt not found. Using a default prompt.")
        return "You are a helpful AI agent."


if __name__ == "__main__":
    # 1. Load the master prompt for the agent
    system_prompt = load_system_prompt()

    # 2. Initialize the agent
    agent = MainAgent(system_prompt=system_prompt)

    # 3. Run the command-line interface
    run_cli(agent)
