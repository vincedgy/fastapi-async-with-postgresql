from pydantic import BaseModel


class NoteIn(BaseModel):
    """The representation of a Note that needs to be saved into the database"""
    text: str
    completed: bool

    def __repr__(self):
        print(f"<class NodeIn :[text={self.text}, completed={self.completed}]>")


class Note(BaseModel):
    """The representation of a Note that needs to be send back to requests from the database"""
    id: int
    text: str
    completed: bool
