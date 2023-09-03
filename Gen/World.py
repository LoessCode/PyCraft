class World():

    def __init__(self):
        self.World = {}

    class Pane():
        def __init__(self, tiles, pos):
            self.pos = pos
            self.Tiles = tiles

    class Tile():
        def __init__(self, tile, pos):
            self.Tile = tile
            self.pos = pos
    
    #WorldManipulation functions

    def AddPane(self, pane):
        #Adds a pane to the World. Used by WorldGen
        key = str(pane.pos)[1:-1]
        self.World[key] = pane

