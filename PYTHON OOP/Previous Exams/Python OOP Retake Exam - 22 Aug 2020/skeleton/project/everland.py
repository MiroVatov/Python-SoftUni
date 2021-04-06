
class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        rooms_already_in_the_hotel = [room_name for room_name in self.rooms if room.family_name == room_name.family_name]
        if not rooms_already_in_the_hotel:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_rooms_cost = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumptions: {total_rooms_cost:.2f}$."

    def pay(self):
        data = []
        for family in self.rooms:
            family_expenses_per_month = family.expenses + family.room_cost
            if family_expenses_per_month > family.budget:
                data.append(f"{family.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(family)
            else:
                data.append(f"{family.family_name} paid {family.expenses + family.room_cost:.2f}$ and have {family.budget:.2f}$ left.")
                family.budget -= family_expenses_per_month
        return '\n'.join(data)

    def status(self):
        data = f"Total population: {sum([room.members_count for room in self.rooms])}" + '\n'
        for room in self.rooms:
            data += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$" + '\n'
            if room.children:
                counter = 0
                for child in room.children:
                    counter += 1
                    data += f"--- Child {counter} monthly cost: {child.cost * 30:.2f}$" + '\n'
            appliances_cost = sum([app.get_monthly_expense() for app in room.appliances])
            data += f"--- Appliances monthly cost: {appliances_cost:.2f}$" + '\n'
        return data
