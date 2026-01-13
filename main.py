import pygame as pg
import sys

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

current_pants = []
"""
{
    "1": " ",
    "2": " ", 
    "3": " ", 
    "4": " ",
    "5": " "
}
"""
gensere = [
    pg.image.load("dresstoimpress/bilder/overdeler/topp1.png"), 
    pg.image.load("dresstoimpress/bilder/overdeler/topp2.png"), 
    pg.image.load("dresstoimpress/bilder/overdeler/topp3.png"), 
    pg.image.load("dresstoimpress/bilder/overdeler/topp4.png"), 
    pg.image.load("dresstoimpress/bilder/overdeler/topp5.png")
    ]

valgt_genser = 0
"""
{
    "1": "",
    "2": " ", 
    "3": " ", 
    "4": " ", 
    "5": " "}
"""

silje = pg.image.load("dresstoimpress/bilder/jente.png")





running = True


knapp = pg.draw.rect(vindu, (255,192,203),(203,450,100,40) )



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
        vindu.blit(gensere[valgt_genser], (150, 150))

        

        
        pg.display.flip()


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                valgt_genser = 0
            if event.key == pg.K_2:
                valgt_genser = 1
            if event.key == pg.K_3:
                valgt_genser = 2
            if event.key == pg.K_4:
                valgt_genser = 3
            if event.key == pg.K_5:
                valgt_genser = 4

            if event.key == pg.K_q:
                current_pants = current_pants[0]
            if event.key == pg.K_w:
                current_pants = current_pants[1]
            if event.key == pg.K_e:
                current_pants = current_pants[2]
            if event.key == pg.K_r:
                current_pants = current_pants[3]
            if event.key == pg.K_t:
                current_pants = current_pants[4]
    





pg.quit()
sys.exit()