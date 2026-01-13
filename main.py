import pygame as pg
import sys

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

current_pants = []
current_sweater = []
silje = pg.image.load("drestoimpress/bilder/jente.png")


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
        vindu.blit(silje, (0, 0))

        pg.display.flip()

"""
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                current_sweater = 
            if event.key == pg.K_2:
                current_sweater = 
            if event.key == pg.K_3:
                current_sweater = 

            if event.key == pg.K_q:
                current_pants = 
            if event.key == pg.K_w:
                current_pants = 
            if event.key == pg.K_e:
                current_pants = 
"""



pg.quit()
sys.exit()