#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment_7 Maze Runner

Author(s): Alireza Iranmanesh
Group: 63
"""
import Randomizedprims as rprim

class Playground:
    """A class representing a maze playground.

    Attributes:
    - level (int): The level of difficulty of the maze.
    - player (object): The object representing the player in the maze.
    - _playground (object): The object representing the maze itself.

    Methods:
    - __init__(self, level, player): Constructor for the Playground class.
    - __str__(self): Returns the graphical representation of the maze playground object.
    - set_playground(self): Generates the maze and sets the player's initial position in the maze.
    - set_player_pos(self, pos, player): Sets the player's position in the maze.
    - get_pos_status(self, pos): Returns the status of the position in the maze.
    - get_entrance_location(self): Returns the entrance location of the maze.
    - get_destination_location(self): Returns the destination location of the maze.
    """    

    def __init__(self, level, player):
        """Constructor for the Playground class.

        Args:
        - level (int): The level of difficulty of the maze.
        - player (object): The object representing the player in the maze.
        """
        self.level = level
        self.player = player
        self._playground = self.set_playground()

    def __str__(self):
        """Returns the graphical representation of the maze playground object."""
        _str = '_' * len(self._playground.playground) * 2 + '_' + '\n'
        for i in range(0, len(self._playground.playground)):
            for j in range (0, len(self._playground.playground[0])):
                _str += ' ' + self._playground.playground[i][j]['status'] + ''
            _str += '\n'
        _str += '_' * len(self._playground.playground) * 2 + '_'
        return _str

    def set_playground(self):
        """Generates the maze and sets the player's initial position in the maze.

        Returns:
        - _playground (object): The object representing the maze.
        """
        self._playground = rprim.RandomizedPrims(self.level)
        # Initial position of the player 
        self.set_player_pos(self.get_entrance_location(), self.player)
        return self._playground

    def set_player_pos(self, pos, player):
        """Sets the player's position in the maze.
        Args:
        - pos (tuple): The position of the player in the maze.
        - player (object): The object representing the player in the maze.
        """
        row, col = pos
        previous_pos = self.player.get_mz_runner_pos()
        if previous_pos:
            self._playground.playground[previous_pos[0]][previous_pos[1]]['status'] = ' '
        # setting player position into the plaground and player attribute itself
        self.player.set_mz_runner_pos(pos)
        self._playground.playground[row][col]['status'] = player.__str__()

    def get_pos_status(self, pos):
        """Returns the status of the position in the maze.
        Args:
        - pos (tuple): The position in the maze.
        
        Returns:
        - The status of the position in the maze.
        """
        return self._playground.playground[pos[0]][pos[1]]['status']

    def get_entrance_location(self):
        """
        Returns the entrance position in the maze

        Returns:
        - (Tuple) :Returns the entrance position in the maze
        """
        return self._playground.entrance['coordinate']

    def get_destination_location(self):
        """
        Returns the destination position in the maze.

        Returns:
        - (Tuple) :Returns the destination position in the maze
        """
        return self._playground.destination['coordinate']