
import pydantic
import typing


class P(pydantic.BaseModel):
    type: typing.Literal['p']
    text: str


class Pre(pydantic.BaseModel):
    type: typing.Literal['pre']
    text: str


class Img(pydantic.BaseModel):
    type: typing.Literal['img']
    path: str
    title: str = ''


class File(pydantic.BaseModel):
    type: typing.Literal['file']
    path: str
    title: str


class Doc(pydantic.BaseModel):
    items: list[P | Pre | Img | File] = []
