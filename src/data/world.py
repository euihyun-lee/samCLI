import networkx as nx
import matplotlib.pyplot as plt
from typing import List

from .location import City, Road
from .value import Color

class World(nx.Graph):
    def __init__(self):
        super().__init__()
        self.city_list = []
        self.road_list = []

    def add_city(self, city: City):
        self.city_list.append(city)
        self.add_node(city)

    def add_cities_from_csv(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                city_id, name, size, x, y, city_type = line.strip().split(',')
                city = City(city_id, name, int(size), (int(x), int(y)), int(city_type))
                self.add_city(city)
        self.city_list.sort(key=lambda x: x.id)

    def add_road(self, road: Road):
        self.road_list.append(road)
        self.add_edge(road.city_from, road.city_to, weight=road.distance)

    def add_roads_from_csv(self, filename: str):
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                road_id, city_from, city_to = map(int, line.strip().split(','))
                city_from = self.city_list[city_from]
                city_to = self.city_list[city_to]
                road = Road(road_id, city_from, city_to)
                self.add_road(road)
        self.road_list.sort(key=lambda x: x.id)

    def draw_world(self):
        city_pos_list = {city: city.pos for city in self.city_list}
        city_size_list = [(city.size+1)*100 for city in self.city_list]
        city_color_list = [city.owner.force.color if not city.owner is None else Color.WHITE for city in self.city_list]
        nx.draw_networkx_edges(self, city_pos_list)
        nx.draw_networkx_nodes(self, city_pos_list, node_size=city_size_list, node_color=city_color_list)
        plt.show()
