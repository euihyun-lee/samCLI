import networkx as nx
import matplotlib.pyplot as plt
from typing import List

from .location import City
from .value import Color

class World(nx.Graph):
    def __init__(self):
        super().__init__()

    def add_city(self, city: City):
        self.add_node(city)

    def add_cities_from_list(self, city_list: List[City]):
        self.add_nodes_from(city_list)

    def add_cities_from_csv(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                name, size, x, y, city_type = line.strip().split(',')
                city = City(name, int(size), (int(x), int(y)), int(city_type))
                self.add_city(city)

    def add_road(self, city_from: City, city_to: City):
        dist = ((city_from.x - city_to.x)**2 + (city_from.y - city_to.y)**2)**.5
        self.add_edge(city_from, city_to, weight=dist)

    def add_roads_from_list(self, city_from_to_list: List[City]):
        for city_from, city_to in city_from_to_list:
            self.add_road(city_from, city_to)

    def add_roads_from_csv(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                city_from_name, city_to_name = line.strip().split(',')
                city_from = self.get_city_by_name(city_from_name)
                city_to = self.get_city_by_name(city_to_name)
                self.add_road(city_from, city_to)

    def get_city_list(self) -> list:
        return list(self.nodes)

    def get_city_by_name(self, name: str) -> City:
        city_list = self.get_city_list()
        for city in city_list:
            if city.name == name:
                return city

        # Not found
        return None

    def draw_world(self):
        city_list = self.get_city_list()
        city_pos_list = {city: city.pos for city in city_list}
        city_size_list = [(city.size+1)*100 for city in city_list]
        city_color_list = [city.owner.force.color if not city.owner is None else Color.WHITE for city in city_list]
        nx.draw_networkx_edges(self, city_pos_list)
        nx.draw_networkx_nodes(self, city_pos_list, node_size=city_size_list, node_color=city_color_list)
        plt.show()
