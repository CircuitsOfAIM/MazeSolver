#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment_7 Maze Runner

Author(s): Alireza Iranmanesh
Group: 63
"""
class Mazerunner(object):
    """
    Class for representing a mazerunner player.

    Attributes:
        name (str): Name of the player.
        _mz_runner_pos (tuple): Current position of the player.

    Methods:
        __init__(self, name): Initializes a new Mazerunner object.
        __str__(self): Returns a string representation of the player.
        __repr__(self): Returns a string representation of the player.
        set_name(self, name): Sets the name of the player.
        get_name(self): Returns the name of the player.
        set_mz_runner_pos(self, mzr_pos): Sets the current position of the player.
        get_mz_runner_pos(self): Returns the current position of the player.
        move(self, direction): Moves the player inside the playground.

    """
    def __init__(self, name):
        """
        Initializes a new Mazerunner object.

        Args:
            name (str): Name of the player.

        """
        #TODO : fix the setter getter for to work properly
        self.name = name
        self._mz_runner_pos = None

    def __str__(self):
        """
        Returns a string representation of the player based on the first letter of the player's name.

        Returns:
            str: The string representation of the player.

        """
        return self.name[0].upper()

    def __repr__(self):
        """
        Returns a string representation of the player instead of the object memory address.

        Returns:
            str: The string representation of the player.

        """
        return str(self.name)

    def set_name(self, name):
        """
        Sets the name of the player.

        Args:
            name (str): Name of the player.

        Returns:
            str: The name of the player.

        """
        self.name = name
        return self.name

    def get_name(self):
        """
        Returns the name of the player.

        Returns:
            str: The name of the player.

        """
        return self.name

    def set_mz_runner_pos(self, mzr_pos):
        """
        Sets the current position of the player.

        Args:
            mzr_pos (tuple): Current position of the player.

        """
        self._mz_runner_pos = mzr_pos

    def get_mz_runner_pos(self):
        """
        Returns the current position of the player.

        Returns:
            tuple: The current position of the player.

        """
        return self._mz_runner_pos

    def move(self, direction):
        """
        Moves the player inside the playground based on the given direction.

        Args:
            direction (str): The direction in which the player is moving.

        Returns:
            list: A list containing the potential move coordinates.

        """
        self.potential_move = []
        if direction == 'w':
            self.potential_move=[self._mz_runner_pos[0]-1,self._mz_runner_pos[1]]
        elif direction =="s":
            self.potential_move=[self._mz_runner_pos[0]+1,self._mz_runner_pos[1]]
        elif direction =="a":
            self.potential_move=[self._mz_runner_pos[0],self._mz_runner_pos[1]-1]
        elif direction =='d':
            self.potential_move=[self._mz_runner_pos[0],self._mz_runner_pos[1]+1]
        else:
            pass
        return self.potential_move
