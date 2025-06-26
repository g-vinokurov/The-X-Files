
from State.Models.Project import Project
from State.Models.Report import Report
from State.Models.Level import Level
from State.Models.Type import Type
from State.Models.Doc import Doc, P, Pre, Img, File

p = Project(path='D:\\__CHERDAK__\\X-Files\\Reports')
p.reports.append(
    Report(
        id='R-125', 
        title='Malware',
        event='PSUTI CTF'
    )
)
print(p)
