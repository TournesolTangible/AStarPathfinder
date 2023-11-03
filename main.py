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
def redraw(window, selectedTiles, startAndEndTiles, testTiles):
    global size, rows

    # fill window with black 
    window.fill(BLACK)
    drawGrid(window, size, rows)

    # fill in tiles that have been selected
    drawSelectedTiles(window, selectedTiles)

    # fill in tiles that are start/ends
    drawStartAndEndTiles(window, startAndEndTiles)

    # fill in the test tiles (testing purposes)
    drawTestTiles(window, testTiles)

    # update display
    pygame.display.update()

# Draws the selected tiles in GRAY
def drawSelectedTiles(window, tiles):
    for tile in tiles:
        pygame.draw.rect(window, GRAY, pygame.Rect(tile.x, tile.y, getTileSize(), getTileSize()))

def drawStartAndEndTiles(window, tiles):
    for tile in tiles:
        pygame.draw.rect(window, WHITE, pygame.Rect(tile.x, tile.y, getTileSize(), getTileSize()))

def drawTestTiles(window, tiles):
    for tile in tiles:
        pygame.draw.rect(window, GREEN, pygame.Rect(tile.x, tile.y, getTileSize(), getTileSize()))

# Defines tile size based on size of window and number of rows
def setTileSize(size, rows):
    global tileSize
    tileSize = size // rows

def getTileSize():
    return tileSize

def findSmallestFValue(list) -> aNode:
    smallestF = 100000.0
    for item in list:
        if item.getF() < smallestF:
            smallestFNode = item
    return smallestFNode

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

    running = True   # Used to keep the program running
    ready = False    # Used to start the A* pathfinding
    testing = False  # Used to start testing 

    # create the grid
    createGridModel()

    # create a list for tiles that are 'selected' by the user
    selectedTiles = []

    # create a list for 'start' and 'end' tiles
    startAndEndTiles = []

    # create a list for 'test' tiles
    testTiles = []

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
                # if gridModel.getTileListItem(mousePos) in selectedTiles and gridModel.getTileListItem(mousePos) not in startAndEndTiles:
                #     selectedTiles.remove(gridModel.getTileListItem(mousePos))

                # # If tile unselected  ->  select it
                # else:
                    selectedTiles.append(gridModel.getTileListItem(mousePos))

            # Handle Right Click (selecting start and end node)
            if state == (False, False, True):
                    if gridModel.getTileListItem(mousePos) in startAndEndTiles and gridModel.getTileListItem(mousePos) not in selectedTiles:
                        startAndEndTiles.remove(gridModel.getTileListItem(mousePos))
                    else:
                        startAndEndTiles.append(gridModel.getTileListItem(mousePos))
            
            # Handle Space input ( Run tests ) 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    testing = True

            if len(startAndEndTiles) > 1:
                ready = True
                startAndEnd = (startAndEndTiles[0], startAndEndTiles[1])


            # MAIN PATHFINDING CODE HERE ###################
            #
            if ready == True:
                # initialize lists
                openList = []
                closedList = []

                # add the starting node
                openList.append(startAndEndTiles[0])
                print(openList)
                # loop until end is found
                while len(openList) > 0:
                    
                    # get current node
                    currentNode = findSmallestFValue(openList)
                    openList.remove(currentNode)
                    closedList.append(currentNode)

                    # if end found
                    if currentNode == startAndEndTiles[1]:
                        # #############################################################   backtrack to get the path  #####
                        print("success!")
                    # else, generate children
                    else:

                        pass

            # run tests
            if testing == True:
                
                # test 1
                # checking the node movements  ->  should paint a green square one node above the current node
                currentNode = startAndEndTiles[0]
                upNode = gridModel.getUpNode(currentNode)
                testTiles.append(upNode)
                


#     // Found the goal
#     if currentNode is the goal
#         Congratz! You've found the end! Backtrack to get path
#     // Generate children
#     let the children of the currentNode equal the adjacent nodes
    
#     for each child in the children
#         // Child is on the closedList
#         if child is in the closedList
#             continue to beginning of for loop
#         // Create the f, g, and h values
#         child.g = currentNode.g + distance between child and current
#         child.h = distance from child to end
#         child.f = child.g + child.h
#         // Child is already in openList
#         if child.position is in the openList's nodes positions
#             if the child.g is higher than the openList node's g
#                 continue to beginning of for loop
#         // Add the child to the openList
#         add the child to the openList

        redraw(window, selectedTiles, startAndEndTiles, testTiles)
    
    pygame.quit()

if __name__ == "__main__":
    main()