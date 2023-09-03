import pygame
import Gen.WorldBuilder as WorldBuilder


global panel
panel = pygame.display.set_mode((1920, 1080))
CENTERCONST = (1920/2 - 16*9, 1080/2 - 16*9)


def init():
    pygame.init()
    panel = pygame.display.set_mode((1920, 1080))


def drawPlayer(pos, pane):
    
    playerTex = pygame.image.load(WorldBuilder.Player.tex).convert_alpha()

    playerRect = pygame.Rect((pos[0] * 32 + CENTERCONST[0]), (pos[1] * 32 + CENTERCONST[1]), 32, 32)

    panel.blit(playerTex, playerRect)

    pygame.display.update()


def drawPane(key, ref=(0, 0), flag = "nr", lm=255):
    #for paneKey in World.Lvl.World:
    pane = WorldBuilder.Lvl.World[str(key)[1:-1]]
    centerConst = (CENTERCONST[0] + ref[0]*32*9, CENTERCONST[1] + ref[1]*32*9)

    for tileRow in pane.Tiles:
        for tile in tileRow:
            tileTex = pygame.image.load(tile.Tile.tex).convert_alpha()
            tileTex.fill((255, 255, 255, lm), special_flags=pygame.BLEND_RGBA_MULT)
            #Here, 32 is the width and height of the rect.
            tileRect = pygame.Rect((tile.pos[0] * 32 + centerConst[0]), (tile.pos[1] * 32 + centerConst[1]), 32, 32)

            panel.blit(tileTex, tileRect)
    if flag == "nr":
        drawFade(key)
    drawPlayer(WorldBuilder.Player.pos, pane)

    #pygame.display.update() # is done by drawPlayer.

def drawFade(key):
    posmatrix = [[(i, j) for i in range(key[0]-1, key[0]+2)] for j in range(key[1]-1, key[1]+2)]; posmatrix[1].remove(posmatrix[1][1])
    for ls in posmatrix: 
        for i in ls:
            ref = (i[0] - key[0], i[1] - key[1])
            if str(i)[1:-1] in WorldBuilder.Lvl.World:
                drawPane(i, ref=ref, flag='r', lm=100)
            else:
                WorldBuilder.GenPane(i)
                drawPane(i, ref=ref, flag='r', lm=100)
    fadeTex = pygame.image.load(r"Data\Assets\Hud\FadeMask.png")
    fadeRect = pygame.Rect(0, 0, 1920, 1080)


def Clear(): panel.fill((0, 0, 0))