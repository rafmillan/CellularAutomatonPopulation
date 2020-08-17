#Generations
---
#####config:
*(see config.txt)*
```
    Num of Factions -> 1 to 8
    fac1 -> Color, (minStr, maxStr) (minRepr, maxRepr) (x, y)
    ...
    facN -> Color (minStr, maxStr) (minRepr, maxRepr) (x, y)
    mutation -> (-1.0, 1.0)
    mutationChance -> 0.0 to 1.0
    disease -> 1:YES | 0:NO
```
---
#####Rules:
- Each cell has the following:
    - Age
    - Strength
    - Reproduction Value
    - Faction Color
    - Sick (T/F)

- Place FACTIONS across Map

- Simulation Begins
 - Each Turn:
    - Age increases
    - Reproduction Ticker decreases
    - Cell can either move N, NE, E, SE, S SW, W or NW
        - If theres water, cell stays put.
     - If Reproduction Ticker == 0
        - Reproduction Ticker resets to Reproduction Value 
        - Cell reproduces
            - Child inherits parents Strength and Reproduction Value
---
    


#####To-Do:
-  Add mutations
-  Add Disease
    - Each move, Cell has a 10% chance of developing a disease, if cell is sick and reproduces child has 50% chance of being born sick. If cell is sick each move it has a 10% chance of recovering
    - Disease cuts cells strength by 1/3 (could be modified by config file)
- Add Zoom in/Zoom out functionality to map
- Cell battles
- Placeable factions with mouse
- Water Travel
- ~~Faction Legend~~
---
**Colors:**

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


---
######Throwaway
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

