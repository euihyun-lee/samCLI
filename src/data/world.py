import networkx as nx
import matplotlib.pyplot as plt

class City(object):
    SIZE = [0, 1, 2, 3] # small, medium, big, huge
    CITY_TYPE = [0] # TBD 
    def __init__(self, name, size, pos, city_type=0):
        assert type(name) is str
        assert size in self.SIZE
        assert type(pos) is tuple
        assert len(pos) == 2
        assert type(pos[0]) is int
        assert type(pos[1]) is int
        assert city_type in self.CITY_TYPE

        self.name = name
        self.size = size
        self.pos = pos
        self.x, self.y = pos
        self.city_type = city_type
        self.owner = None
        self.people = []


class Road(object):
    def __init__(self, city_from, city_to, road_type=0, name=None):
        self.city_from = city_from
        self.city_to = city_to
        self.road_type = road_type
        self.name = name
        self.people = []
        self.distance = ((city_from.x - city_to.x)**2 + (city_from.y - city_to.y)**2)**.5

class World(nx.Graph):
    def __init__(self):
        super().__init__()

    def add_city(self, city):
        self.add_node(city)

    def add_cities_from_list(self, city_list):
        self.add_nodes_from(city_list)

    def add_cities_from_csv(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, size, x, y, city_type = line.strip().split(',')
                city = City(name, int(size), (int(x), int(y)), int(city_type))
                self.add_city(city)

    def add_road(self, city_from, city_to):
        dist = ((city_from.x - city_to.x)**2 + (city_from.y - city_to.y)**2)**.5
        self.add_edge(city_from, city_to, weight=dist)

    def add_roads_from_list(self, city_from_to_list):
        for city_from, city_to in city_from_to_list:
            self.add_road(city_from, city_to)

    def add_roads_from_csv(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                city_from_name, city_to_name = line.strip().split(',')
                city_from = self.get_city_by_name(city_from_name)
                city_to = self.get_city_by_name(city_to_name)
                self.add_road(city_from, city_to)


    def get_city_list(self):
        return list(self.nodes)

    def get_city_by_name(self, name):
        city_list = self.get_city_list()
        for city in city_list:
            if city.name == name:
                return city

        # Not found
        return None

    def draw_world(self):
        city_pos_list = {city: city.pos for city in self.get_city_list()}
        city_size_list = [(city.size+1)*100 for city in self.get_city_list()]
        nx.draw_networkx_edges(self, city_pos_list)
        nx.draw_networkx_nodes(self, city_pos_list, node_size=city_size_list)
        plt.show()
