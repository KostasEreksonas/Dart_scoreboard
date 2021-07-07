#!/usr/bin/env python3

# Filename Dart_score_calculator_GUI.py

__version__ = '0.1'
__author__ = 'Kostas Ereksonas'

import sys

# Import needed PyQt5 widgets for creating a dart score calculator program's graphical user interface
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import Q(...)

class scoreboardUI(QMainWindow):
    """Main window of dart scoreboard."""
    def __init__(self):
        super().__init__()
