from cell import Faction
from cell import Cell
from cell import *


class World:
	def __init__(self, config):
		with open(config, "r") as config:
			self.numFactions = int( config.readline() )
			self.factions = []
			self.mutationRange = 0
			self.mutationChance = 0
			print(self.numFactions)
			word = ''

			for fac in range(0, self.numFactions):
				rules = [] # rules[0] = color, rules[1] = strength, rules[2] = reprTick, rules[3] = loc
				line = config.readline()
				for char in line:
					if char.isspace():
						rules.append( eval(word) )
						word  = ''
					elif not char.isspace():
						word += char

				self.factions.append( Faction(rules[0], rules[1], rules[2], rules[3]) )
				print(rules)

			self.mutationRange = eval(config.readline())
			self.mutationChance = eval(config.readline())
			

		print(self.factions)
		print(self.mutationRange)
		print(self.mutationChance)
		

	def update(self, map):

		for faction in self.factions:

			#text = 'Population: ' + str(len(faction.cells))
			#textsurface = myfont.render(text, True, (255, 255, 255))

			for cell in faction.cells:

				if cell.alive:
					pygame.draw.rect(win, cell.color, (cell.x, cell.y, cell.size, cell.size) )

					#if tuple(surface.get_at( (cell.x, cell.y) )) == (255,0,0):
					#print(tuple(win.get_at( (cell.x, cell.y) )))
					
					cell.move(map)

					if cell.counter == 0:
						cell.color = GREEN
						cell.counter = cell.reproTick
						faction.reproduce(cell, self.mutationRange, self.mutationChance)
				else:
					faction.cells.remove(cell)

			#win.blit(textsurface,(0,0))	


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

pygame.init()
win = pygame.display.set_mode((600, 480))
worldMap = pygame.image.load("map1.png")
worldMap = pygame.transform.scale(worldMap, (600, 480))
rect = worldMap.get_rect()
rect = rect.move((0, 0))
pygame.display.set_caption("Generations")
pygame.font.init() 
myfont = pygame.font.SysFont('Calibri', 20)

if __name__ == "__main__":

	world = World("config.txt")

	run = True
	while run:

		pygame.time.delay(100)
		#win.fill((0,0,0))
		win.blit(worldMap, rect)

		world.update(worldMap)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()
