import sys
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
			for cell in faction.cells:

				if cell.alive:
					for x in range(cell.x, cell.x+cell.size):
						for y in range(cell.y, cell.y+cell.size):
							win.set_at((x, y), faction.color())

					cell.move(map, win)

					if cell.counter == 0:
						faction.reproduce(cell, self.mutationRange, self.mutationChance)
						cell.counter = cell.reproTick

				else:
					faction.cells.remove(cell)

	def textHollow(self, font, message, fontcolor):
		notcolor = [c^0xFF for c in fontcolor]
		base = font.render(message, 0, fontcolor, notcolor)
		size = base.get_width() + 2, base.get_height() + 2
		img = pygame.Surface(size, 16)
		img.fill(notcolor)
		base.set_colorkey(0)
		img.blit(base, (0, 0))
		img.blit(base, (2, 0))
		img.blit(base, (0, 2))
		img.blit(base, (2, 2))
		base.set_colorkey(0)
		base.set_palette_at(1, notcolor)
		img.blit(base, (1, 1))
		img.set_colorkey(notcolor)
		return img

	def textOutline(self, font, message, fontcolor, outlinecolor):
		base = font.render(message, 0, fontcolor)
		outline = self.textHollow(font, message, outlinecolor)
		img = pygame.Surface(outline.get_size(), 16)
		img.blit(base, (1, 1))
		img.blit(outline, (0, 0))
		img.set_colorkey(0)
		return img

	def printLegend(self, win):
		legend = ''
		txtHeight = 0
		for faction in self.factions:
			text = 'Population: ' + str(len(faction.cells))
			#textsurface = myfont.render(text, True, faction.facCol)
			#win.blit(textsurface,(0,textY))
			textL = self.textOutline(myfont, text, faction.color(), (255,255,255))
			win.blit(textL, (0, txtHeight))
			txtHeight = txtHeight + 20

pygame.init()
win = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Generations")

worldMap = pygame.image.load("map1.png")
worldMap = pygame.transform.scale(worldMap, (600, 480))
rect = worldMap.get_rect()
rect = rect.move((0, 0))

pygame.font.init() 
myfont = pygame.font.SysFont('Arial', 30)


if __name__ == "__main__":

	world = World("config.txt")
	run = True
	while run:

		pygame.time.delay(100)
		
		win.blit(worldMap, rect)
		world.printLegend(win)
		world.update(worldMap)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()
