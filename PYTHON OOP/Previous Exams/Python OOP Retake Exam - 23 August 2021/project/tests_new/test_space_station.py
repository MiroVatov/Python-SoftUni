import pytest

from project.planet.planet import Planet
from project.space_station import SpaceStation


def test__init__():
    space_station = SpaceStation()
    assert space_station.astronauts_limit == 5
    assert space_station.eligible_astronauts == []
    assert space_station.completed_missions == 0
    assert space_station.not_completed_missions == 0


def test_method_add_astronaut_already_added():
    space_station = SpaceStation()
    space_station.add_astronaut("Biologist", "John")
    assert space_station.add_astronaut("Biologist", "John") == "John is already added."


def test_method_add_astronaut_type_not_correct():
    space_station = SpaceStation()
    with pytest.raises(Exception) as exc:
        space_station.add_astronaut("Biolog", "John")

    assert exc.type == Exception
    message = str(exc.value)
    assert message == "Astronaut type is not valid!"


def test_method_add_astronaut_successfully_added():
    space_station = SpaceStation()
    assert space_station.add_astronaut("Biologist", "John") == "Successfully added Biologist: John."


def test_method_add_planet_already_added():
    space_station = SpaceStation()
    space_station.add_planet("Mars", "oxygen, stone")
    assert space_station.add_planet("Mars", "") == "Mars is already added."


def test_method_add_planet_successful():
    space_station = SpaceStation()
    assert space_station.add_planet("Mars", "oxygen, stone") == "Successfully added Planet: Mars."


def test_retire_astronaut_doesnt_exist():
    space_station = SpaceStation()
    assert space_station.retire_astronaut("Joh"), "Astronaut Jon doesn't exists!"


def test_method_retire_astronaut_success():
    space_station = SpaceStation()
    space_station.add_astronaut("Biologist", "John")
    assert space_station.retire_astronaut("John"), "Astronaut John was retired!"


def test_method_recharge_oxygen():
    space_station = SpaceStation()
    space_station.add_astronaut("Biologist", "John")
    space_station.add_astronaut("Geodesist", "Ivan")
    space_station.add_astronaut("Meteorologist", "Svetli")
    space_station.recharge_oxygen()

    for astro in space_station.astronaut_repository.astronauts:
        if astro.__class__.__name__ == "Biologist":
            assert astro.oxygen == 80
        elif astro.__class__.__name__ == "Geodesist":
            assert astro.oxygen == 60
        elif astro.__class__.__name__ == "Meteorologist":
            assert astro.oxygen == 100


def test_method_send_on_a_mission_planet_not_found():
    space_station = SpaceStation()
    with pytest.raises(Exception) as exc:
        space_station.send_on_mission("Mars")

    assert exc.type == Exception
    message = str(exc.value)
    assert message == "Invalid planet name!"


def test_method_send_on_a_mission_no_eligible_astronauts():
    space_station = SpaceStation()
    space_station.add_astronaut("Meteorologist", "Svetli")
    space_station.add_planet("Mars", "stone")
    astronaut = space_station.astronaut_repository.find_by_name("Svetli")
    astronaut.breathe()
    astronaut.breathe()
    astronaut.breathe()
    astronaut.breathe()

    with pytest.raises(Exception) as exc:
        space_station.send_on_mission("Mars")

    assert exc.type == Exception
    message = str(exc.value)
    assert message == "You need at least one astronaut to explore the planet!"


def test_method_send_on_a_mission_not_successful():
    space_station = SpaceStation()
    space_station.add_astronaut("Meteorologist", "Svetli")

    space_station.add_planet("Mars", "stone, water, oxygen, fire, wall, salt, coconut")
    assert space_station.send_on_mission("Mars"), "Mission is not completed."
    assert space_station.not_completed_missions == 1
    assert space_station.planet_repository.planets == [space_station.planet_repository.planets[0]]


def test_method_send_on_a_mission_successful():
    space_station = SpaceStation()
    space_station.add_astronaut("Biologist", "Ivan")
    space_station.add_astronaut("Meteorologist", "Svetli")
    space_station.add_astronaut("Geodesist", "Yonko")
    space_station.add_planet("Mars", "stone, water, oxygen, fire, wall, salt, coconut, whiskey, aroma")
    assert space_station.send_on_mission(
        "Mars"), "Planet: Mars was explored. 2 astronauts participated in collecting items."
    data = "1 successful missions!" + "\n"
    data += "0 missions were not completed!" + "\n"
    data += "Astronauts' info:" + '\n'
    data += "Name: Ivan" + '\n'
    data += "Oxygen: 0" + '\n'
    data += "Backpack items: aroma, whiskey, coconut, salt, wall, fire" + "\n"
    data += "Name: Svetli" + "\n"
    data += "Oxygen: 55" + "\n"
    data += "Backpack items: oxygen, water, stone" + "\n"
    assert space_station.report() == data
