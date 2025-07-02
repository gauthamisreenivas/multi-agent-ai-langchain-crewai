from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.decision_agent import DecisionAgent

def run_agents():
    print("🔍 Starting multi-agent workflow...")

    data = ResearchAgent().run()
    summary = SummarizerAgent().run(data)
    decision = DecisionAgent().run(summary)

    print("\n✅ Final Decision:")
    print(decision)
