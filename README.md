# Hello World Validation Agent

This repository demonstrates a Google ADK agent that uses two Python tool
functions in sequence:

1. `answer_agent` returns exactly `Hello, world!`.
2. `validate_agent` checks that answer.
3. The main agent returns the answer and the validation result.

The agent uses Sysco's SAGE LLM through `SageLlmRegistry` with the
`sage-gemini-2.5-flash` model.

## Project files

- `agent.py` defines the main ADK agent and registers the tools.
- `sub_agent.py` defines `answer_agent()` and `validate_agent(answer)`.
- `requirements.txt` lists the project dependencies.

## Example behavior

The workflow is:

```text
User request
    ↓
answer_agent()       → Hello, world!
    ↓
validate_agent(...)  → VALID
```

The validation function returns `INVALID` if the answer is not exactly
`Hello, world!`.

## Run the agent

Install the dependencies, configure the project environment, and run from
the repository folder:

```powershell
pip install -r requirements.txt
adk web .
```

Alternatively, run it in the terminal:

```powershell
adk run .
```
