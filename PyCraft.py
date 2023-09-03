import Gen.WorldBuilder as WorldBuilder
import Gen.Entity as Entity
import pygame
import Registry
import Render.Render as Render
import Utils.InputHandler as InputHandler


#Registers all items and tiles from local Data
Registry.RegisterAll()
Registry.loadSavedGame()

#Initiates World-Gen module
WorldBuilder.init()

#Initiates the Render module
Render.init()

def update():
    Render.Clear()
    Render.drawPane(WorldBuilder.Player.pane)

running = True
while(running):
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            Registry.dumpSavedGame(WorldBuilder.Player, WorldBuilder.Lvl)
            pygame.quit()
            quit()

        #Movement
        elif event.type == pygame.KEYDOWN:
            InputHandler.keyDown(event.key)
            update()

    #input("1")

    #pygame.display.update()
