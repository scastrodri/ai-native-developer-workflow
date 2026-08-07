# Weekly Team Feedback Tool

Local-first MVP for collecting weekly team feedback and running retrospectives.

## Task 1 test commands

Run the backend test suite:

```powershell
cd backend
uv run pytest
```

Run the frontend test suite:

```powershell
cd frontend
npm test
```

## Docker Compose commands

Build and start the empty backend and frontend services:

```powershell
docker compose up --build
```

Verify the backend health endpoint while Compose is running:

```powershell
Invoke-RestMethod http://localhost:8000/health
```

Verify the frontend app by opening:

```text
http://localhost:5173
```

Stop the Compose services:

```powershell
docker compose down
```
