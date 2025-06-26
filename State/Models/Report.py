
import datetime
import pydantic

from State.Models.Level import Level
from State.Models.Type import Type
from State.Models.Doc import Doc


class Report(pydantic.BaseModel):
    id: str
    title: str
    type: Type = Type.Jeopardy
    event: str = 'CTF'
    date: datetime.date | None = None
    lvl: Level = Level.Baby
    tags: list[str] = []
    task: Doc = Doc()
    solution: Doc = Doc()
