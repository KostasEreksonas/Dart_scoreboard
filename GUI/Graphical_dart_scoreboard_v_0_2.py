#!/usr/bin/env python3

# Filename: Graphical_dart_scoreboard_v_0_2.py

# Dependencies: Python3, PyQt5.QtCore, PyQt5.QtWidgets

__version__ = "0.2"
__author__ = "Kostas Ereksonas"

#  ---------
# | Imports |
#  ---------

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel

#  ---------
# | Classes |
#  ---------
"""In this section I will define classes for the program"""

#  --------------
# | Calculations |
#  --------------
class calculateResults():
    def __init__(self, score):
        self.score = score

    def count100(score):
        if (score >= 100) and (score < 140):
            c100 += 1
        return c100

    def count140(score):
        if (score >= 140) and (score < 179):
            c140 += 1
        return c140

    def count180(score):
        if (score == 180):
            c180 += 1
        return c180

    def countLeg(score):
        if (score == 0):
            leg += 1
        return leg

    def countSet(legCurrent, legWin):
        if (legCurrent == legWin):
            set += 1
        return set

    def pointsLeft(points, score):
        points -= score
        return points

    def namePlayer1(player1):
        player1 = input("Enter name of player 1:")
        return player1

    def namePlayer2(player2):
        player2 = input("Enter name of player 2:")
        return player2


#  -------------
# | Main Window |
#  -------------
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

#  ---------------
# | Dialog window |
#  ---------------
class dialogWindow(QDialog):
    def __init__(self):
        super().__init__()


def main():
    """Main function."""
    scoreboard = QApplication(sys.argv)
    view = mainWindow()
    view.show()
    dialog = dialogWindow()
    sys.exit(scoreboard.exec_())

if __name__ == "__main__":
    main()
