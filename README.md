# 🧠 Multi-Agent Task Automation with Langchain & CrewAI

This project explores how autonomous agents can work together to perform intelligent backend tasks using **Langchain** and **CrewAI**. It simulates a simple multi-agent system designed to research a topic, summarize findings, and make decisions—mirroring real-world Agentic AI workflows.

---

## 🚀 Overview

This system demonstrates:

- 🤖 **ResearchAgent** – Gathers content based on a topic
- 📝 **SummarizerAgent** – Condenses and summarizes research
- 📊 **DecisionAgent** – Analyzes and makes a recommendation
- 🧭 **Coordinator** – Orchestrates and runs the multi-agent pipeline

Agents are modular, each with a single responsibility. The coordinator handles agent orchestration and task handoff.

---

## ⚙️ Tech Stack

- **Python 3.10**
- **Langchain** – Language model framework
- **CrewAI** – Agent orchestration
- **FastAPI** *(optional for future UI)*
- **Docker** – For deployment
---

## 📦 Installation

```bash
git clone https://github.com/gauthamisreenivas/multi-agent-ai-langchain-crewai.git
cd multi-agent-ai-langchain-crewai
pip install -r requirements.txt
python main.py
