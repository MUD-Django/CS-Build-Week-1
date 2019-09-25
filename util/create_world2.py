from django.contrib.auth.models import User
from adventure.models import Player, Room
import random


Room.objects.all().delete()
number_rooms = []
direction = 1
reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
reverse_dir = reverse_dirs[direction]
# grid = []
# width = 0
# height = 0
size_x = 10
size_y = 10
num_rooms = 100


grid = [None] * size_y
width = size_x
height = size_y
for i in range( len(grid) ):
    grid[i] = [None] * size_x

x = -1 
y = 0
room_count = 0

direction = 1  

previous_room = None
while room_count < num_rooms:

    if direction > 0 and x < size_x - 1:
        room_direction = "e"
        x += 1
    elif direction < 0 and x > 0:
        room_direction = "w"
        x -= 1
    else:
        room_direction = "n"
        y += 1
        direction *= -1

    room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
    number_rooms.append(room)

    grid[y][x] = room
    if previous_room is not None:
        previous_room.connectRooms(room, room_direction)
        room_below = grid[y - 1][x]
        if room_below and random.randint(1,10) % 2 == 0:
            room_below.connectRooms(room, 'n')

    previous_room = room

    room_count += 1 

players=Player.objects.all()
for p in players:
  p.currentRoom= number_rooms[0].id
  p.save()





