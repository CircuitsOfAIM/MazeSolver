#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment_7 Maze Runner

Author(s): Alireza Iranmanesh
Group: 63
"""
import random
class RandomizedPrims(object):
	'''
		Builds a maze playground based on Randomized Prims algorithm
	'''
	def __init__(self,level):
		'''
			Instantiate algorithm

			Args:
			level (int): levels of difficulty
		'''
		LEVELS = [(19,19),(39,39),(69,39)]
		self.l_width,self.l_height = LEVELS[level]
		self.playground = [[{'status':'#','coordinate':(i,j)} for j in range(self.l_width)] for i in range(self.l_height)]
		self.walls_neighbours=[]
		self.entrance = self.playground[len(self.playground)-2][0]        
		self.start_point =self.playground[len(self.playground)-2][1]
		self.destination = self.playground[1][len(self.playground[0])-1]
		self.finish_point =self.playground[1][len(self.playground[0])-2]
		self.entrance['status'],self.destination['status'],self.start_point['status'],self.finish_point['status']=' ',' ',' ',''
		self.build_maze()

	def get_neighbours(self,cell):
	    """
	    Get the neighbours of the passed cell.

	    Args:
	    cell (dict) : a dictionary consisting status and coordinate for each index of playground list

	    Returns:
	    neighbours (list): list of neighbouring cells in each direction 
	    """
	    i, j = cell['coordinate']
	    neighbours = []
	    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
	        ni, nj = i + di, j + dj
	        if 0 < ni < len(self.playground)-1 and 0 < nj < len(self.playground[0])-1	:
	            neighbour = self.playground[ni][nj]
	            neighbours.append(neighbour)
	    return neighbours

	def build_maze(self):
		'''
			Builds maze based on algorithm

			Returns:
			playground(list) : the 2D list of all location dictionaries
		'''
		self.walls_neighbours+=self.get_neighbours(self.start_point)
		while self.walls_neighbours:
			self.random_wall = self.walls_neighbours[random.randint(0,len(self.walls_neighbours)-1)]
			self.random_wall_neighbours = self.get_neighbours(self.random_wall)
			wall_counter = 0
			n=None
			for n in self.random_wall_neighbours:
				if n['status']==' ':
					wall_counter+=1
					n = n
			if(wall_counter==1):
				self.random_wall['status']=' '
				rw_i , rw_j = self.random_wall['coordinate']
				n_i , n_j = n['coordinate']
				new_cell_i,new_cell_j = rw_i,rw_j
				if  0 < new_cell_i < len(self.playground)-1 and 0 < new_cell_j < len(self.playground[0])-1	:
					if (rw_i == n_i):
						new_cell = self.playground[rw_i][new_cell_j]
					elif(rw_j==n_j):
						new_cell = self.playground[new_cell_i][rw_j]
					new_cell['status']=' '	
					self.walls_neighbours+=self.get_neighbours(new_cell)
			self.walls_neighbours.remove(self.random_wall)
		self.finish_point['status']=' '
		return self.playground
