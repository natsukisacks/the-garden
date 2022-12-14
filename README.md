# The Garden
This is the repository for The Garden, a game created by Natsuki Sacks and Olga Pidruchna.

## Game Overview
In this game, you can walk around, harvest different types of produce, enjoy the beautiful view and music, and maybe even find a secret little creature. The main objective is to eat as many vegetables as possible.

## Installation and setup
Before playing this game, you need to have pygame installed. You can do this in your terminal with the following command:
`$ pip install pygame`

Optionally, you can install the pytest library to test our code, but this is not necessary to play the game. Install using:
`$ pip install pytest`

To download the code for this game, you can clone this repository to your computer, or download its ZIP file.
Once you have the game downloaded, you can play it by navigating to the folder it’s in and running `$ python main.py` in your terminal.

## File Structure
Our game consists of the following Python files:
- `main.py` puts the model, view, and controller together. Run this file to play the game.
- `model.py` contains the state of the game.
- `view.py` draws the model so it is visible to the player.
- `controller.py` provides the methods for the player to be able to interact with and control the game.

As well as 
- `test_all.py` to test our game.

### Static Files
The folder `/graphics` contains all the images we used in our game, such as the player sprite, background, and all the produce, as well as the font used in the start screen and the sound effect files. The folder `/docs` contains the files used to create our website.

## Website
The website can be found [here](https://olincollege.github.io/the-garden/).
