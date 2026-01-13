import pygame as pg
import sys

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

current_pants = {
    "1": " ",
    "2": " ", 
    "3": " ", 
    "4": " ",
    "5": " "
}
current_sweater = {
    "1": "",
    "2": " ", 
    "3": " ", 
    "4": " ", 
    "5": " "}

silje = pg.image.load("dresstoimpress/bilder/jente.png")


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    
        # Fyll bakgrunn (valgfritt, men anbefalt)
        vindu.fill((255, 255, 255))

        # Tegn jenta (alltid)
        vindu.blit(silje, (130, 0))

        pg.display.flip()

"""
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                current_sweater = current_sweater[0]
            if event.key == pg.K_2:
                current_sweater = current_sweater[1]
            if event.key == pg.K_3:
                current_sweater = current_sweater[2]
             if event.key == pg.K_4:
                current_sweater = current_sweater[3]
            if event.key == pg.K_5:
                current_sweater = current_sweater[4]

            if event.key == pg.K_q:
                current_pants = 
            if event.key == pg.K_w:
                current_pants = 
            if event.key == pg.K_e:
                current_pants = 
"""



pg.quit()
sys.exit()