from pynoise.noisemodule import *
from pynoise.noiseutil import *
import json
import Registry
from Gen.World import World

perlin = Perlin(octaves=2)
TerrainKey = json.load(open(r"Data\Tile\TerrainKey.json", "r"))

"""
biomemap = noise_map_plane(9, 9, 0.5, 1, 0.5, 1, perlin)
gradient = grayscale_gradient()
render = RenderImage()
render.render(9, 9, biomemap, 'terrain2.png', gradient)
print(biomemap)
"""

def reduceFloat(x):
    for key in TerrainKey:
        if x <= float(key):
            return key

def genMap(pos):
    biomemap = noise_map_plane(9, 9, pos[0]/2, pos[0]/2+0.5, pos[1]/2, pos[1]/2+0.5, perlin)
    #gradient = grayscale_gradient()
    #render = RenderImage()
    #render.render(9, 9, biomemap, f'terrain{pos}.png', gradient)
    return [biomemap[i].round(2) + 1 for i in range(81)]

def genTiles(pos):
    map = genMap(pos)
    Tiles = []
    rTiles = [[] for i in range(9)]
    for i in map:
        Tiles.append(Registry.Tiles[TerrainKey[reduceFloat(i)]])
    for i in range(81):
        rTiles[i//9].append(World.Tile(Tiles[i], (i-(i//9)*9, (i//9))))
    return rTiles

