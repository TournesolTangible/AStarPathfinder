
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
                
                # one tile has 4 values, (x,y) of top left and (x,y) of bottom right
                self.pyList.append( [tileX, tileY, tileX+tileLength, tileY+tileLength] )
                tileX += int(tileLength)
                tileNum += 1

            tileY += int(tileLength)
            tileX = 0
        

    # returns the list item for a given coordinate
    def getTileListItem(self, xy) -> []:
        
        x = xy[0]
        y = xy[1]

        for i in self.pyList:
            if x >= i[0] and x <= i[2]:
                if y >= i[1] and y <= i[3]:
                    return i
        return 
