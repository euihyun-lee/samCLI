from .location import City, Location
from .force import Force

class Person:
    def __init__(self,
                 name: str,
                 char: int,
                 power: int,
                 intel: int,
                 adm: int,
                 dip: int,
                 rep: int,
                 birth: int,
                 death: int,
                 force: Force = None,
                 city: City = None,
                 location: Location = None):
        # Charisma(char): military power; related to army combat power
        # Power(power): personal power; related to personal battle event
        # Intelligence(intel): personal(military) intelligence; related to stratagem success rate
        # Administration(adm): related to administrative action
        # Diplomatic skill(dip): related to diplomatic action
        # Reputation(rep): related to personal interaction 
        self.name = name
        self.char = char
        self.power = power
        self.intel = intel
        self.adm = adm
        self.dip = dip
        self.rep = rep
        self.birth = birth
        self.death = death
        self.force = force
        self.city = city
        self.location = location    # City or Road
        self.items = []

