from typing import Tuple

class Location:
    def __init__(self,
                 loc_id: int,
                 name: str):
        
        self.id = loc_id
        self.name = name
        self.people = []


class City(Location):
    SIZE = [0, 1, 2, 3] # small, medium, big, huge
    CITY_TYPE = [0] # TBD 
    def __init__(self,
                 city_id: int,
                 name: str,
                 size: int,
                 pos: Tuple[int, int],
                 city_type: int = 0):

        assert size in self.SIZE
        assert city_type in self.CITY_TYPE

        Location.__init__(self, city_id, name)
        self.size = size
        self.pos = pos
        self.x, self.y = pos
        self.city_type = city_type
        self.owner = None
        self.army = 0


class Road(Location):
    def __init__(self,
                 road_id: int,
                 city_from: City,
                 city_to: City,
                 road_type: int = 0,
                 name: str = None):

        Location.__init__(self, road_id, name)
        self.city_from = city_from
        self.city_to = city_to
        self.road_type = road_type
        self.distance = ((city_from.x - city_to.x)**2 + (city_from.y - city_to.y)**2)**.5

