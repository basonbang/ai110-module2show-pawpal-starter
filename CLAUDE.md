# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Run tests
pytest
```

## Project Overview

**PawPal+** is a Streamlit-based pet care planning assistant. The backend classes are in `pawpal_system.py`; the next steps are implementing the scheduling logic, writing pytest tests, and wiring the scheduler into `app.py`.

## Architecture

- **`app.py`** — Streamlit UI shell. Collects owner name, pet name, species, and a task list (title, duration, priority) via `st.session_state`. The "Generate schedule" button is a placeholder to be wired into the scheduler.
- **`pawpal_system.py`** — All backend dataclasses: `Pet`, `Task`, `Scheduler`, `Schedule`, `Owner`. The class diagram lives in `diagram.md`.

**Domain model relationships:**
- `Owner` holds a `list[Pet]` and delegates scheduling via `request_schedule(pet, scheduler)`
- `Scheduler` sorts tasks by priority, fits them into `available_minutes`, and returns a `Schedule`
- `Task.apply(pet)` mutates `Pet` state attributes (hunger, energy, health, happiness, each 0–100)
- `Schedule` holds scheduled items `{task, start_time, reason}` and skipped tasks with reasons

All method stubs are in place; logic is not yet implemented.
