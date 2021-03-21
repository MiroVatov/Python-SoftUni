class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        available_room = [room for room in self.rooms if room.number == room_number and (room.guests + people) <= room.capacity and not room.is_taken]
        if available_room:
            for room in available_room:
                room.guests += people
                self.guests += people
                room.is_taken = True

    def free_room(self, room_number):
        occupied_room = [room for room in self.rooms if room.number == room_number and room.is_taken]
        if occupied_room:
            for room in occupied_room:
                self.guests -= room.guests
                room.guests = 0
                room.is_taken = False

    def print_status(self):
        print(f'Hotel {self.name} has {self.guests} total guests', end='\n')
        free_rooms = ', '.join([str(room.number) for room in self.rooms if not room.is_taken])
        print(f"Free rooms: {free_rooms}", end='\n')
        taken_rooms = ', '.join([str(room.number) for room in self.rooms if room.is_taken])
        print(f"Taken rooms: {taken_rooms}")

