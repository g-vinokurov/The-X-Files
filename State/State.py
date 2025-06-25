
from State.Models.Project import Project


class State:
    def __init__(self):
        self._project : Project | None = None

    @property
    def project(self):
        return self._project
    
    @project.setter
    def project(self, project: Project | None):
        self._project = project
