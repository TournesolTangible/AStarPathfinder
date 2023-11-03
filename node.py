
class aNode:

    # A Node is used to represent each of the possible spaces in the map

    def __init__(self, fCost, gDist, hDist, x, y, w, z):

        self.f = fCost   # The cost to get to the this node in particular
        self.g = gDist   # The distance from the first node to this node
        self.h = hDist   # The estimated distance from this node to the end node

        self.x = x   # x of the node's top left coordinate
        self.y = y   # y of the node's top left coordinate
        self.w = w   # x of the node's bottom right coordinate
        self.z = z   # y of the node's bottom right coordinate

    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getW(self):
        return self.w
    
    def getZ(self):
        return self.z
    
    def getF(self):
        return self.f
    def setF(self, newF):
        self.f = newF
    
    def getG(self):
        return self.g
    def setG(self, newG):
        self.g = newG
    
    def getH(self):
        return self.h
    def setH(self, newH):
        self.h = newH