
from project.space_station import SpaceStation

station = SpaceStation()
print(station.add_astronaut("Biologist", "Ridley"))
print(station.add_astronaut("Geodesist", "Marko"))
# print(station.add_astronaut("Meteorologist", "Mincho"))
# print(station.add_astronaut("Meteorologist", "Doncho"))
# print(station.add_astronaut("Meteorologist", "Gencho"))
print(station.add_astronaut("Meteorologist", "Niki"))
print(station.add_planet("Jupiter", "helium", "gold", "silver", "magnesium", "aluminum", "calcium", "potassium"))
print(station.add_planet("Mars", "silicon", "oxygen", "iron"))
print(station.send_on_mission("Jupiter"))
print(station.report())
print(station.send_on_mission("Mars"))
print(station.report())
