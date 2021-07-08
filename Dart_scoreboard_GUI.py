#!/usr/bin/env python3

# Filename Dart_score_calculator_GUI.py

__version__ = '0.1'
__author__ = 'Kostas Ereksonas'

import sys

# Import needed PyQt5 widgets for creating a dart score calculator program's graphical user interface
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
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
        self.setFixedSize(400, 400) # Just a placeholder values for now
        # Set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create display
        self._createDisplay()
        self._namePlayer()

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
        # Set layout for player name display line
        self.namesLayout = QHBoxLayout()
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

    def _legsStats(self):
        """Displaying won legs statistics for both players."""

    def _pointsStats(self):
        """Displaying  points left in a leg for both players."""

    def _100+(self):
        """Displaying a number of scored 100+ point 3-dart throws."""

    def _140+(self):
        """Displaying a number of scored 140+ point 3-dart throws."""

    def _180(self):
        """Displaying a number of scored 180 point 3-dart throws."""

    def _scoreMax(self):
        """Displaying the best score of a 3-dart throw."""

    def _scoreAverage(self):
        """Displaying the average score of a 3-dart throw."""

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
