# Development stack: React + Tailwind (frontend) + FastAPI (backend) + Postgres (docker-compose)

## How to use

1. Install Docker and Docker Compose.
2. From the project root (where docker-compose.yml is), run:
   ```bash
   docker compose up --build
   ```
3. Open the apps:
   - Frontend (Vite dev server): http://localhost:3000
   - Backend (FastAPI): http://localhost:8000/docs
   - Postgres: localhost:5432

Notes:
- Frontend runs in development mode (hot reload) inside a container.
- Backend runs with `uvicorn --reload` for fast development.
- Edit the files in `frontend/` and `backend/` on your host; changes will hot-reload.
