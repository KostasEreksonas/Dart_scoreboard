#!/usr/bin/env python3

# Filename Graphical_dart_scoreboard.py

# Dependencies: Python3, PyQt5.QtCore, PyQt5.QtWidgets

__version__ = '0.1'
__author__ = 'Kostas Ereksonas'

import sys

# Import needed PyQt5 widgets for creating a dart score calculator program's graphical user interface
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget

# Variable list (copied from CLI version of the scoreboard)
player_1 = "Name 1" # Name of the player 1
player_2 = "Name 2" # Name of the player 2
sets = 0            # Number of sets to play
set_1 = 0           # Number of sets that player 1 won
set_2 = 0           # Number of sets that player 2 won
legs = 2            # Number of legs to play
leg_1 = 0           # Number of legs that player 1 won
leg_2 = 0           # Number of legs that player 2 won
points = 0          # Number of points to score for winning a leg
points_1 = 0        # Number of points that player 1 has left
points_2 = 0        # Number of points that player 2 has left
points_scored_1 = 0 # Number of points that player 1 has scored
points_scored_2 = 0 # Number of points that player 2 has scored
average_1 = 0       # Points average for player 1
average_2 = 0       # Points average for player 2
max_1 = 0           # Maximum score of player 1
max_2 = 0           # Maximum score of player 2
count_100_1 = 0     # Count instances when player 1 scored more than 100 points during single 3-dart throw
count_140_1 = 0     # Count instances when player 1 scored more than 140 points during single 3-dart throw
count_180_1 = 0     # Count instances when player 1 scored more than 180 points during single 3-dart throw
count_100_2 = 0     # Count instances when player 2 scored more than 100 points during single 3-dart throw
count_140_2 = 0     # Count instances when player 2 scored more than 140 points during single 3-dart throw
count_180_2 = 0     # Count instances when player 2 scored more than 180 points during single 3-dart throw

class scoreboardUI(QMainWindow):
    """Main window of dart scoreboard."""
    def __init__(self):
        super().__init__()
        # Set title and size of main window
        self.setWindowTitle('Dart scoreboard')
        self.setFixedSize(400, 450)
        # Set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Defined functions of various elements of the scorebard's GUI
        self._createHeading()
        self._namePlayer()
        self._setsStats()
        self._legsStats()
        self._pointsLeft()
        self._pointsScored()
        self._100()
        self._140()
        self._180()
        self._scoreMax()
        self._scoreAverage()
        self._createButtons()

    def _createHeading(self):
        """Create the Heading of the scoreboard."""
        self.heading = QLineEdit()  # Create the heading widget
        # Set properties of the heading
        self.heading.setFixedHeight(35) # Fixed height
        self.heading.setAlignment(Qt.AlignCenter)   # Center alignment
        self.heading.setText("Dart scoreboard") # Heading
        self.heading.setReadOnly(True)  # Set as read only
        self.generalLayout.addWidget(self.heading)  # Add the heading to the general layout

    def _namePlayer(self):
        """Display names of a dart game players."""
        self.namesLayout = QHBoxLayout()    # Set the layout for displaying player names
        self.nameBlank = QLineEdit()        # Add a blank field as every column has 3 rows
        self.nameBlank.setFixedHeight(35)   # Set height of the blank field
        self.nameBlank.setAlignment(Qt.AlignCenter) # Set alignment of the blank field
        self.nameBlank.setReadOnly(True)    # Set the blank field as Read-Only
        self.namesLayout.addWidget(self.nameBlank)  # Add the blank field to the names layout
        self.name1 = QLineEdit()    # Create a field to store the name of Player 1
        self.name1.setFixedHeight(35)   # Set height of player 1's name field
        self.name1.setAlignment(Qt.AlignCenter) # Set alignment of player 1's name
        self.name1.setReadOnly(True)    # Set player 1's name field as Read-Only
        self.name1.setText("{}".format(player_1))   # Set the name of player 1
        self.namesLayout.addWidget(self.name1)  # Add name of player 1 to the names layout
        self.name2 = QLineEdit()    # Create a field to store the name of Player 2
        self.name2.setFixedHeight(35)   # Set height of player 2 name field
        self.name2.setAlignment(Qt.AlignCenter) # Set alignment of player 2's name
        self.name2.setReadOnly(True)    # Set player 2's name field as Read-Only
        self.name2.setText("{}".format(player_2))   # Set the name of player 2
        self.namesLayout.addWidget(self.name2)  # Add name of player 2 to the names layout
        self.generalLayout.addLayout(self.namesLayout)  # Add player names to the general layout

    def _setsStats(self):
        """Displaying won sets statistics for both players."""
        self.setsLayout = QHBoxLayout() # Set layout for displaying set counts
        self.setName = QLineEdit()  # Display a title of a set count fields line
        self.setName.setFixedHeight(35) # Set height of set count field
        self.setName.setAlignment(Qt.AlignCenter)   # Set alignment of the block
        self.setName.setReadOnly(True)  # Set the block as a Read-Only
        self.setName.setText("Sets won")    # Add the title
        self.setsLayout.addWidget(self.setName) # Add the block to sets layout
        self.set1 = QLineEdit() # Create an instance of QLineEdit to put a set count for player 1
        self.set1.setFixedHeight(35)    # Set height of the field
        self.set1.setAlignment(Qt.AlignCenter)  # Set alignment of the field
        self.set1.setReadOnly(True) # Set the field as Read-Only
        self.set1.setText("{}".format(set_1))   # Add counter of sets
        self.setsLayout.addWidget(self.set1)    # Add won set counter to sets layout
        self.set2 = QLineEdit() # Create an instance of QLineEdit to put a set count of player 2
        self.set2.setFixedHeight(35)    # Set height of the field
        self.set2.setAlignment(Qt.AlignCenter)  # Set alignment of the field
        self.set2.setReadOnly(True) # Set the field as Read-Only
        self.set2.setText("{}".format(set_2))   # Add sets counter
        self.setsLayout.addWidget(self.set2)    # Add the field to sets layout
        self.generalLayout.addLayout(self.setsLayout)   # Add set counters to the general layout

    def _legsStats(self):
        """Displaying won legs statistics for both players."""
        self.legsLayout = QHBoxLayout()
        self.legName = QLineEdit()
        self.legName.setFixedHeight(35)
        self.legName.setAlignment(Qt.AlignCenter)
        self.legName.setReadOnly(True)
        self.legName.setText("Legs won")
        self.legsLayout.addWidget(self.legName)
        self.leg1 = QLineEdit()
        self.leg1.setFixedHeight(35)
        self.leg1.setAlignment(Qt.AlignCenter)
        self.leg1.setReadOnly(True)
        self.leg1.setText("{}".format(leg_1))
        self.legsLayout.addWidget(self.leg1)
        self.leg2 = QLineEdit()
        self.leg2.setFixedHeight(35)
        self.leg2.setAlignment(Qt.AlignCenter)
        self.leg2.setReadOnly(True)
        self.leg2.setText("{}".format(leg_2))
        self.legsLayout.addWidget(self.leg2)
        self.generalLayout.addLayout(self.legsLayout)

    def _pointsLeft(self):
        """Displaying  points left in a leg for both players."""
        self.pointsLayout = QHBoxLayout()
        self.pointsName = QLineEdit()
        self.pointsName.setFixedHeight(35)
        self.pointsName.setAlignment(Qt.AlignCenter)
        self.pointsName.setReadOnly(True)
        self.pointsName.setText("Points left")
        self.pointsLayout.addWidget(self.pointsName)
        self.point1 = QLineEdit()
        self.point1.setFixedHeight(35)
        self.point1.setAlignment(Qt.AlignCenter)
        self.point1.setText("{}".format(points_1))
        self.pointsLayout.addWidget(self.point1)
        self.point2 = QLineEdit()
        self.point2.setFixedHeight(35)
        self.point2.setAlignment(Qt.AlignCenter)
        self.point2.setReadOnly(True)
        self.point2.setText("{}".format(points_2))
        self.pointsLayout.addWidget(self.point2)
        self.generalLayout.addLayout(self.pointsLayout)

    def _pointsScored(self):
        """Displaying  points scored in a 3-dart throw for both players."""
        self.scoredLayout = QHBoxLayout()
        self.scoredName = QLineEdit()
        self.scoredName.setFixedHeight(35)
        self.scoredName.setAlignment(Qt.AlignCenter)
        self.scoredName.setReadOnly(True)
        self.scoredName.setText("Points scored")
        self.scoredLayout.addWidget(self.scoredName)
        self.scored1 = QLineEdit()
        self.scored1.setFixedHeight(35)
        self.scored1.setAlignment(Qt.AlignCenter)
        self.scored1.setText("{}".format(points_scored_1))
        self.scoredLayout.addWidget(self.scored1)
        self.scored2 = QLineEdit()
        self.scored2.setFixedHeight(35)
        self.scored2.setAlignment(Qt.AlignCenter)
        self.scored2.setText("{}".format(points_scored_2))
        self.scoredLayout.addWidget(self.scored2)
        self.generalLayout.addLayout(self.scoredLayout)

    def _100(self):
        """Displaying a number of scored 100+ point 3-dart throws."""
        self._100Layout = QHBoxLayout()
        self._100Name = QLineEdit()
        self._100Name.setFixedHeight(35)
        self._100Name.setAlignment(Qt.AlignCenter)
        self._100Name.setReadOnly(True)
        self._100Name.setText("100+")
        self._100Layout.addWidget(self._100Name)
        self._100_1 = QLineEdit()
        self._100_1.setFixedHeight(35)
        self._100_1.setAlignment(Qt.AlignCenter)
        self._100_1.setReadOnly(True)
        self._100_1.setText("{}".format(count_100_1))
        self._100Layout.addWidget(self._100_1)
        self._100_2 = QLineEdit()
        self._100_2.setFixedHeight(35)
        self._100_2.setAlignment(Qt.AlignCenter)
        self._100_2.setReadOnly(True)
        self._100_2.setText("{}".format(count_100_2))
        self._100Layout.addWidget(self._100_2)
        self.generalLayout.addLayout(self._100Layout)

    def _140(self):
        """Displaying a number of scored 140+ point 3-dart throws."""
        self._140Layout = QHBoxLayout()
        self._140Name = QLineEdit()
        self._140Name.setFixedHeight(35)
        self._140Name.setAlignment(Qt.AlignCenter)
        self._140Name.setReadOnly(True)
        self._140Name.setText("140+")
        self._140Layout.addWidget(self._140Name)
        self._140_1 = QLineEdit()
        self._140_1.setFixedHeight(35)
        self._140_1.setAlignment(Qt.AlignCenter)
        self._140_1.setReadOnly(True)
        self._140_1.setText("{}".format(count_140_1))
        self._140Layout.addWidget(self._140_1)
        self._140_2 = QLineEdit()
        self._140_2.setFixedHeight(35)
        self._140_2.setAlignment(Qt.AlignCenter)
        self._140_2.setReadOnly(True)
        self._140_2.setText("{}".format(count_140_2))
        self._140Layout.addWidget(self._140_2)
        self.generalLayout.addLayout(self._140Layout)

    def _180(self):
        """Displaying a number of scored 180 point 3-dart throws."""
        self._180Layout = QHBoxLayout()
        self._180Name = QLineEdit()
        self._180Name.setFixedHeight(35)
        self._180Name.setAlignment(Qt.AlignCenter)
        self._180Name.setReadOnly(True)
        self._180Name.setText("180s")
        self._180Layout.addWidget(self._180Name)
        self._180_1 = QLineEdit()
        self._180_1.setFixedHeight(35)
        self._180_1.setAlignment(Qt.AlignCenter)
        self._180_1.setReadOnly(True)
        self._180_1.setText("{}".format(count_180_1))
        self._180Layout.addWidget(self._180_1)
        self._180_2 = QLineEdit()
        self._180_2.setFixedHeight(35)
        self._180_2.setAlignment(Qt.AlignCenter)
        self._180_2.setReadOnly(True)
        self._180_2.setText("{}".format(count_180_2))
        self._180Layout.addWidget(self._180_2)
        self.generalLayout.addLayout(self._180Layout)

    def _scoreMax(self):
        """Displaying the best score of a 3-dart throw."""
        self.maxLayout = QHBoxLayout()
        self.maxName = QLineEdit()
        self.maxName.setFixedHeight(35)
        self.maxName.setAlignment(Qt.AlignCenter)
        self.maxName.setReadOnly(True)
        self.maxName.setText("Max score")
        self.maxLayout.addWidget(self.maxName)
        self.max1 = QLineEdit()
        self.max1.setFixedHeight(35)
        self.max1.setAlignment(Qt.AlignCenter)
        self.max1.setReadOnly(True)
        self.max1.setText("{}".format(max_1))
        self.maxLayout.addWidget(self.max1)
        self.max2 = QLineEdit()
        self.max2.setFixedHeight(35)
        self.max2.setAlignment(Qt.AlignCenter)
        self.max2.setReadOnly(True)
        self.max2.setText("{}".format(max_2))
        self.maxLayout.addWidget(self.max2)
        self.generalLayout.addLayout(self.maxLayout)

    def _scoreAverage(self):
        """Displaying the average score of a 3-dart throw."""
        self.averageLayout = QHBoxLayout()
        self.averageName = QLineEdit()
        self.averageName.setFixedHeight(35)
        self.averageName.setAlignment(Qt.AlignCenter)
        self.averageName.setReadOnly(True)
        self.averageName.setText("Average score")
        self.averageLayout.addWidget(self.averageName)
        self.average1 = QLineEdit()
        self.average1.setFixedHeight(35)
        self.average1.setAlignment(Qt.AlignCenter)
        self.average1.setReadOnly(True)
        self.average1.setText("{}".format(average_1))
        self.averageLayout.addWidget(self.average1)
        self.average2 = QLineEdit()
        self.average2.setFixedHeight(35)
        self.average2.setAlignment(Qt.AlignCenter)
        self.average2.setReadOnly(True)
        self.average2.setText("{}".format(average_2))
        self.averageLayout.addWidget(self.average2)
        self.generalLayout.addLayout(self.averageLayout)

    def _createButtons(self):
        """Create a button for opening a Dialog window."""
        self.dialogOpen = QPushButton()
        self.dialogOpen.setText("Start game")
        self.dialogOpen.clicked.connect(self._callDialog)
        self.generalLayout.addWidget(self.dialogOpen)

    def _callDialog(self):
        """Function to call Dialog window class."""
        self.dialogWindow = Dialog().exec_()

    # Functions for counting scores and statistics
    def _leftPoints1(self, var):
        """Return how many points player 1 has left."""
        return (points_1 == points_1 - var)

    def _leftPoints2(self, var):
        """Return how many points player 2 has left."""
        return (points_2 == points_2 - var)

class Dialog(QDialog):
    """Dialog window of dart scoreboard."""
    def __init__(self):
        super().__init__()
        # Set properties of main window
        self.setWindowTitle('User input')
        self.setFixedSize(300, 180)
        # Set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)
        # Placed functions for user input fields and buttons
        self._userInput()
        self._dialogButtons(self)

    def _userInput(self):
        """Function for collecting user inputted data."""
        # Set layout of user input fields
        self.inputFields = QVBoxLayout()
        # Set layout of first user input field
        self.inputField1 = QHBoxLayout()
        # Set text of the first user input field
        self.inputField1_Text = QLabel()
        self.inputField1_Text.setText("Input name of the first player")
        # Set alignment of the first input filed's text
        self.inputField1_Text.setAlignment(Qt.AlignCenter)
        # Add text widget to first input field layout
        self.inputField1.addWidget(self.inputField1_Text)
        # Add a box for entering data for the first user input field
        self.inputField1_Data = QLineEdit()
        # Add the box to the first input field's layout
        self.inputField1.addWidget(self.inputField1_Data)
        # Add first input field to inputFields layout
        self.inputFields.addLayout(self.inputField1)
        # Same process repeated for the second field (might offload to a different function later on)
        self.inputField2 = QHBoxLayout()
        self.inputField2_Text = QLabel()
        self.inputField2_Text.setText("Input name of the second player")
        self.inputField2_Text.setAlignment(Qt.AlignCenter)
        self.inputField2.addWidget(self.inputField2_Text)
        self.inputField2_Data = QLineEdit()
        self.inputField2.addWidget(self.inputField2_Data)
        self.inputFields.addLayout(self.inputField2)
        # Same process repeated for the set count field (might offload to a different function later on)
        self.inputField3 = QHBoxLayout()
        self.inputField3_Text = QLabel()
        self.inputField3_Text.setText("How many sets to play")
        self.inputField3_Text.setAlignment(Qt.AlignCenter)
        self.inputField3.addWidget(self.inputField3_Text)
        self.inputField3_Data = QLineEdit()
        self.inputField3.addWidget(self.inputField3_Data)
        self.inputFields.addLayout(self.inputField3)
        # Same process repeated for the leg count field (might offload to a different function later on)
        self.inputField4 = QHBoxLayout()
        self.inputField4_Text = QLabel()
        self.inputField4_Text.setText("How many legs to play")
        self.inputField4_Text.setAlignment(Qt.AlignCenter)
        self.inputField4.addWidget(self.inputField4_Text)
        self.inputField4_Data = QLineEdit()
        self.inputField4.addWidget(self.inputField4_Data)
        self.inputFields.addLayout(self.inputField4)
        # Same process repeated for the point count field (might offload to a different function later on)
        self.inputField5 = QHBoxLayout()
        self.inputField5_Text = QLabel()
        self.inputField5_Text.setText("How many points to win a leg")
        self.inputField5_Text.setAlignment(Qt.AlignLeft)
        self.inputField5.addWidget(self.inputField5_Text)
        self.inputField5_Data = QLineEdit()
        self.inputField5.addWidget(self.inputField5_Data)
        self.inputFields.addLayout(self.inputField5)
        # Add input fields to the general layout
        self.generalLayout.addLayout(self.inputFields)

    def _dialogButtons(self, function):
        """Function for adding buttons to dialog."""
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self._setName1)
        self.buttonBox.accepted.connect(self._setName2)
        self.buttonBox.accepted.connect(self._setSets)
        self.buttonBox.accepted.connect(self._setLegs)
        self.buttonBox.accepted.connect(self._setPoints)
        self.buttonBox.accepted.connect(self._userInput)
        self.buttonBox.rejected.connect(self.reject)
        self.generalLayout.addWidget(self.buttonBox)

    def _setName1(self):
        """Set name of Player 1."""
        player_1 = self.inputField1_Data.text()
        return(player_1)

    def _setName2(self):
        """Set name of Player 2."""
        player_2 = self.inputField2_Data.text()
        return(player_2)

    def _setSets(self):
        """Set the number of sets to play."""
        sets = self.inputField3_Data.text()
        return(sets)

    def _setLegs(self):
        """Set the number of legs to play."""
        legs = self.inputField4_Data.text()
        return(legs)

    def _setPoints(self):
        """Set score to reach for winning a leg."""
        points = self.inputField5_Data.text()
        return(points)


# Main function
def main():
    """Main function."""
    scoreboard = QApplication(sys.argv) # Create an instance of QApplication
    # Show GUI of the application
    view = scoreboardUI()
    view.show()
    dialog = Dialog()   # Instance of a Dialog
    sys.exit(scoreboard.exec_()) # Execute the main loop

if __name__ == '__main__':
    main()
