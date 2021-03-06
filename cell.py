import random
import pygame
from pygame.locals import *
from colour import Color

random.seed()

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Cell:

	size = 2
	vel = 2

	def __init__(self, facCol, stren: tuple, repro: tuple, loc: tuple, sick=None):
		self.age = 0
		self.color = facCol
		self.x = loc[0]
		self.y = loc[1]
		self.strengthRange = stren
		self.reproRange = repro
		self.strength = random.randint(int(stren[0]), int(stren[1]))
		self.reproTick = random.randint(int(repro[0]), int(repro[1]))
		self.counter = self.reproTick

		self.alive = True
		self.isSick = False

		if not sick is None:
			self.isSick = sick

	def kill(self):
		self.alive = False

	def isOccupied(self, win):
		for x in range(0, 600):
			for y in range(0, 480):
				if win.get_at((x, y)) != GREEN:
					return True
				else:
					return False

	def move(self, map, win):
		# TODO maybe change to if spot is not GREEN then kill() instead of not being able to move. 
		dir = random.randint(0,9) #1 - N, 2 - NE,  3 - E, 4 - SE, 5 - S, 6 - SW, 7 - W, 8 - NW
		if dir == 1:# N y-vel
			if self.y > 0 and not map.get_at((self.x, self.y-self.vel) ) == BLUE:
				self.y = self.y-self.vel

				#if not self.isOccupied(win):

		elif dir == 2:# NE x+vel, y-vel
			if self.x < (600-self.size) and self.y > 0 and not map.get_at( (self.x+self.vel+self.size, self.y-self.vel) ) == BLUE:
				self.x = self.x+self.vel
				self.y = self.y-self.vel

				#if not self.isOccupied(win):

		elif dir == 3:# E x+vel
			if self.x < (600-self.size) and not map.get_at( (self.x+self.vel+self.size, self.y) ) == BLUE:
				self.x = self.x+self.vel

				#if not self.isOccupied(win):

		elif dir == 4:# SE x+vel, y+vel
			if self.x < (600-self.size) and self.y < (480-self.size) and not map.get_at( (self.x+self.vel+self.size, self.y+self.vel+self.size) ) == BLUE:
				self.x = self.x+self.vel
				self.y = self.y+self.vel
				
				#if not self.isOccupied(win):

		elif dir == 5:# S y+vel;
			if self.y < (480-self.size) and not map.get_at( (self.x, self.y+self.vel+self.size) ) == BLUE:
				self.y = self.y+self.vel
				
				#if not self.isOccupied(win):

		elif dir == 6:# SW x-vel, y+vel
			if self.y < (480-self.size) and self.x > 0 and not map.get_at( (self.x-self.vel, self.y+self.vel+self.size) ) == BLUE:
				self.x = self.x-self.vel
				self.y = self.y+self.vel
				
				#if not self.isOccupied(win):

		elif dir == 7:# W
			if self.x > 0 and not map.get_at( (self.x-self.vel, self.y) ) == BLUE:
				self.x = self.x-self.vel
				
				#if not self.isOccupied(win):	
		
		elif dir == 8:# NW x-vel, y-vel
			if self.x > 0 and self.y > 0 and not map.get_at( (self.x-self.vel, self.y-self.vel) ) == BLUE:
				self.x = self.x-self.vel
				self.y = self.y-self.vel
				
				#if not self.isOccupied(win):

		self.counter = self.counter - 1;
		self.age = self.age + 1;

		if self.age > self.strength:
			self.kill()

	def attack(self, otherCell):
		if self.strength >= otherCell.strength:
			otherCell.kill()
		else:
			self.kill()

	def getDisease(self, disChance):
		chance = random.random()
		if chance <= 0.1 and not self.isSick:
			self.isSick = True
			self.strength = int(self.strength * (2/3))
		
		if chance <= 0.1 and self.isSick:
			self.isSick = False
			self.strength = int(self.strength  + int(self.strength * 1/3) )
	
class Faction:
	
	def __init__(self, col, strth:tuple, reprt: tuple, loc:tuple):
		self.facCol = col 
		self.facStr = strth
		self.facRepr = reprt
		self.cells = []
		self.population = len(self.cells)

		self.cells.append( Cell(col, strth, reprt, loc) )

	def color(self):
		return self.facCol

	def reproduce(self, parentCell, mutRange: tuple, mutChance):
		chance = random.random()

		if chance <= mutChance: #MUTATE
			mutation = random.uniform(mutRange[0], mutRange[1])
			strengthMutation1 = parentCell.strengthRange[0] * mutation
			strengthMutation2 = parentCell.strengthRange[1] * mutation
			
			newStren = ( int(parentCell.strengthRange[0] + strengthMutation1), int(parentCell.strengthRange[1] * strengthMutation2) )

			reproMutation1 = parentCell.reproRange[0] * mutation
			reproMutation2 = parentCell.reproRange[1] * mutation

			newRepro = ( int(parentCell.reproRange[0] + reproMutation1), int(parentCell.reproRange[1] + reproMutation2) )

		else:
			newStren = parentCell.strengthRange
			newRepro = parentCell.reproRange

		if parentCell.isSick:
			sickChance = random.random()
			if sickChance <= 0.5:
				self.cells.append( Cell(self.facCol, newStren, newRepro, ( parentCell.x, parentCell.y), True) )

		else:
			self.cells.append( Cell(self.facCol, newStren, newRepro, ( parentCell.x, parentCell.y)) )



