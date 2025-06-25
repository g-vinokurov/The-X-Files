
class File:
    def __init__(self, src: str, title: str):
        self._src = src
        self._title = title
    
    @property
    def src(self):
        return self._src
    
    @property
    def title(self):
        return self._title


class Img:
    def __init__(self, src: str, alt: str):
        self._src = src
        self._alt = alt
    
    @property
    def src(self):
        return self._src
    
    @property
    def alt(self):
        return self._alt


class P:
    def __init__(self, text: str):
        self._text = text
    
    @property
    def text(self):
        return self._text


class Pre:
    def __init__(self, text: str):
        self._text = text
    
    @property
    def text(self):
        return self._text


Document = tuple[P | Pre | Img | File]
