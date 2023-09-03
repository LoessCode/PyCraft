from Gen.World import World
import Gen.Entity as Entity
import Gen.GenEngine as GenEngine
import Utils.HitBoxHandler as HitBoxHandler
import Registry
import random

boardRadius = 9

def init():
    global Lvl, Player
    if Registry.Save[0] == "!":
        Lvl = World()
        Player = Entity.Player()
        GenPane((0, 0))
    else:
        Lvl = Registry.Save[1]
        Player = Registry.Save[0]
        GenPane(Player.pos)

    

def GenPane(pos):
    #TileChoice = random.choice((Registry.Tiles["Env.Mud"], Registry.Tiles["Env.Rock"], Registry.Tiles["Env.Gravel"], Registry.Tiles["Env.Sand"]))
    #Tiles = [[World.Tile(TileChoice, (i,j)) for i in range(boardRadius)] for j in range(boardRadius)]
    """
    for x in range(9):
        Tiles.append([])
        rowI = x
        for i in range(9):
            TileChoice = random.choice((Registry.Tiles["Env.Mud"], Registry.Tiles["Env.Rock"], Registry.Tiles["Env.Gravel"], Registry.Tiles["Env.Sand"]))
            Tiles[rowI].append(World.Tile(TileChoice, (i, rowI)))
    """

    Tiles = GenEngine.genTiles(pos)
    Lvl.AddPane(World.Pane(Tiles, pos))

def movePlayer(dir, distance=1):
    dirKey = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0)}
    dir = dirKey[dir]
    
    #Position of next pane and player in said plane
    nextPane = Player.pane[0] + dir[0], Player.pane[1] + dir[1]
    nextPanePlayerPos = HitBoxHandler.getNextPanePlayerPos(Player.pos, dir)

    if HitBoxHandler.isTouchingPaneBound(Player.pos, dir):
        if str(nextPane)[1:-1] in Lvl.World:
            Player.setPos(nextPanePlayerPos, nextPane)
        else:
            GenPane(nextPane)
            Player.setPos(nextPanePlayerPos, nextPane)

    else: Player.setPos((Player.pos[0] + dir[0]*distance, Player.pos[1] + dir[1]*distance))
