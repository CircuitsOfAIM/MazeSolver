#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment_7 Maze Runner

Author(s): Alireza Iranmanesh
Group: 63
"""
import time
import Playground as plg
import Mazerunner 


# This constant is set to terminate the game after 10 hours or if the user quit the game before it finishes
MAX_TIME = 36000


class Gamecontroller(object):
	'''runs the single play game and keep track of game configurations'''

	def __init__(self,player,level):
		"""
		Instanciates gamecontroller

		Arguments:
		player (Mazerunner): player of the game in single play mode.
		level (int): specified level of difficulty of the game.

		"""
		self.level = level
		self.player =player


	def start_game(self):
		"""
		Creates game by creating playground ,puts player valid move on playground
		and terminates the game when player reaches destination

		Returns:
		string : a 'done' message when user reaches destination

		"""

		#Building maze playground
		maze = plg.Playground(self.level,self.player)
		print(maze)
		print(self.player.name)

		# Geting user input and move the player inside the maze playground
		while not self.is_gameover(maze,self.player):
			try:
				user_move_inpt = input('Run!\nUse "W","S","A","D" or "E" for exit:').lower()
				if(user_move_inpt=='e'):
					break
				potential_move = self.player.move(user_move_inpt)

				#checking if the move is valid
				if self.is_valid_move(maze,potential_move):
					maze.set_player_pos(potential_move,self.player)
					print(maze)
			except:
				print('Please Enter Correct Input (W,S,A or D)\n------------------')
			continue

		# Checks if the game is over 
		if self.is_gameover(maze,self.player):
			print('Welldone! YOU WON :)')
			return 'done' 


	def is_valid_move(self,maze,pos):
		"""
			Checks player move not to bump into wall,
		   	if not asks user to insert the correct.

		   	Arguments:
		   	maze (Playground) : playgournd object created by start_game()
		   	pos (list): player position in row (index 0) and column (index 1)

		   	Returns:
		   	(Bool) : True if player's intented move is valid False if it is wall.

		"""
		return True if maze.get_pos_status(pos)==' ' else print('This is Wall.Try another Move ')


	def is_gameover(self,maze,player):
		"""
		Checks wether the players arrived at the destination

		Arguments:
		maze (Playground):Playground object created by start_game()
		player (Mazerunner) : player object of the game

		Returns:
		(Bool) : True if player position is same as destination position False if not

		"""
		mzrunner_pos= player.get_mz_runner_pos()
		dest_pos= maze.get_destination_location()
		return True if (mzrunner_pos[0]==dest_pos[0]) and (mzrunner_pos[1]==dest_pos[1]) else False


class MultiGameController(Gamecontroller):
	'''
	Game controller for multiplayer mode of the game

	Arguments:
	(Gamecontroller) : inherits from Gamecontroller class

	'''

	def __init__(self,player,level):
		'''
		Overwrites __init__ of the parent class Gamecontroller

		Arguments:
		player (list) : list of Mazerunner objects (player) of the game
		level (int) : level of difficulty

		'''
		super().__init__(player,level)
		self.player = player
		self.score = []


	def winner_player(self,scorelist):
		"""
		Determines winner based on player spent less time to solve maze
		
		Arguments:
		scorelist (list): list of dictionaries with player and scores key value pairs

		Returns:
		(string): message of winner of the game or there is no winner

		"""
		_scorels=[]
		for dic in scorelist:
				_scorels.append(list(dic.values()))		
		if min(_scorels)==[MAX_TIME]:
			return 'THERE IS NO WINNER'
		return f'{list(scorelist[_scorels.index(min(_scorels))].keys())[0].get_name()} IS WINNER !'


	def calculate_time(self,game):
		"""
		Calculats time player spent to solve the maze

		Arguments:
		game (Method) : start_game() method of the game

		Returns:
		(int): Spent time by user 

		"""
		start_time = time.time()
		status=game()
		end_time = time.time()

		#To control users quit during game Max_Time will be set when user quits game
		return end_time - start_time if status=='done' else MAX_TIME


	def start_game(self):
		"""
		Overwrites sart_game method to run for each player
		
		"""
		for pl in self.player:
			self.player = pl
			self.score.append({pl:self.calculate_time(super().start_game)})
		print(self.winner_player(self.score))
			
