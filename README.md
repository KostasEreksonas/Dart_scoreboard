# Dart Score Calculator

Project for creating scoreboard for the game of Darts. There are CLI and GUI versions of the scoreboard.

Table of Contents
=================
* [Dart Score Calculator](#Dart-Score-Calculator)
* [Versions](#Versions)
* [CLI Version](#CLI_Version)
* [GUI Version](#GUI_Version)
* [Further work](#Further-Work)

# Versions

1. The scoreboard working within Command Line Interface (CLI) can be found in [CLI folder](/CLI) and the source code [can be found by following this link](/CLI/Dart_scoreboard.py).
2. The graphical version of the scoreboard with GUI can be found in [GUI](/GUI) folder and the source code for it [can be found here](/GUI/Graphical_dart_scoreboard_v_0_2.py).
3. Previous versions of the scoreboard with GUI can be found in [Previous versions](/GUI/Previous_versions) subfolder within GUI folder.

# CLI Version

Features of this version are:

1. Count score for a 2 player game.
2. Choose, how many sets and legs you want to play in your game.
3. Set a point count for a leg.
4. Count an average score of 3-dart throws made.
5. Count stats - ammount of times of scored 100's 140's and 180's.

# GUI Version

Features of this version are:

1. A comprehensible GUI for counting stats of a darts game.

A sketch of how a finished GUI would look like is presented below:

![Sketch of a dart calculator's GUI](/img/score_calculator_GUI_sketch.png)

Also I have added a [.drawio file for calculator's GUI scheme](/schemes/score_calculator_GUI_sketch.drawio) in a [schemes](/schemes/) folder.

Next is the sketch of a ***Dialog*** window, which is used for collecting user input and data about the darts game. It is presented below:

![Sketch of a dialog for user input](/img/score_calculator_Dialog_sketch.png)

Also I have added a [.drawio file for calculator's Dialog scheme](/schemes/score_calculator_Dialog_sketch.drawio) in a [schemes](/schemes/) folder.

# Further Work

In ***v0.2*** I will redesign the code of the GUI and will implement these updates:

1. Clean the code for drawing Main window and Dialog window.
2. Pass user input from Dialog to the Main window.
3. Input data in specific Main window fields.
4. Pass the user input to predefined functions for calculations.
5. Redraw the Main window with new calculated values.
