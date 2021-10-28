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
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

#  ---------
# | Classes |
#  ---------

class scoreboardUI():
    def __init__(self):
        pass

    def createLayout(self):
        pass


class dialogWindow():
    def __init__(self):
        pass


def main():
    """Main function."""
    scoreboard = QApplication(sys.argv)
    view = scoreboardUI()
    view.show()
    dialog = Dialog()
    sys.exit(scoreboard.exec_())

if __name__ == '__main__':
    main()
