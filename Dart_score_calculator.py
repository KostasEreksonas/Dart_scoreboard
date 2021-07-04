#!/usr/bin/env python3

# The software is distributer under a GNU GPL v3.0 license.

# version = 0.1

# Variables
set_1 = 0       # Number of sets that player 1 won
set_2 = 0       # Number of sets that player 2 won
leg_1 = 0       # Number of legs that player 1 won
leg_2 = 0       # Number of legs that player 2 won
points_1 = 0    # Number of points that player 1 scored
points_2 = 0    # Number of points that player 2 scored
count_100_1 = 0 # Count instances when player 1 scored more than 100 points during single 3-dart throw
count_140_1 = 0 # Count instances when player 1 scored more than 140 points during single 3-dart throw
count_180_1 = 0 # Count instances when player 1 scored more than 180 points during single 3-dart throw
count_100_2 = 0 # Count instances when player 2 scored more than 100 points during single 3-dart throw
count_140_2 = 0 # Count instances when player 2 scored more than 140 points during single 3-dart throw
count_180_2 = 0 # Count instances when player 2 scored more than 180 points during single 3-dart throw

# User input of match information
player_1 = input("Enter name of the first player: ")
player_2 = input("Enter name of the second player: ")
print("How many sets: ")
sets = int(input())
print("How many legs: ")
legs = int(input())
print("How many points for a leg: ")
points = int(input())

# Assign points to score for both players
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

# Main counter loop
while ((set_1 != sets) or (set_2 != sets)):
    if (c == 1):
        # Point count for the first player
        print("How many points player {} scored: ".format(player_1))
        points_scored_1 = int(input())
        if (points_scored_1 >= 100) and (points_scored_1 < 140):
            count_100_1 += 1
        elif (points_scored_1 >= 140) and (points_scored_1 < 180):
            count_140_1 += 1
        elif (points_scored_1 == 180):
            count_180_1 += 1

        # If player 1 scores more points that (s)he has left, point count does not change
        # Else scored points are deducted from what the player had before a dart throw
        if ((points_1 - points_scored_1) < 0) or ((points_1 - points_scored_1) == 1):
            c = 2
            print("{} has ".format(player_1) + str(points_1) + " points left.")
            print("{} has ".format(player_1) + str(count_100_1) + " 100's scored.")
            print("{} has ".format(player_1) + str(count_140_1) + " 140's scored.")
            print("{} has ".format(player_1) + str(count_180_1) + " 180's scored.")
        else:
            c = 2
            points_1 -= points_scored_1
            print("{} has ".format(player_1) + str(points_1) + " points left.")
            print("{} has ".format(player_1) + str(count_100_1) + " 100's scored.")
            print("{} has ".format(player_1) + str(count_140_1) + " 140's scored.")
            print("{} has ".format(player_1) + str(count_180_1) + " 180's scored.")

        # Leg count for the first player
        # If player 1 gets to 0 points and wins a leg, points of both players resets to whatever was set in the beginning.
        # Also, stats of a leg winner are presented.
        if (points_1 == 0):
            leg_1 += 1
            points_1 = points
            points_2 = points
            print("{} won the leg. ".format(player_1) + "The player won " + str(leg_1) + " legs and " + str(set_1) + " sets.")

        # Set count for the first player
        # If player 1 wins as many legs as it is set in the beginning, the player wins the set.
        # Points of both players are reset to values set at the beginning of the match.
        if (leg_1 == legs):
            set_1 += 1
            leg_1 = 0
            leg_2 = 0
            points_1 = points
            points_2 = points
            print("{} won the set. ".format(player_1) + "The player won " + str(leg_1) + " legs and " + str(set_1) + " sets.")

        # Game win condition for the first player when a player wins as many sets as set in the beginning of the match.
        if (set_1 == sets):
            print("Player {} won the game.".format(player_1))
            break

    if (c == 2):
        # Point count for the second player
        print("How many points player {} scored: ".format(player_2))
        points_scored_2 = int(input())
        if (points_scored_2 >= 100) and (points_scored_2 < 140):
            count_100_2 += 1
        elif (points_scored_2 >= 140) and (points_scored_2 < 180):
            count_140_2 += 1
        elif (points_scored_2 == 180):
            count_180_2 += 1

        # If player 2 scores more points that (s)he has left, point count does not change
        # Else scored points are deducted from what the player had before a dart throw
        if ((points_2 - points_scored_2) < 0) or ((points_2 - points_scored_2) == 1):
            c = 1
            print("{} has ".format(player_2) + str(points_2) + " points left.")
            print("{} has ".format(player_2) + str(count_100_2) + " 100's scored.")
            print("{} has ".format(player_2) + str(count_140_2) + " 140's scored.")
            print("{} has ".format(player_2) + str(count_180_2) + " 180's scored.")
        else:
            c = 1
            points_2 -= points_scored_2
            print("{} has ".format(player_2) + str(points_2) + " points left.")
            print("{} has ".format(player_2) + str(count_100_2) + " 100's scored.")
            print("{} has ".format(player_2) + str(count_140_2) + " 140's scored.")
            print("{} has ".format(player_2) + str(count_180_2) + " 180's scored.")

        # Leg count for the second player
        # If player 2 gets to 0 points and wins a leg, points of both players resets to whatever was set in the beginning.
        # Also, stats of a leg winner are presented.
        if (points_2 == 0):
            leg_2 += 1
            points_1 = points
            points_2 = points
            print("{} won the leg. ".format(player_2) + "The player won " + str(leg_2) + " legs and " + str(set_2) + " sets.")

        # Set count for the second player
        # If player 2 wins as many legs as it is set in the beginning, the player wins the set.
        # Points of both players are reset to values set at the beginning of the match.
        if (leg_2 == legs):
            set_2 += 1
            leg_1 = 0
            leg_2 = 0
            points_1 = points
            points_2 = points
            print("{} won the set. ".format(player_2) + "The player won " + str(leg_2) + " legs and " + str(set_2) + " sets.")

        # Game win condition for the second player when a player wins as many sets as set in the beginning of the match.
        if (set_2 == sets):
            print("Player {} won the game.".format(player_2))
            break
