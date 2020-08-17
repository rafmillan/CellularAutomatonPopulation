#Generations

**config:**
*(see config.txt)*
```
    Num of Factions -> 1 to 8
    fac1 -> Color, (minStr, maxStr) (minRepr, maxRepr) (x, y)
    ...
    facN -> Color (minStr, maxStr) (minRepr, maxRepr) (x, y)
    mutation -> (-1.0, 1.0)
    mutationChance -> 0.0 to 1.0
    sickness -> 1:YES | 0:NO
```


**COLORS:**

RED = (255,0,0)\
BLUE = (0,0,255)\
GREEN = (0,255,0)\
YELLOW = (255,255,0)\
MAGENTA = (255,0,255)\
CYAN = (0,255,255)\
ORANGE = (255,165,0)\
PURPLE = (128,0,128)\
WHITE = (255,255,255)\
BLACK = (0,0,0)

#####TODO:
- [ ] Add mutations
- [ ] Add Zoom in/Zoom out functionality to map
- [ ] Cell battles
- [ ] Placeable factions with mouse
- [ ] Water Travel
- [x] Faction Legend

####Throwaway
```
for faction in self.factions:
    for cell in faction.cells:

        if cell.alive:
            #pygame.draw.rect(win, cell.color, (cell.x, cell.y, cell.size, cell.size) )	
            for x in range(cell.x, cell.x+cell.size):
                for y in range(cell.y, cell.y+cell.size):
                    worldMap.set_at((x, y), faction.color())
            
            prevX = cell.x
            prevy = cell.y
            cell.move(map)
            
            for x in range(prevX, prevX+cell.size):
                for y in range(prevY, prevYy+cell.size):
                    worldMap.set_at((prevx, y), faction.color())


            if cell.counter == 0:
                cell.color = GREEN
                cell.counter = cell.reproTick
                faction.reproduce(cell, self.mutationRange, self.mutationChance)

        else:
            faction.cells.remove(cell)
            #worldMap.set_at((cell.x, cell.y), GREEN)
```

