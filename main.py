#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment_7 Maze Runner

Author(s): Alireza Iranmanesh
Group: 63
"""
import Gamecontroller as gcntrl
import Mazerunner






if __name__=='__main__':
	another_round=True
	while another_round:
		# welcoming message and setting game mode and difficulty
		print('__________________________\n'+'Welcome To The Maze Runner \n')
		try:
			game_mode = input('Singleplay or Multiplay?\nPlease enter "s" for singleplay and "m" for multiplay: ').lower()
			if game_mode not in ['s','m']:
				raise ValueError
		except ValueError:
			print('PLEASE ENTER THE CORRECT INPUT: "s" for singleplay "m for multiplay"')
			continue

		try:
			difficulty = int(input(
				'-----------------\n'+'Alright, Choose a level of difficulty;\nEasy Medium Hard ?\nEnter "0" "1" or "2": '
				))
			if difficulty not in [0,1,2]:
				raise IndexError
		except IndexError:
			print('PLEASE ENTER A CORRECT DIFFICULTY LEVEL: 0 , 1 OR 2')
			continue
		except ValueError:
			print('PLEASE ENTER A NUMBER ')
			continue
		# instanciating game with game controller class 
		if(game_mode=='s'):
			# single play mode of game
			player_1 = Mazerunner.Mazerunner(input('What Your Name? '))
			Game_1 = gcntrl.Gamecontroller(player_1,difficulty)
			Game_1.start_game()
		if(game_mode=='m'):
			# multiplayer mode of the game
			player_1 = Mazerunner.Mazerunner(input('Player 1 name : '))
			player_2 = Mazerunner.Mazerunner(input('Player 2 name : '))
			multigame = gcntrl.MultiGameController([player_1,player_2],difficulty)
			multigame.start_game()	
		if input('Want to play another round [Y/N] :').lower()=='y':
			another_round =True
			continue
		another_round=False
