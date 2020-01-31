from time import *

roomArray = []
itemArray = []
#items are "key", "axe", "broom", "wrench", "knife", "health", "money", "clipboard"

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[300] = "You are at the front entrance of the mental facility. The front door is locked, so the only way to move is South."
roomArray[201] = "You stand in the top left corner of the main lobby. It is very chilly in this corner."
roomArray[301] = "You look all around you. It is a cramped lobby: to the East and West is nothing special, but to the South you can see a hallway."
roomArray[401] = "You decide to sit in a chair for no good reason. There is a desk to the South."
roomArray[202] = "You walk into the lower left corner of the lobby. To the East, there is a hallway entrance."
roomArray[302] = "You stand right in the middle of the main lobby. To the South, there is a hallway. To the East, there is a desk."
roomArray[402] = "You stand in front of a desk. To the East, there is a short hallway. To the West, there is a longer one."
roomArray[502] = "You stand in the middle of the short hallway. To the West is a desk. To the East is a door."
roomArray[602] = "A huge iron door is directly to the West of you. Kinda eerie."
roomArray[303] = "You are at the biginning of the hallway. You look out of a window and see that it's probably after midnight."
roomArray[304] = "A door that leads to the janitor's closet is South of you."
roomArray[205] = "You are standing in a dark, smaller section of the closet.  You're surrounded by walls to the North, West, and South.  The closet opens back up to the East."
roomArray[305] = "Inside the janitor's closet, you see nothing really. It's pretty dark."
roomArray[405] ="You're now in the Northeast corner of the closet.  It smells strong of bleach.  There's a dark room to the West but you can't see that far."
roomArray[306] = "You've reached a wall to the South and West.  There's spilled cleaner on the floor."
roomArray[406] = "You are standing in the Southeast corner of the closet.  Theres a small single light bulb above your head and theres a cool breeze flowing from a vent near the floor on the wall."

def doesRoomExist(roomNumber):
  try:
    if roomArray[roomNumber] == False:
      print("You can’t go there.") 
      return False
    else:
      return True 
  except:
    print("You can't go there.")
    return False

def move(userInput, location):
  if userInput == "n" and doesRoomExist(location - 1) == True:
    location -= 1
  else:
    if userInput == "s" and doesRoomExist(location + 1) == True:
      location += 1
    else:
      if userInput == "e" and doesRoomExist(location + 100) == True:
        location += 100
      else:
        if userInput == "w" and doesRoomExist(location - 100) == True:
          location -= 100
  return location

def main():
  location = 300
  print("MENTAL")
  print("by: Isaac, Caleb, Sanjeev, and Jon")
  sleep(1)
  while True:
    print(roomArray[location])
    print("Please type: n, s, e, w, or quit")
    userInput = input()
    location = move(userInput, location)
