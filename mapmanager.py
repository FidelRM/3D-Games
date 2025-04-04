# write the code for creating and managing the map here
class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ]
        self.startNew()
    def startNew(self):
        self.land = render.attachNewNode ('Land')
    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadLand(self, filename):
        self.clear()
        with open(filename)as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z in range(int(z)+1):
                        block = self.addBlock((x, y, z))
                    x += 1
                y += 1
                
