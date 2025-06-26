
import pydantic

from State.Models.Report import Report


class Project(pydantic.BaseModel):
    path: str
    reports: list[Report] = []
