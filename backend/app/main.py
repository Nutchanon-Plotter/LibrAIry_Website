from fastapi import FastAPI
import os
from databases import Database
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql://appuser:apppassword@db:5432/appdb')

settings = Settings()

app = FastAPI(title='Backend API')

db = Database(settings.DATABASE_URL)

@app.on_event('startup')
async def startup():
    await db.connect()

@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()

@app.get('/api/health')
async def health():
    # simple DB verification (non-critical)
    try:
        row = await db.fetch_one('SELECT 1 AS ok')
        return {'status': 'ok', 'db': bool(row)}
    except Exception as e:
        return {'status': 'ok', 'db': False, 'error': str(e)}
