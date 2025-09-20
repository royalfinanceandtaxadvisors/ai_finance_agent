# Root wrapper: executes the Streamlit app that lives in a subfolder
import os, runpy
script_path = os.path.join(
    os.path.dirname(__file__),
    "advanced_ai_agents", "multi_agent_apps", "ai_financial_coach_agent",
    "ai_financial_coach_agent.py"
)
runpy.run_path(script_path, run_name="__main__")

