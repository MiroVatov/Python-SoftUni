
from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()  # a new repository created for each space station
        self.astronaut_repository = AstronautRepository()  # a new repository created for each space station
        self.astronauts_limit = 5
        self.eligible_astronauts = []
        self.completed_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        astronaut = None
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, *items: str):
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        planet = Planet(name, *items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            return f"Astronaut {name} doesn't exists!"

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet_found = self.planet_repository.find_by_name(planet_name)

        if planet_found is None:
            raise Exception("Invalid planet name!")

        self.eligible_astronauts = self.check_for_suitable_astronauts()

        if not self.eligible_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        # TODO check the reversed list by attribute
        self.eligible_astronauts.sort(key=lambda a: a.oxygen, reverse=True)

        astronauts_participated = 0
        sorted_astronauts = deque(self.eligible_astronauts)
        planet_items_reversed = deque(planet_found.items)

        while True:
            astronaut = sorted_astronauts.popleft()
            astronauts_participated += 1

            while planet_items_reversed:
                item = planet_items_reversed.pop()
                astronaut.breathe()
                astronaut.backpack.append(item)

                if astronaut.oxygen <= 0:
                    break

            if len(sorted_astronauts) > 0 and len(planet_items_reversed) > 0:
                continue

            elif not planet_items_reversed:
                self.completed_missions += 1
                return f"Planet: {planet_name} was explored. {astronauts_participated} astronauts participated in collecting items."

            elif planet_items_reversed:
                self.not_completed_missions += 1
                return "Mission is not completed."

    def report(self):
        data = f"{self.completed_missions} successful missions!" + '\n'
        data += f"{self.not_completed_missions} missions were not completed!" + '\n'
        data += "Astronauts' info:" + '\n'

        for astronaut in self.astronaut_repository.astronauts:
            data += f"Name: {astronaut.name}" + '\n'
            data += f"Oxygen: {astronaut.oxygen}" + '\n'
            if not astronaut.backpack:
                data += f"Backpack items: none" + '\n'
            else:
                data += f"Backpack items: {', '.join(astronaut.backpack)}" + '\n'
        return data

    def check_for_suitable_astronauts(self):

        # TODO You should pick up to 5 astronauts with the highest amount of oxygen among the ones with oxygen above 30 units.

        astronauts_count = 0

        self.astronaut_repository.astronauts.sort(key=lambda a: a.oxygen, reverse=True)
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30 and astronauts_count < self.astronauts_limit:
                self.eligible_astronauts.append(astronaut)
                astronauts_count += 1

        return self.eligible_astronauts
