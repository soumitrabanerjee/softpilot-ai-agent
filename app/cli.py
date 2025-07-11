# app/cli.py
from agents.main_agent import MainAgent


def run_cli(agent: MainAgent):
    """Runs a command-line interface to interact with the agent."""
    print("AI Agent CLI is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting. Goodbye!")
            break
        if not user_input:
            continue

        agent.run(user_input)
