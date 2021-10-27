# Dart score calculator

Table of Contents
=================
* [Dart score calculator](#Dart-score-calculator)
* [Dart score calculator program](Dart-score-calculator-program)
* [CLI version](#CLI_version)
* [GUI version](#GUI_version)
* [Previous versions](#Previous-versions)
* [What to update](#What-to-update)
* [Further work](#Further-work)

# Dart score calculator program

This is a simple CLI program used to calculate sets, legs and points of darts game. It is written to count score of a two player game. This program is createad with Python programming language. The code can be found within [Dart_score_calculator.py](Dart_score_calculator.py) file and is distributed under a GNU GPL-3.0 License.

I've also started creating a [GUI version](Dart_score_calculator_GUI.py) of this dart score calculator.

# CLI version

Features of this version are:

1. Count score for a 2 player game.
2. Choose, how many sets and legs you want to play in your game.
3. Set a point count for a leg.
4. Count an average score of 3-dart throws made.
5. Count stats - ammount of times of scored 100's 140's and 180's.

# GUI version

Features of this version are:

1. A comprehensible GUI for counting stats of a darts game.

A sketch of how a finished GUI would look like is presented below:

![Sketch of a dart calculator's GUI](/img/score_calculator_GUI_sketch.png)

Also I have added a [.drawio file for calculator's GUI scheme](/schemes/score_calculator_GUI_sketch.drawio) in a [schemes](/schemes/) folder.

Next is the sketch of a ***Dialog*** window, which is used for collecting user input and data about the darts game. It is presented below:

![Sketch of a dialog for user input](/img/score_calculator_Dialog_sketch.png)

Also I have added a [.drawio file for calculator's Dialog scheme](/schemes/score_calculator_Dialog_sketch.drawio) in a [schemes](/schemes/) folder.

# Previous versions

Previous versions of Dart scoreboard programs are stored in [Previous versions](/Previous_versions) folder.

# What to update

In ***v0.2*** I will implement these updates:

1. Clean the code for drawing Main window and Dialog window.
2. Pass user input from Dialog to the Main window.
3. Input data in specific Main window fields.
4. Pass the user input to predefined functions for calculations.
5. Redraw the Main window with new calculated values.

# Further work
Redesign of dart scoreboard's GUI code.
