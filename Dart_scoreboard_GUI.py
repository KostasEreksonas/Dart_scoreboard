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
        # Add name of player 1 to namesLayout
        self.namesLayout.addWidget(self.name1)
        # Create an instance of QLineEdit to put a name of player 2
        self.name2 = QLineEdit()
        # Add name of player 2 to namesLayout
        self.namesLayout.addWidget(self.name2)
        self.name1.setFixedHeight(35)
        self.name2.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)
        # Add player names to the general layout
        self.generalLayout.addLayout(self.namesLayout)

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
