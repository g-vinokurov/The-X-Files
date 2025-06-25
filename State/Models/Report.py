
import datetime

from State.Models.Level import Level
from State.Models.Type import Type
from State.Models.Items import Document


class Report:
    def __init__(self, dir: str, id: str, title: str):
        self._dir = dir
        self._id = id
        self._title = title

        self._type : Type | None = None
        self._src : str | None = None
        self._date : datetime.date | None = None
        self._lvl : Level | None = None

        self._tags : tuple[str] = ()

        self._task : Document | None = None
        self._solution : Document | None = None
    
    @property
    def dir(self):
        return self._dir
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
