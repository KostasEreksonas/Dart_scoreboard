#!/usr/bin/env python3

# Filename Dart_score_calculator_GUI.py

__version__ = '0.1'
__author__ = 'Kostas Ereksonas'

import sys

# Import needed PyQt5 widgets for creating a dart score calculator program's graphical user interface
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget

class scoreboardUI(QMainWindow):
    """Main window of dart scoreboard."""
    def __init__(self):
        super().__init__()
        # Set properties of main window
        self.setWindowTitle('Dart scoreboard')
        self.setFixedSize(400, 450) # Just a placeholder values for now
        # Set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create display
        self._createDisplay()
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

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set properties of the display
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)
        self.display.setText("Dart scoreboard")
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _namePlayer(self):
        """Display names of a dart match players."""
        # Set layout for player name display line
        self.namesLayout = QHBoxLayout()
        # Display a title of a set line
        self.nameBlank = QLineEdit()
        # Set height of player 1 name field
        self.nameBlank.setFixedHeight(35)
        # Set alignment of player 1's name
        self.nameBlank.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.nameBlank.setReadOnly(True)
        # Add name of player 1
        self.nameBlank.setText("")
        # Add name of player 1 to namesLayout
        self.namesLayout.addWidget(self.nameBlank)
        # Create an instance of QLineEdit to put a name of player 1
        self.name1 = QLineEdit()
        # Set height of player 1 name field
        self.name1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.name1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.name1.setReadOnly(True)
        # Add name of player 1
        self.name1.setText("Player 1")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.namesLayout.addWidget(self.name1)
        # Create an instance of QLineEdit to put a name of player 2
        self.name2 = QLineEdit()
        # Set height of player 2 name field
        self.name2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.name2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.name2.setReadOnly(True)
        # Add name of player 2
        self.name2.setText("Player 2")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.namesLayout.addWidget(self.name2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.namesLayout)

    def _setsStats(self):
        """Displaying won sets statistics for both players."""
        # Set layout for player name display line
        self.setsLayout = QHBoxLayout()
        # Display a title of a set line
        self.setName = QLineEdit()
        # Set height of player 1 name field
        self.setName.setFixedHeight(35)
        # Set alignment of player 1's name
        self.setName.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.setName.setReadOnly(True)
        # Add name of player 1
        self.setName.setText("Sets won")
        # Add name of player 1 to namesLayout
        self.setsLayout.addWidget(self.setName)
        # Create an instance of QLineEdit to put a name of player 1
        self.set1 = QLineEdit()
        # Set height of player 1 name field
        self.set1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.set1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.set1.setReadOnly(True)
        # Add name of player 1
        self.set1.setText("0")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.setsLayout.addWidget(self.set1)
        # Create an instance of QLineEdit to put a name of player 2
        self.set2 = QLineEdit()
        # Set height of player 2 name field
        self.set2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.set2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.set2.setReadOnly(True)
        # Add name of player 2
        self.set2.setText("0")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.setsLayout.addWidget(self.set2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.setsLayout)

    def _legsStats(self):
        """Displaying won legs statistics for both players."""
        # Set layout for player name display line
        self.legsLayout = QHBoxLayout()
        # Display a title of a leg line
        self.legName = QLineEdit()
        # Set height of player 1 name field
        self.legName.setFixedHeight(35)
        # Set alignment of player 1's name
        self.legName.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.legName.setReadOnly(True)
        # Add name of player 1
        self.legName.setText("Legs won")
        # Add name of player 1 to namesLayout
        self.legsLayout.addWidget(self.legName)
        # Create an instance of QLineEdit to put a name of player 1
        self.leg1 = QLineEdit()
        # Set height of player 1 name field
        self.leg1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.leg1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.leg1.setReadOnly(True)
        # Add name of player 1
        self.leg1.setText("0")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.legsLayout.addWidget(self.leg1)
        # Create an instance of QLineEdit to put a name of player 2
        self.leg2 = QLineEdit()
        # Set height of player 2 name field
        self.leg2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.leg2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.leg2.setReadOnly(True)
        # Add name of player 2
        self.leg2.setText("0")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.legsLayout.addWidget(self.leg2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.legsLayout)

    def _pointsLeft(self):
        """Displaying  points left in a leg for both players."""
        # Set layout for player name display line
        self.pointsLayout = QHBoxLayout()
        # Display a title of a leg line
        self.pointsName = QLineEdit()
        # Set height of player 1 name field
        self.pointsName.setFixedHeight(35)
        # Set alignment of player 1's name
        self.pointsName.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.pointsName.setReadOnly(True)
        # Add name of player 1
        self.pointsName.setText("Points left")
        # Add name of player 1 to namesLayout
        self.pointsLayout.addWidget(self.pointsName)
        # Create an instance of QLineEdit to put a name of player 1
        self.point1 = QLineEdit()
        # Set height of player 1 name field
        self.point1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.point1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.point1.setReadOnly(True)
        # Add name of player 1
        self.point1.setText("501")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.pointsLayout.addWidget(self.point1)
        # Create an instance of QLineEdit to put a name of player 2
        self.point2 = QLineEdit()
        # Set height of player 2 name field
        self.point2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.point2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.point2.setReadOnly(True)
        # Add name of player 2
        self.point2.setText("501")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.pointsLayout.addWidget(self.point2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.pointsLayout)

    def _pointsScored(self):
        """Displaying  points scored in a 3-dart throw for both players."""
        # Set layout for player name display line
        self.scoredLayout = QHBoxLayout()
        # Display a title of a leg line
        self.scoredName = QLineEdit()
        # Set height of player 1 name field
        self.scoredName.setFixedHeight(35)
        # Set alignment of player 1's name
        self.scoredName.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.scoredName.setReadOnly(True)
        # Add name of player 1
        self.scoredName.setText("Points scored")
        # Add name of player 1 to namesLayout
        self.scoredLayout.addWidget(self.scoredName)
        # Create an instance of QLineEdit to put a name of player 1
        self.scored1 = QLineEdit()
        # Set height of player 1 name field
        self.scored1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.scored1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.scored1.setReadOnly(True)
        # Add name of player 1
        self.scored1.setText("180")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.scoredLayout.addWidget(self.scored1)
        # Create an instance of QLineEdit to put a name of player 2
        self.scored2 = QLineEdit()
        # Set height of player 2 name field
        self.scored2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.scored2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.scored2.setReadOnly(True)
        # Add name of player 2
        self.scored2.setText("180")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.scoredLayout.addWidget(self.scored2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.scoredLayout)

    def _100(self):
        """Displaying a number of scored 100+ point 3-dart throws."""
        # Set layout for player name display line
        self._100Layout = QHBoxLayout()
        # Display a title of a leg line
        self._100Name = QLineEdit()
        # Set height of player 1 name field
        self._100Name.setFixedHeight(35)
        # Set alignment of player 1's name
        self._100Name.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self._100Name.setReadOnly(True)
        # Add name of player 1
        self._100Name.setText("100+")
        # Add name of player 1 to namesLayout
        self._100Layout.addWidget(self._100Name)
        # Create an instance of QLineEdit to put a name of player 1
        self._100_1 = QLineEdit()
        # Set height of player 1 name field
        self._100_1.setFixedHeight(35)
        # Set alignment of player 1's name
        self._100_1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self._100_1.setReadOnly(True)
        # Add name of player 1
        self._100_1.setText("0")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self._100Layout.addWidget(self._100_1)
        # Create an instance of QLineEdit to put a name of player 2
        self._100_2 = QLineEdit()
        # Set height of player 2 name field
        self._100_2.setFixedHeight(35)
        # Set alignment of player 2's name
        self._100_2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self._100_2.setReadOnly(True)
        # Add name of player 2
        self._100_2.setText("0")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self._100Layout.addWidget(self._100_2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self._100Layout)

    def _140(self):
        """Displaying a number of scored 140+ point 3-dart throws."""
        # Set layout for player name display line
        self._140Layout = QHBoxLayout()
        # Display a title of a leg line
        self._140Name = QLineEdit()
        # Set height of player 1 name field
        self._140Name.setFixedHeight(35)
        # Set alignment of player 1's name
        self._140Name.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self._140Name.setReadOnly(True)
        # Add name of player 1
        self._140Name.setText("140+")
        # Add name of player 1 to namesLayout
        self._140Layout.addWidget(self._140Name)
        # Create an instance of QLineEdit to put a name of player 1
        self._140_1 = QLineEdit()
        # Set height of player 1 name field
        self._140_1.setFixedHeight(35)
        # Set alignment of player 1's name
        self._140_1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self._140_1.setReadOnly(True)
        # Add name of player 1
        self._140_1.setText("0")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self._140Layout.addWidget(self._140_1)
        # Create an instance of QLineEdit to put a name of player 2
        self._140_2 = QLineEdit()
        # Set height of player 2 name field
        self._140_2.setFixedHeight(35)
        # Set alignment of player 2's name
        self._140_2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self._140_2.setReadOnly(True)
        # Add name of player 2
        self._140_2.setText("0")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self._140Layout.addWidget(self._140_2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self._140Layout)

    def _180(self):
        """Displaying a number of scored 180 point 3-dart throws."""
        # Set layout for player name display line
        self._180Layout = QHBoxLayout()
        # Display a title of a leg line
        self._180Name = QLineEdit()
        # Set height of player 1 name field
        self._180Name.setFixedHeight(35)
        # Set alignment of player 1's name
        self._180Name.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self._180Name.setReadOnly(True)
        # Add name of player 1
        self._180Name.setText("180s")
        # Add name of player 1 to namesLayout
        self._180Layout.addWidget(self._180Name)
        # Create an instance of QLineEdit to put a name of player 1
        self._180_1 = QLineEdit()
        # Set height of player 1 name field
        self._180_1.setFixedHeight(35)
        # Set alignment of player 1's name
        self._180_1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self._180_1.setReadOnly(True)
        # Add name of player 1
        self._180_1.setText("0")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self._180Layout.addWidget(self._180_1)
        # Create an instance of QLineEdit to put a name of player 2
        self._180_2 = QLineEdit()
        # Set height of player 2 name field
        self._180_2.setFixedHeight(35)
        # Set alignment of player 2's name
        self._180_2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self._180_2.setReadOnly(True)
        # Add name of player 2
        self._180_2.setText("0")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self._180Layout.addWidget(self._180_2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self._180Layout)

    def _scoreMax(self):
        """Displaying the best score of a 3-dart throw."""
        # Set layout for player name display line
        self.maxLayout = QHBoxLayout()
        # Display a title of a leg line
        self.maxName = QLineEdit()
        # Set height of player 1 name field
        self.maxName.setFixedHeight(35)
        # Set alignment of player 1's name
        self.maxName.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.maxName.setReadOnly(True)
        # Add name of player 1
        self.maxName.setText("Max score")
        # Add name of player 1 to namesLayout
        self.maxLayout.addWidget(self.maxName)
        # Create an instance of QLineEdit to put a name of player 1
        self.max1 = QLineEdit()
        # Set height of player 1 name field
        self.max1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.max1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.max1.setReadOnly(True)
        # Add name of player 1
        self.max1.setText("180")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.maxLayout.addWidget(self.max1)
        # Create an instance of QLineEdit to put a name of player 2
        self.max2 = QLineEdit()
        # Set height of player 2 name field
        self.max2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.max2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.max2.setReadOnly(True)
        # Add name of player 2
        self.max2.setText("180")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.maxLayout.addWidget(self.max2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.maxLayout)

    def _scoreAverage(self):
        """Displaying the average score of a 3-dart throw."""
        # Set layout for player name display line
        self.averageLayout = QHBoxLayout()
        # Display a title of a leg line
        self.averageName = QLineEdit()
        # Set height of player 1 name field
        self.averageName.setFixedHeight(35)
        # Set alignment of player 1's name
        self.averageName.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.averageName.setReadOnly(True)
        # Add name of player 1
        self.averageName.setText("Average score")
        # Add name of player 1 to namesLayout
        self.averageLayout.addWidget(self.averageName)
        # Create an instance of QLineEdit to put a name of player 1
        self.average1 = QLineEdit()
        # Set height of player 1 name field
        self.average1.setFixedHeight(35)
        # Set alignment of player 1's name
        self.average1.setAlignment(Qt.AlignCenter)
        # Set player 1's name field Read-Only
        self.average1.setReadOnly(True)
        # Add name of player 1
        self.average1.setText("180")          # Placeholder for now, will write a function for user input later
        # Add name of player 1 to namesLayout
        self.averageLayout.addWidget(self.average1)
        # Create an instance of QLineEdit to put a name of player 2
        self.average2 = QLineEdit()
        # Set height of player 2 name field
        self.average2.setFixedHeight(35)
        # Set alignment of player 2's name
        self.average2.setAlignment(Qt.AlignCenter)
        # Set player 2's name field Read-Only
        self.average2.setReadOnly(True)
        # Add name of player 2
        self.average2.setText("180")          # Same as for player 1
        # Add name of player 2 to namesLayout
        self.averageLayout.addWidget(self.average2)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.averageLayout)


class scoreboardCtrl:
    """Class for controlling actions for the scoreboard."""
    def __init__(self):
        """Initialization of the controller mechanism."""


class Dialog(QDialog):
    """Dialog window of dart scoreboard."""
    def __init__(self):
        super().__init__()
        # Set properties of main window
        self.setWindowTitle('User input')
        self.setFixedSize(400, 400) # Just a placeholder values for now
        # Set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

# Main function
def main():
    """Main function."""
    # Create an instance of QApplication
    scoreboard = QApplication(sys.argv)
    # Show GUI of the application
    view = scoreboardUI()
    view.show()
    # Execute the main loop
    sys.exit(scoreboard.exec_())

if __name__ == '__main__':
    main()
