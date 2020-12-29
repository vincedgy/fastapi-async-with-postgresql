import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lib.db_utils import database
from lib.models import Note, NoteIn
from lib.schema import notes

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
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/notes", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert()
    values = {"text": note.text, "completed": note.completed}
    last_record_id = await database.execute(query=query, values=values)
    return {**note.dict(), "id": last_record_id}


@app.get("/notes")
async def get_notes():
    query = notes.select()
    rows = await database.fetch_all(query=query)
    return rows


# Run the Server
if __name__ == '__main__':
    uvicorn.run(app="main:app", port=5000, host='0.0.0.0', reload=True, workers=2, access_log=True)
