# 🤖 Autonomous AI Agent

An autonomous decision-making engine built with Python, focusing on **Functional Programming** principles and robust **state management**. This agent is designed to navigate complex environments, manage resources, and achieve goals through logical reasoning.

---

## 🚀 Overview

This project marks a significant milestone in my journey toward AI development. Moving away from simple procedural scripts, I implemented an agent that perceives its environment and makes autonomous choices based on a set of predefined rules and functional logic.

### Key Features
* **Autonomous Logic:** Independent decision-making without hard-coded "if-else" spaghetti.
* **Functional Core:** Heavy use of **Pure Functions** and **Immutability** to ensure the agent's behavior is predictable and bug-free.
* **State Machine Architecture:** Efficiently tracks the agent's status, goals, and environmental changes.
* **Recursive Problem Solving:** Leverages recursion to handle complex, nested decision trees.

---

## 🛠 Tech Stack

* **Language:** Python 3.13
* **Paradigm:** Functional Programming (FP) & Object-Oriented Programming (OOP)
* **Environment:** Linux (WSL2)
* **Tools:** `uv` for lightning-fast dependency management, `Git` for version control.

---

## 🧠 Deep Dive: What I Learned

Building this agent in a single day was an intense challenge that solidified several high-level concepts:

1.  **Declarative vs. Imperative:** I learned to focus on *what* the agent should achieve rather than just *how* to loop through commands.
2.  **Side-Effect Management:** By using functional principles, I kept the "brain" of the agent separate from the "actions," making the code much easier to test and scale.
3.  **Data Structures:** Implemented efficient ways to store and retrieve the agent's knowledge base.

---

## ⚙️ Installation & Usage

This project uses `uv` for Python package management.

```bash
# Clone the repository
git clone [https://github.com/DEIN_GITHUB_NAME/ai-agent.git](https://github.com/DEIN_GITHUB_NAME/ai-agent.git)

# Navigate to the directory
cd ai-agent

# Install dependencies and run the agent
uv run main.py
