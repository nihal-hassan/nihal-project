# 🧠 Agents Module

**Module:** Agents Module  
**Author:** Nihal Hassan  
**Version:** 1.0.0  
**Stack:** Python 3.10+ · LangGraph · HuggingFace Transformers · Qwen 2.5  

---

## 📑 Table of Contents
- Overview  
- Architecture  
- Module Structure  
- Getting Started  
- How to Run  
- Execution Flow  
- API Reference  
- Prompt Design Strategy  
- Configuration  
- Integration Guide  
- Constraints & Contracts  
- Dependencies  
- Troubleshooting  
- Contact  

---

## 📌 Overview
The **Agents Module** is the reasoning layer of the Multi-Agent Debate System. It defines three intelligent agents that simulate a structured debate process using a Large Language Model (LLM).

### Agents:
- **Pro Agent** — Generates arguments supporting the topic  
- **Con Agent** — Generates counterarguments opposing the topic  
- **Judge Agent** — Evaluates the debate and declares a winner  

The module operates on a shared state (`DebateState`) and integrates with the Core Engine for workflow execution.

---

## 🏗 Architecture

[ Start ]
    │
    ▼
[ Pro Agent ]
    │
    ▼
[ Con Agent ]
    │
    ▼
[ Check Rounds ]
    │
 ┌──┴──────────────┐
 │                 │
 ▼                 ▼
Repeat         [ Judge Agent ]
(Pro → Con)         │
                   ▼
                 [ End ]




### Flow:
- Pro Agent generates supporting argument  
- Con Agent generates counterargument and increments round  
- Loop continues until `max_rounds`  
- Judge Agent evaluates and ends debate  

---

## 📂 Module Structure
agents/
├── agents.py # Pro and Con agents
├── judge.py # Judge agent
└── README.md


---

## ⚙️ agents.py — Debate Agents

### `pro_agent(state) → dict`
Generates arguments supporting the topic.

```python
{"history": ["Pro: <argument>"]}

con_agent(state) → dict

Generates counterarguments and increments round count.

{
  "history": ["Con: <argument>"],
  "round_count": state["round_count"] + 1
}

⚖️ judge.py — Judge Agent
judge_agent(state) → dict

Evaluates debate and decides winner.
{
  "winner": "Pro" | "Con" | "Unknown",
  "judge_reason": "..."
}

Getting Started
Prerequisites
    Python 3.10+
    Core Engine files (memory.py, qwen_utils.py, graph.py)
    Internet connection (first-time model download)
    Installation
pip install langgraph langchain-core transformers torch accelerate

How to Run
Step 1: Project Structure
project/
├── memory.py
├── qwen_utils.py
├── graph.py
├── agents.py
├── judge.py
├── main.py

Step 2: Create main.py
from graph import build_debate_graph

def main():
    app = build_debate_graph()

    initial_state = {
        "topic": "AI is good for society",
        "max_rounds": 2,
        "round_count": 0,
        "history": [],
        "winner": "",
        "judge_reason": ""
    }

    print("Starting Debate...\n")

    for step, output in enumerate(app.stream(initial_state), 1):
        print(f"Step {step}")
        print(output)
        print("-" * 40)

if __name__ == "__main__":
    main()


Step 3: Run
python main.py

Step 4: Output
Pro and Con arguments
Final Judge decision
{'history': ['Pro: AI improves efficiency...']}
{'history': ['Con: AI causes job loss...'], 'round_count': 1}
...
{'winner': 'Pro', 'judge_reason': 'Stronger logical arguments'}

Execution Flow

| Step  | Agent  | Action             |
| ----- | ------ | ------------------ |
| 1     | Pro    | Generates argument |
| 2     | Con    | Counters argument  |
| Loop  | Repeat | Until max rounds   |
| Final | Judge  | Declares winner    |

API Reference
pro_agent(state) → Returns Pro argument
con_agent(state) → Returns Con argument + updates round
judge_agent(state) → Returns winner + reasoning

Prompt Design Strategy
Keep arguments concise
Ensure logical reasoning
Maintain role consistency
Avoid repetition
⚙️ Configuration

Modify prompts in:

agents.py
judge.py

Advanced (Core Engine):

Temperature
Max tokens
Model selection

Integration Guide
Required from Core Engine:
DebateState (memory.py)
generate_response() (qwen_utils.py)
build_debate_graph() (graph.py)
Import Example
from agents import pro_agent, con_agent
from judge import judge_agent

Constraints & Contracts
Do NOT change:
    Function signatures
    Return formats
    State fields
📦 Dependencies
    langgraph
    langchain-core
    transformers
    torch
    accelerate
🛠 Troubleshooting
Model not downloading
    Check internet
    Retry execution
Slow performance
    Use GPU
    Reduce rounds
Incorrect output
Verify return format
👨‍💻 Contact

Module Owner: Nihal Hassan
Role: Debate Agents — Argument Generation & Evaluation