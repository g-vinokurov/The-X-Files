
import pydantic


class P(pydantic.BaseModel):
    text: str


class Pre(pydantic.BaseModel):
    text: str


class Img(pydantic.BaseModel):
    path: str
    title: str = ''


class File(pydantic.BaseModel):
    path: str
    title: str


class Doc(pydantic.BaseModel):
    items: list[P | Pre | Img | File] = []
