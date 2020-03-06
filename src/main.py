from data.world import World
from data.location import City

if __name__ == "__main__":
    world = World()
    world.add_cities_from_csv('../data/cities.txt')
    world.add_roads_from_csv('../data/roads.txt')
    world.draw_world()
