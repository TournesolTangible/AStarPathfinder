import pygame
# python -m pip install pyautogui
import pyautogui
from grid import *
from time import sleep

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

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
def redraw(window, selectedTiles, startAndEndTiles, testTiles, openTiles):
    global size, rows

    # fill window with black 
    window.fill(BLACK)
    drawGrid(window, size, rows)

    # fill in tiles that have been selected in GRAY
    drawSelectedTiles(window, selectedTiles)

    # fill in tiles that are start/ends in WHITE
    drawStartAndEndTiles(window, startAndEndTiles)

    # fill in the test tiles in GREEN (testing purposes)
    drawTestTiles(window, testTiles)

    # fill the open tiles in RED 
    drawOpenTiles(window, openTiles)

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

def drawOpenTiles(window, tiles):
    for tile in tiles:
        pygame.draw.rect(window, YELLOW, pygame.Rect(tile.x, tile.y, getTileSize(), getTileSize()))

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

def clearAllLists(listOfLists):
    for list in listOfLists:
        list.clear()

# Set parentNode to be parent of all adjacent nodes that are not closed off
def setAllAdjacentChildren(parentNode, closedList) -> []:
    listOfChildren = gridModel.getAllAdjacentNodes(parentNode)
    for node in listOfChildren:
        if node not in closedList:
            node.setParent(parentNode)
            pass

    return listOfChildren


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
    pygame.display.set_caption('A* Pathfinding Tool')

    running = True   # Used to keep the program running
    ready = False    # Used to start the A* pathfinding
    testing = False  # Used to start testing
    endFound = False # Used to stop program once finished

    # create the grid
    createGridModel()

    # create a list for tiles that are 'blocked' by the user
    blockedTiles = []

    # create a list for 'start' and 'end' tiles
    startAndEndTiles = []

    # create a list for 'test' tiles
    testTiles = []

    # for tiles that may be 'traversed'
    openList = []     

    # for tiles that may not be 'traversed        
    closedList = []

    # the final path that has the shortest length of nodes from start to end tile
    path = []

    pyautogui.alert('Draw "blocking" tiles with left mouse click\nDraw "Start" and "End" tiles using right mouse click\nThe board may be cleared with the "c" key', "A* Pathfinding") 
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
                blockedTiles.append(gridModel.getTileListItem(mousePos))

            # Handle Right Click (selecting start and end node)
            if state == (False, False, True):
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if gridModel.getTileListItem(mousePos) in startAndEndTiles and gridModel.getTileListItem(mousePos) not in blockedTiles:
                            startAndEndTiles.remove(gridModel.getTileListItem(mousePos))
                        else:
                            startAndEndTiles.append(gridModel.getTileListItem(mousePos))
                
            # Handle Space input ( Run tests )  or 'c' input ( Clear lists, fresh board )
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    testing = True
                elif event.key == pygame.K_c:
                    clearAllLists([blockedTiles, startAndEndTiles, testTiles, openList, closedList])
                    ready = False
                    endFound = False

            # Handle start and end placed ( Begin search algorithm )
            if len(startAndEndTiles) > 1 and endFound == False:
                ready = True
                startAndEnd = (startAndEndTiles[0], startAndEndTiles[1])


            # MAIN PATHFINDING CODE HERE #########################################
            #
            if ready == True:               

                # set startNode to starting tile and initialize g, h, f values
                startNode = startAndEnd[0]
                startNode.setG(0)
                startNode.setH(startAndEnd)

                # add the starting node
                openList.append(startNode)
                
                # loop until end is found
                while len(openList) > 0 and endFound == False:

                    # get current node
                    currentNode = openList[0]
                    currentIndex = 0
                    for index, item in enumerate(openList):
                        if item.getF() < currentNode.getF():
                            item.setParent(currentNode)
                            currentNode = item
                            currentIndex = index

                    openList.pop(currentIndex)
                    closedList.append(currentNode)

                    # if end found
                    if currentNode == startAndEnd[1]:
                        current = currentNode
                        while current != startAndEnd[0]:
                            path.append(current)
                            current = current.getParent()
                            for item in path:
                                print(item)
                            break
                    
                    # else, generate list of 'unblocked' children
                    else:
                        children = setAllAdjacentChildren(currentNode, blockedTiles)
                    for child in children:
                        if child:
                            # ignore if child in closedList (not traversable)
                            if child in closedList or child in blockedTiles:
                                pass

                            # if not in openList, add it to openList and initialize g, h, f values
                            elif child not in openList:
                                openList.append(child)
                                child.setG(child.getParent().getG()+1)
                                nodePair = [child, startAndEnd[1]]
                                child.setH(nodePair)
                                child.setF()

                            # if child in openList  ->  check if it has a lower g value (more efficient path)   
                            elif child in openList:
                                if child.getG() < currentNode.getG():
                                    #child.setParent(currentNode)
                                    child.setG(child.getParent().getG()+1)
                                    nodePair = [child, startAndEnd[1]]
                                    child.setH(nodePair)
                                    child.setF()

                        if startAndEnd[1] in closedList or currentNode == startAndEnd[1]:
                            ready = False
                            endFound = True
                            break

                    redraw(window, blockedTiles, startAndEndTiles, testTiles, openList)
                    sleep(0.1)
                
                # execution goes here after found
                     

            # Run tests ##########################################################
            #
            if testing == True and len(startAndEndTiles) > 0:
                
                # test 1
                # checking the node movements  ->  should paint a green square one node above the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getUpNode(currentNode)
                testTiles.append(testNode)

                # test 2
                # checking the node movements  ->  should paint a green square one node above and to the right of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getUpRightNode(currentNode)
                testTiles.append(testNode)

                # test 3
                # checking the node movements  ->  should paint a green square one node to the right of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getRightNode(currentNode)
                testTiles.append(testNode)

                # test 4
                # checking the node movements  ->  should paint a green square one node to the right and down of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getDownRightNode(currentNode)
                testTiles.append(testNode)

                # test 5
                # checking the node movements  ->  should paint a green square one node down of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getDownNode(currentNode)
                testTiles.append(testNode)

                # test 6
                # checking the node movements  ->  should paint a green square one node down and to the left of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getDownLeftNode(currentNode)
                testTiles.append(testNode)
                
                # test 7
                # checking the node movements  ->  should paint a green square one node to the left of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getLeftNode(currentNode)
                testTiles.append(testNode)

                # test 8
                # checking the node movements  ->  should paint a green square one node to the left and up of the current node
                currentNode = startAndEndTiles[0]
                testNode = gridModel.getUpLeftNode(currentNode)
                testTiles.append(testNode)

        redraw(window, blockedTiles, startAndEndTiles, testTiles, openList)

    pygame.quit()


if __name__ == "__main__":
    main()