from pydantic import BaseModel


class NoteIn(BaseModel):
    """The representation of a Note that needs to be saved into the database"""
    text: str
    completed: bool


class Note(NoteIn):
    """The representation of a Note that needs to be send back to requests from the database"""
    id: int
