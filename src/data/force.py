from .title import Title
from .person import Person

class Force:
    def __init__(self,
                 name: str,
                 title: Title,
                 owner: Person,
                 color: str):

        self.name = name
        self.title = title
        self.owner = owner
        self.color = color

