mport time

class HilbertsInfinityHotel:
    def __init__(self):
        self.rooms = {}  # Store room numbers and their guest counts

    def _room_number(self, index_people, index_people_in_car, index_people_in_boat, index_people_in_group_boat , index_people_in_space_ship):
        """Calculate the room number based on the given formula."""
        return (2 ** index_people) * (3 ** index_people_in_car) * (5 ** index_people_in_boat) * (7 ** index_people_in_group_boat) * (11 ** index_people_in_space_ship)

    def add_guests(self, num_people, num_people_in_car, num_people_in_boat, num_people_in_group_boat , num_people_in_space_ship):
        start_time = time.time()
        for i in range(num_people):
            room = self._room_number(i, num_people_in_car, num_people_in_boat, num_people_in_group_boat , num_people_in_space_ship)
            self.rooms[room] = self.rooms.get(room, 0) + 1  # Increment guest count for the room
        end_time = time.time()
        print(f"Added {num_people} guests in {end_time - start_time:.6f} seconds.")

    def remove_guests(self, room):
        start_time = time.time()
        if room in self.rooms:
            del self.rooms[room]
            print(f"Removed guests from room {room}.")
        else:
            print(f"Room {room} does not exist.")
        end_time = time.time()
        print(f"Removal operation completed in {end_time - start_time:.6f} seconds.")

    def sort_rooms(self):
        start_time = time.time()
        sorted_rooms = sorted(self.rooms.items())  # Sort by room number and get items
        end_time = time.time()
        print(f"Sorted rooms in {end_time - start_time:.6f} seconds.")
        for room, count in sorted_rooms:
            print(f"Room {room} has {count} guests.")  # Display room number and guest count
        return sorted_rooms

    def search_room(self, room):
        start_time = time.time()
        exists = room in self.rooms
        end_time = time.time()
        print(f"Room {room} exists: {exists}. Search operation completed in {end_time - start_time:.6f} seconds.")
        return exists

    def available_rooms(self):
        max_room_number = max(self.rooms.keys(), default=0)
        occupied_rooms = set(self.rooms.keys())
        available = [room for room in range(max_room_number + 1) if room not in occupied_rooms]
        print(f"Available rooms: {available}.")
        return available

    def guests_count(self):
        return sum(self.rooms.values())

# Example usage
hotel = HilbertsInfinityHotel()

# Adding guests
hotel.add_guests(num_people=10, num_people_in_car=0, num_people_in_boat=0, num_people_in_group_boat=0,num_people_in_space_ship=0 )
hotel.add_guests(num_people=10, num_people_in_car=1, num_people_in_boat=0, num_people_in_group_boat=0,num_people_in_space_ship=0 )
# hotel.add_guests(num_people=3, num_people_in_car=3, num_people_in_boat=3, num_people_in_group_boat=3)

# Removing guests
# hotel.remove_guests(room=1)

# Sorting rooms and showing the result
sorted_rooms = hotel.sort_rooms()

# Searching for a room
hotel.search_room(room=1)

# print(hotel.guests_count())

# Displaying available rooms
# hotel.available_rooms()
