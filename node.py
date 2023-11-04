import math

class aNode:

    # A Node is used to represent each of the possible spaces in the map

    def __init__(self, fCost, gDist, hDist, x, y, w, z, parentNode):

        self.f = fCost   # The cost to get to the this node in particular
        self.g = gDist   # The distance from the first node to this node
        self.h = hDist   # The estimated distance from this node to the end node

        self.x = x   # x of the node's top left coordinate
        self.y = y   # y of the node's top left coordinate
        self.w = w   # x of the node's bottom right coordinate
        self.z = z   # y of the node's bottom right coordinate

        self.parent = parentNode   # the node that was visited immediately before this one
    
    def setParent(self, parentNode):
        self.parent = parentNode
    
    def getParent(self):
        try:
            return self.parent
        except Exception:
            print(f"The current node, '{self}' has no parent set.")

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
    def setF(self):
        self.f = self.getG() + self.getH()
    
    def getG(self):
        return self.g
    def setG(self, newG):
        self.g = newG
    
    def getH(self):
        return self.h
    
    # Set the relative distance from current node to target node (xy)
    def setH(self, xy):
        # Dist = max(abs(x2-x1), abs(y2-y1))

        print(f"{xy[1].getX()} - {xy[0].getX()}")
        print("\n")
        print(f"{xy[1].getY()} - {xy[0].getY()}")

        self.h = math.sqrt((xy[1].getX() - xy[0].getX())**2 + (xy[1].getY() - xy[0].getY())**2)

        # self.h = max( abs(xy[1].getX() - xy[0].getX()), abs(xy[1].getY() - xy[0].getY()) )
