from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply


class Bunker:

    def __init__(self):

        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = [f for f in self.supplies if isinstance(f, FoodSupply)]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water = [w for w in self.supplies if isinstance(w, WaterSupply)]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkiller = [p for p in self.medicine if isinstance(p, Painkiller)]
        if not painkiller:
            raise IndexError("There are no painkillers left!")
        return painkiller

    @property
    def salves(self):
        salve = [s for s in self.medicine if isinstance(s, Salve)]
        if not salve:
            raise IndexError("There are no salves left!")
        return salve

    def add_survivor(self, survivor):
        for srv in self.survivors:
            if srv.name == survivor.name:
                raise ValueError(f"Survivor with name {survivor.name} already exists.")
        # NOTE check if this is the correct way to check for survivor already exists
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            last_medicine_from_certain_type = [medicine for medicine in self.medicine if medicine.__class__.__name__ == medicine_type]
            if last_medicine_from_certain_type:
                medicine_to_remove = last_medicine_from_certain_type.pop()
                medicine_to_remove.apply(survivor)
                for medicine in self.medicine[::-1]:
                    if medicine.__class__.__name__ == medicine_type:
                        self.medicine.remove(medicine)
                return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            last_supply_from_certain_type = [supply for supply in self.supplies if supply.__class__.__name__ == sustenance_type]
            if last_supply_from_certain_type:
                supply_to_remove = last_supply_from_certain_type.pop()
                supply_to_remove.apply(survivor)
                for supply in self.supplies[::-1]:
                    if supply.__class__.__name__ == sustenance_type:
                        self.supplies.remove(supply)
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= (survivor.age * 2)
            if self.food:
                food = self.food.pop()
                food.apply(survivor)
            if self.water:
                water = self.water.pop()
                water.apply(survivor)








