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

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

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

# Initialiserer/starter pygame
pg.init()
