# Agent Instructions

## Documents

- `_docs/process.md` - how work is organized

## Commands

- `cd backend && uv sync` - install backend dependencies
- `cd backend && uv run pytest` - run the whole backend test suite
- `cd backend && uv run pytest tests/test_health.py` - run one backend test file
- `cd frontend && npm install` - install frontend dependencies
- `cd frontend && npm test` - run the whole frontend test suite
- `cd frontend && npm test -- src/App.test.tsx` - run one frontend test file
- `cd frontend && npm run build` - type-check and build the frontend

## Rules

- This project has both a Python/FastAPI backend and a Node/Vite frontend. Do not assume there is only one stack.
- Dependencies are added in `backend/pyproject.toml` for the backend or `frontend/package.json` for the frontend. Do not add one without asking.
- Use `_docs/architecture.md` as the source of truth for the selected stack, pinned service versions, and local-first Docker Compose direction.
- Keep the project local-first. Do not add cloud infrastructure, managed services, or external identity providers unless the project direction changes.
- Use Conventional Commits format for commit messages (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`), matching the convention already used in this repository's history.
