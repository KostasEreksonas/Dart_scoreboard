#!/usr/bin/env python3

# The software is distributer under a GNU GPL v3.0 license.

# version = 0.1

# Variables
set_1 = 0
set_2 = 0
leg_1 = 0
leg_2 = 0
points_1 = 0
points_2 = 0
total_1 = 0
total_2 = 0
avg_1 = 0
avg_2 = 0
count_1 = 0
count_2 = 0

# User input
player_1 = input("Enter name of the first player: ")
player_2 = input("Enter name of the second player: ")
print("How many sets: ")
sets = int(input())
print("How many legs: ")
legs = int(input())
print("How many points for a leg: ")
points = int(input())

# Assign set points to both players
points_1 = points
points_2 = points

# Set the starting person of the match
while True:
    print("Who will start the game?")
    starting_player = str(input())
    if (starting_player == player_1):
        print("{} starts the game.".format(player_1))
        c = 1
        break
    elif (starting_player == player_2):
        print("{} starts the game.".format(player_2))
        c = 2
        break
    else:
        print("Error! Please type again, who will start the game.")

while ((set_1 != sets) or (set_2 != sets)):
    if (c == 1):
        # Point count for the first player
        print("How many points player {} scored: ".format(player_1))
        points_scored_1 = int(input())
        if ((points_1 - points_scored_1) < 0) or ((points_1 - points_scored_1) == 1):
            c = 2
            count_1 += 1
            print("{} has ".format(player_1) + str(points_1) + " points left.")
        else:
            c = 2
            count_1 += 1
            points_1 -= points_scored_1
            print("{} has ".format(player_1) + str(points_1) + " points left.")
        total_1 += points_scored_1
        avg_1 = total_1/count_1
        print("Player {}".format(player_1) + " has " + str(avg_1) + " points average.")
        # Leg count for the first player
        if (points_1 == 0):
            leg_1 += 1
            points_1 = points
            points_2 = points
            print("{} won the leg. ".format(player_1) + "The player won " + str(leg_1) + " legs and " + str(set_1) + " sets.")

        # Set count for the first player
        if (leg_1 == legs):
            set_1 += 1
            leg_1 = 0
            leg_2 = 0
            points_1 = points
            points_2 = points
            print("{} won the set. ".format(player_1) + "The player won " + str(leg_1) + " legs and " + str(set_1) + " sets.")

        # Game win condition for the first player
        if (set_1 == sets):
            print("Player {} won the game.".format(player_1))
            break

    if (c == 2):
        # Point count for the second player
        print("How many points player {} scored: ".format(player_2))
        points_scored_2 = int(input())
        if ((points_2 - points_scored_2) < 0) or ((points_2 - points_scored_2) == 1):
            c = 1
            count_2 += 1
            print("{} has ".format(player_2) + str(points_2) + " points left.")
        else:
            c = 1
            count_2 += 1
            points_2 -= points_scored_2
            print("{} has ".format(player_2) + str(points_2) + " points left.")
        total_2 += points_scored_2
        avg_2 = total_2/count_2
        print("Player {}".format(player_2) + " has " + str(avg_2) + " points average.")

        # Leg count for the second player
        if (points_2 == 0):
            leg_2 += 1
            points_1 = points
            points_2 = points
            print("{} won the leg. ".format(player_2) + "The player won " + str(leg_2) + " legs and " + str(set_2) + " sets.")

        # Set count for the second player
        if (leg_2 == legs):
            set_2 += 1
            leg_1 = 0
            leg_2 = 0
            points_1 = points
            points_2 = points
            print("{} won the set. ".format(player_2) + "The player won " + str(leg_2) + " legs and " + str(set_2) + " sets.")

        # Game win condition for the second player
        if (set_2 == sets):
            print("Player {} won the game.".format(player_2))
            break
