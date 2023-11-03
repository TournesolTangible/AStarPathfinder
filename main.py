import pygame
import random
from grid import *

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def drawGrid(window, size, rows):

    # Takes window, size, and number of rows to draw gridlines on window
    distanceBetweenRows = size // rows
    x = 0
    y = 0
    for l in range(rows):
        x += distanceBetweenRows
        y += distanceBetweenRows
        pygame.draw.line(window, WHITE, (x, 0), (x, size))
        pygame.draw.line(window, WHITE, (0, y), (size, y))

# Creates the global 'gridModel' which stores the coordinates for each grid tile
def createGridModel():
    global gridModel
    gridModel = Grid(rows, rows, size)

# Redraws the entire model
def redraw(window, selectedTiles, startAndEndTiles):
    global size, rows

    # fill window with black 
    window.fill(BLACK)
    drawGrid(window, size, rows)

    # fill in tiles that have been selected
    drawSelectedTiles(window, selectedTiles)

    # fill in tiles that are start/ends
    drawStartAndEndTiles(window, startAndEndTiles)

    # update display
    pygame.display.update()

# Draws the selected tiles in GRAY
def drawSelectedTiles(window, tiles):
    for tile in tiles:
        pygame.draw.rect(window, GRAY, pygame.Rect(tile[0], tile[1], getTileSize(), getTileSize()))

def drawStartAndEndTiles(window, tiles):
    for tile in tiles:
        pygame.draw.rect(window, RED, pygame.Rect(tile[0], tile[1], getTileSize(), getTileSize()))

# Defines tile size based on size of window and number of rows
def setTileSize(size, rows):
    global tileSize
    tileSize = size // rows

def getTileSize():
    return tileSize


## MAIN PROGRAM STARTS HERE ############################
#
#
def main():
    # Starter variables
    global size, rows
    size = 800
    rows = 40
    setTileSize(size, rows)

    # window definition
    window = pygame.display.set_mode((size, size))

    running = True

    # create the grid
    createGridModel()

    # create a list for tiles that are 'selected' by the user
    selectedTiles = []

    # create a list for 'start' and 'end' tiles
    startAndEndTiles = []

    # Main loop execution
    while running: 

        # Event handling   
        for event in pygame.event.get():      
            if event.type == pygame.QUIT:
                running = False

            # Get mouse inputs
            state = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()

            # Handle Left Click (selecting tiles)
            if state == (True, False, False):

                # # If tile selected  ->  unselect it
                # if gridModel.getTileListItem(mousePos) in selectedTiles:
                #     selectedTiles.remove(gridModel.getTileListItem(mousePos))

                # # If tile unselected  ->  select it
                # else:
                    selectedTiles.append(gridModel.getTileListItem(mousePos))

            # Handle Right Click (selecting start and end node)
            if state == (False, False, True):
                
                # If tile already selected  ->  unselect it and make it into a start/end
                if gridModel.getTileListItem(mousePos) in selectedTiles:
                    print("getting through")
                    selectedTiles.remove(gridModel.getTileListItem(mousePos))
                    startAndEndTiles.append(gridModel.getTileListItem(mousePos))

                

        redraw(window, selectedTiles, startAndEndTiles)
    
    pygame.quit()

if __name__ == "__main__":
    main()