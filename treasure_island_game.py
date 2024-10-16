print("Welcome to the Treasure Island!")
print("Will you find riches or certain doom...")
way = (input("You are at a cross road, where do you want to go? To your left is a dark cave, to your right is the Forest of Flowers \nEnter left or right ")).lower()

if way == "left":
    way2 = input("You made it out of the cave alive and reached a coast \n It has gotten dark... \n Will you wait till sunrise or swim in the dark? \n swim or wait? ").lower()

    if way2 == "wait":
        way3 = input("You waited till sunrise and swam to an island \n There are three doors on the island. \n One yellow, one red and one blue. \n Which one will you choose? ").lower()
        if way3 == "red":
            print("You died from touching the door knob...")
        elif way3 == "yellow":
            print("You found infinite $$$ and won the game!")
        elif way3 == "blue":
            print("You are allergic to blue paint and die...")
        else:
            print("You died...")
    else:
        print("Creatures of the night pull you down towards the deepest depths...")

else:
    print("Roots entangle your legs and tie them together, you starve... ")







