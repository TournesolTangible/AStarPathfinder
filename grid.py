from node import *

class Grid:

    # A Grid class will contain a list of all tiles in the grid
    #
    # Each tile is a list item containing 4 coordinates as the "value"
    # For example: 
    #               
    #

    def __init__(self, x, y, sizeOfWindow):
        self.rows = x
        self.cols = y
        self.size = sizeOfWindow
        self.pyList = []

        tileX = 0
        tileY = 0

        tileNum = int(0)

        tileLength = self.size // self.rows

        for i in range(self.rows):

            for j in range(self.cols):
                
                # one node has 7 values: f, g, h, and (x,y) of top left and (x,y) of bottom right
                node = aNode(0, 0, 0, tileX, tileY, tileX+tileLength, tileY+tileLength, None)
                self.pyList.append( node )
                tileX += int(tileLength)
                tileNum += 1

            tileY += int(tileLength)
            tileX = 0
        

    # returns the list item for a given coordinate
    def getTileListItem(self, xy) -> []:
        
        x = xy[0]
        y = xy[1]

        for i in self.pyList:
            if x >= i.getX() and x <= i.getW():
                if y >= i.getY() and y <= i.getZ():
                    return i
        return 

    
    # Traversal Methods ###################################################
    #
    # Used to return one of the nodes in any of the 8 directions
    def getUpLeftNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) - self.rows - 1]
        except IndexError:
            print("Warning - index of 'Up Left Node' is out of bounds") 
    def getUpRightNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) - self.rows + 1]
        except IndexError:
            print("Warning - index of 'Up Right Node' is out of bounds")
    def getDownRightNode(self, currentNode) -> aNode:
        try:    
            return self.pyList[self.pyList.index(currentNode) + self.rows + 1]
        except IndexError:
            print("Warning - index of 'Down Right Node' is out of bounds")
    def getDownLeftNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) + self.rows -1]
        except IndexError:
            print("Warning - index of 'Down Left Node' is out of bounds")
    def getDownNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) + self.rows]
        except IndexError:
            print("Warning - index of 'Down Node' is out of bounds")
    def getUpNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) - self.rows]
        except IndexError:
            print("Warning - index of 'Up Node' is out of bounds")
    def getLeftNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) - 1]
        except IndexError:
            print("Warning - index of 'Left Node' is out of bounds")
    def getRightNode(self, currentNode) -> aNode:
        try:
            return self.pyList[self.pyList.index(currentNode) + 1]
        except IndexError:
            print("Warning - index of 'Right Node' is out of bounds")
    
    