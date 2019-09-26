from django.contrib.auth.models import User
from adventure.models import Player, Room
import random


Room.objects.all().delete()
number_rooms = []
direction = 1
reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
width = 0
height = 0
size_x = 10
size_y = 10
num_rooms = 100

title = ['Garden Room','Living Room', 'Treasure Room', 
'Dining Room', 'Trading Room', 'Sports Room', 'Bedroom', 
'Flower Room', 'Dungeon Room', 'Movie Room', 'Astronomy Room', 'Library','Coatroom',
'CookRoom', 'FireRoom', 'HeadRoom', 'HouseRoom', 'MultiRoom', 'SaddleRoom', 'SailRoom',
'ShelfRoom', 'StackRoom', 'StreetRoom', 'WareRoom', 'BreadRoom', 'GuardRoom', 'HotelRoom', 
'Study room', 'Closet', 'Cellar Room', 'Kitchen', 'Gym', 'Sauna Room', 'Pool Room', 'Computer Room',
'Mushroom', 'Newsroom', 'BoardRoom', 'Storage Room', 'Makeup Room','Jedi Room', 'Dragon Room', 
'Space room', 'Watch room', 'Phone room', 'Self room', 'Light room', 'Play room', 'Ballroom', 
'Hospital room', 'Kids room', 'Watch room', 'Candle room', 'Basketball room', 'Game room',
'Wine Room', 'Programming Room', 'Fantasy Room', 'Salsa Room', 'Taco Room', 'Roof Top Room',
'Music Room', 'Clothes room', 'Theatre room', 'Control room', 'Nail Salon', 'Hair Salon room',
'Greenhouse room', 'Balcony', 'Moose Room', 'Break Room', 'Muddy Room', 'Amber Room', 'Holy Room',
'Dart room', 'Armageddon Room', 'Ancient Room', 'Avalon Room', 'Gem Room', 'Lost Souls Room', 'NightMare Room',
'Bay Room','Costello Room','Cleaning Room', 'Laundry Room', 'Art Room', 'Piano Room', 'Electric room', 'History room', 
'Studio', 'Basement', 'Attic', 'Hallway', 'Bookstore', 'Pantry room', 'Candy room', 'tennis room', 'Doll room', 'Lambda room',
'Build room', 'Car room', 'Remote room', 'Yoga room', 'Dance room' ]

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
    print("room_count : {}, num_rooms: {}".format(room_count, num_rooms))    
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
    print("After if")
    # gen_title = random.choice(title)
    # gen_description = random.choice(description)
    room = Room(title=title[room_count], description=f"you are in {title[room_count]}", x=0, y=0)
    print(f'room title: {room.title}, room description: {room.description}')
    room.save()
    number_rooms.append(room)
    print("After room")
    grid[y][x] = room
    if previous_room is not None:
        previous_room.connectRooms(room, room_direction)
        room_below = grid[y - 1][x]
        if room_below and random.randint(1,10) % 2 == 0:
            room_below.connectRooms(room, 'n')
    print("After grid")
    previous_room = room
    print(f'room count: {room_count} previous room {previous_room}')
    print("Incrementing")
    room_count += 1
    print(f'room count:{room_count}, previous_room: {previous_room}')

if (room_count == 100):
    previous_room.connectRooms(number_rooms[98], room_direction)
    print(f'room count:{room_count}, previous_room: {previous_room}') 

players=Player.objects.all()
for p in players:
  p.currentRoom= number_rooms[0].id
  p.save()





