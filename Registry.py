import json
import pickle
#
global Tiles, Items, Entities, Save
Tiles = {}; Items = {}; Entities = {}; Save = []

class Item():
    def __init__(self, name, item, tex):
        self.name = name
        self.Item = item
        self.Tex = tex

class Tile():
    def __init__(self, name, tile, tex):
        self.name = name
        self.Tile = tile
        self.tex = tex 

class Player():
    def __init__(self, player, tex):
        self.Player = player
        self.Tex = tex

def RegisterAll():
    #unpackItem()
    unpackTile()

def unpackTile():
    with open(r"Data\Tile\Tile.json", "r") as TileFile:
        TileList = json.load(TileFile)

        for TileKey in TileList:
            FTile = TileList[TileKey]

            tile = json.load(open(str(FTile["path"]), "r"))

            Tiles[TileKey] = Tile(FTile["name"], tile, FTile["tex"])

def unpackItem():
    with open(r"Data\Item\Item.json", "r") as ItemFile:
        ItemList = json.load(ItemFile)

        for ItemKey in ItemList:
            FItem = ItemList[ItemKey]

            item = json.load(open(str(FItem["path"]), "r"))

            Items[ItemKey] = Item(FItem["name", item, FItem["tex"]])

def dumpSavedGame(Plr, Lvl):
    with open(r"Saves\Save.plrstate", "bw") as fPlr: pickle.dump(Plr, fPlr)
    with open(r"Saves\Save.lvlstate", "bw") as fLvl: pickle.dump(Lvl, fLvl)

def loadSavedGame():
    try:
        Plr = open(r"Saves\Save.plrstate", "br")
        Lvl = open(r"Saves\Save.lvlstate", "br")
        Save.append(pickle.load(Plr))
        Save.append(pickle.load(Lvl))
        Plr.close(); Lvl.close()
    except:
        Plr = open(r"Saves\Save.plrstate", "bw"); Plr.close()
        Lvl = open(r"Saves\Save.lvlstate", "bw"); Lvl.close()
        Save.append("!")
