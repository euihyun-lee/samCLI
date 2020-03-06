class Title:
    def __init__(self,
                 name: str,
                 level: int):

        self.name = name
        self.level = level


class HanTitle(Title):
    TITLES = ["Emperor", "King", "Duke"]
    def __init__(self, level: int):
        assert 0 <= level < len(self.TITLES)

        Title.__init__(self, self.TITLES[level], level)
        
