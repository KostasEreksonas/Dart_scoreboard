#!/usr/bin/env python3

# Filename: Graphical_dart_scoreboard_v_0_2.py

# Dependencies: Python3, PyQt5.QtCore, PyQt5.QtWidgets

__version__ = "0.2"
__author__ = "Kostas Ereksonas"

#  ---------
# | Imports |
#  ---------

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit

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

    def count100(self, c100):
        if (self.score >= 100) and (self.score < 140):
            c100 += 1
        return c100

    def count140(self, c140):
        if (score >= 140) and (score < 179):
            c140 += 1
        return c140

    def count180(self, c180):
        if (score == 180):
            c180 += 1
        return c180

    def countLeg(self, leg):
        if (score == 0):
            leg += 1
        return leg

    def countSet(legCurrent, legWin):
        if (legCurrent == legWin):
            set += 1
        return set

    def pointsLeft(self, points):
        points -= score
        return points


#  ------------
# | User Input |
#  ------------
class userInput():
    def __init__(self):
        self.player1 = player1
        self.player2 = player2

    def namePlayer1(player1):
        player1 = input("Enter name of player 1:")
        return player1

    def namePlayer2(player2):
        player2 = input("Enter name of player 2:")
        return player2

    def legCount(legNumber):
        legNumber = input("Number of legs to play:")
        return legNumber

    def legCount(setNumber):
        setNumber = input("Number of sets to play:")
        return setNumber


#  -------------
# | Main Window |
#  -------------
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createWindow()

    def createWindow(self):
        self.setWindowTitle("Dart Scoreboard")
        self.setFixedSize(400, 450)
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.heading = QLineEdit()
        self.heading.setFixedHeight(35)
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setText("Dart scoreboard")
        self.heading.setReadOnly(True)
        self.generalLayout.addWidget(self.heading)
        displayText = ["", "Player1", "Player2", "Sets won", "0", "0", "Legs won", "0", "0", "Points left", "0", "0", "Points scored", "0", "0", "100+", "0", "0", "140+", "0", "0", "180s", "0", "0", "Max score", "0", "0","Average score", "0", "0"]
        displayBoxes = []
        for i in range(len(displayText)//3+1):
            for j in range(3):
                self.textBox = QLineEdit()
                self.boxLayout = QHBoxLayout()
                self.textBox.setFixedHeight(35)
                self.textBox.setReadOnly(True)
                if i == 1:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j])
                    for l in range(len(displayBoxes)):
                        self.boxLayout.addWidget(displayBoxes[l])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 2:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+3])
                    for l in range(len(displayBoxes)-3):
                        self.boxLayout.addWidget(displayBoxes[l+3])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 3:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+6])
                    for l in range(len(displayBoxes)-6):
                        self.boxLayout.addWidget(displayBoxes[l+6])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 4:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+9])
                    for l in range(len(displayBoxes)-9):
                        self.boxLayout.addWidget(displayBoxes[l+9])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 5:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+12])
                    for l in range(len(displayBoxes)-12):
                        self.boxLayout.addWidget(displayBoxes[l+12])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 6:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+15])
                    for l in range(len(displayBoxes)-15):
                        self.boxLayout.addWidget(displayBoxes[l+15])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 7:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+18])
                    for l in range(len(displayBoxes)-18):
                        self.boxLayout.addWidget(displayBoxes[l+18])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 8:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+21])
                    for l in range(len(displayBoxes)-21):
                        self.boxLayout.addWidget(displayBoxes[l+21])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 9:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+24])
                    for l in range(len(displayBoxes)-24):
                        self.boxLayout.addWidget(displayBoxes[l+24])
                    self.generalLayout.addLayout(self.boxLayout)
                if i == 10:
                    displayBoxes.append(self.textBox)
                    self.textBox.setText(displayText[j+27])
                    for l in range(len(displayBoxes)-27):
                        self.boxLayout.addWidget(displayBoxes[l+27])
                    self.generalLayout.addLayout(self.boxLayout)


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
