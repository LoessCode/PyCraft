class Player():
    def __init__(self):
        self.pos = [4, 4]

        #Player Inventory Dict
        self.inv = {
            "matRaw": [],
            "toolRock": [],
            "toolSplit": [],
            "toolHurt": []
        }

        self.tex = "Data/Assets/Entity/Player.png"
        self.pane = (0, 0)

    def setPos(self, pos, pane = 0):
        self.pos = pos
        self.pane = (self.pane if pane == 0 else pane)