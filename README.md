# AI Agent Project

A small Python project for experimenting with LLM-based agents, tool calling and basic project-file interaction.

The goal of this project was to understand how an AI agent can use predefined functions to inspect, read, modify and run files inside a project folder. It is not meant to be a production-ready coding agent, but a learning project for API integration, tool execution and structured Python development.

## What it does

The agent can work with a limited set of tools, such as:

- listing files and directories
- reading file contents
- writing or modifying files
- running Python files
- using function calls to decide which tool should be executed

The project is built around the idea that the language model should not directly access the system. Instead, it can only call specific Python functions that are defined in the project.

## Why I built it

I built this project to better understand how AI coding agents work on a basic level.

While using tools like ChatGPT or Codex, I wanted to learn what happens behind the scenes: how prompts are structured, how function calls are handled, how tool outputs are passed back to the model, and how a project can be organized so that this process stays understandable.

## Tech stack

- Python 3
- Google GenAI / Gemini API
- `uv`
- `pyproject.toml`
- `.env` configuration
- `pytest`
- Git / GitHub

## Main concepts

This project helped me practice:

- API integration with an LLM provider
- function calling / tool calling
- separating configuration from project logic
- reading and writing files safely through controlled functions
- basic test structure with `pytest`
- organizing a Python project across multiple files

## Project structure

The project is organized into separate modules for configuration, function execution and agent logic. The exact structure may change while I continue improving the project.

```text
agent_project/
├── main.py
├── config/
├── functions/
├── tests/
├── pyproject.toml
└── README.md
