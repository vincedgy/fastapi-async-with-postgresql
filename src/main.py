from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from lib.db_utils import database
from lib.models import Note, NoteIn
from lib.schema import notes
from lib.utils import get_logger

logger = get_logger(name='main')

# Defines the API

app = FastAPI(
    title="REST API that serves asyncio Posgresql datas with async Endpoints")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    """Executed on server's startup"""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """Executed on server's shutdown"""
    await database.disconnect()


@app.post("/notes", response_model=Note)
async def create_note(note: NoteIn):
    """Create a note into the database and send back the created record's id"""
    query = notes.insert()
    values = {"text": note.text, "completed": note.completed}
    last_record_id = await database.execute(query=query, values=values)
    return {**note.dict(), "id": last_record_id}


@app.get("/notes/all", response_model=List[Note])
async def get_all_notes():
    """Fetch all notes at once"""
    query = notes.select()
    rows = await database.fetch_all(query=query)
    return rows


@app.get("/notes", response_model=List[Note])
async def get_notes(skip: int = 0, take: int = 20):
    """Fetch notes with pagination"""
    query = notes.select().offset(skip).limit(take)
    rows = await database.fetch_all(query=query)
    return rows


@app.get("/notes/{note_id}", response_model=Note)
async def get_one_note_by_id(note_id: int):
    """Fetch one Note given the note_id"""
    query = notes.select().where(text(f"id={note_id}"))
    row = await database.fetch_one(query=query)
    if row is None:
        logger.info("No record !")
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": f"Request asked for note id: [{note_id}]"}
        )
    return row


# Run the Server
if __name__ == '__main__':
    uvicorn.run(app="main:app", port=5000, host='0.0.0.0', reload=True, workers=2, access_log=True)
