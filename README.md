# trustpartners-assistant

A production-ready **RAG-based AI assistant** built for the Trust Partners website to provide reliable, policy-grounded guidance.

This branch has been created to **migrate from OpenAI Chat Completions to the OpenAI Agent SDK**, enabling:

- Agent-based reasoning rather than openai chat completion
- Structured tool usage
- Better orchestration and extensibility for future automation

---

## 🚀 Tech Stack

- Python (FastAPI)
- OpenAI **Agent SDK**
- RAG (Retrieval-Augmented Generation)
- Vector-based document retrieval
- Lightweight HTML chatbot widget

---

## 🧠 Architecture Overview

- Uses the **Agent SDK** for conversational orchestration instead of raw chat completions
- The agent is responsible for:
  - Intent understanding
  - Context retrieval (RAG)
  - Policy-safe response generation
- Backend exposes a REST API consumed by a standalone chatbot widget

---

## Virtual Enviroment

`uv venv`

## Activate Virtual Enviroment

`source .venv/Scripts/activate`

## Install Dependencies

`uv pip install .`

## Run backend

`uv run uvicorn app.main:app --reload --port 8002`

## Run chatbot widget

`open chat-widget.html`
