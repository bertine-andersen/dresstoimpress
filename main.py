import pygame as pg
import sys
from constants import *

# Initialiserer/starter pygame
pg.init()


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and knapp.collidepoint(event.pos):
            if not ferdig_trykket:  # Bare hvis ikke allerede trykket
                print("Du klikket")
                ferdig_trykket = True  # Sett til True!

            
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
                valgt_bukse = 0
            if event.key == pg.K_w:
                valgt_bukse = 1
            if event.key == pg.K_e:
                valgt_bukse = 2
            if event.key == pg.K_r:
                valgt_bukse = 3
            if event.key == pg.K_t:
                valgt_bukse = 4



        # Fyll bakgrunn (valgfritt, men anbefalt)
        vindu.fill((255, 255, 255))

        # Tegn jenta
        vindu.blit(silje, silje_rect)

        # Tegn valgt genser og bukse
        genser_rect = gensere[valgt_genser].get_rect()
        genser_rect.centerx = silje_rect.centerx + 8
        genser_rect.top = silje_rect.top + 170

        bukse_rect = bukser[valgt_bukse].get_rect()
        bukse_rect.centerx = silje_rect.centerx + 8
        bukse_rect.top = silje_rect.top + int(SILJE_HOYDE * 0.55)

        vindu.blit(bukser[valgt_bukse], bukse_rect)
        vindu.blit(gensere[valgt_genser], genser_rect)

    
        # Lager en tekst i form av et bilde og legger til bildet i vinduet
        pg.draw.rect(vindu,(255,192,203),knapp)
        bilde = font.render("Ferdig", True, (255, 0, 0)).convert_alpha()
        vindu.blit(bilde, (knapp.x+15, knapp.y+5))

        
        if ferdig_trykket:
        # Vis "Dagens antrekk!" øverst
            finish = font.render("Dagens antrekk!", True, (255, 0, 0))
            vindu.blit(finish, (150, 20))
    
        else:
            # Vis "Ferdig"-knappen
            pg.draw.rect(vindu, (255, 192, 203), knapp)
            bilde = font.render("Ferdig", True, (255, 0, 0))
            vindu.blit(bilde, (knapp.x + 15, knapp.y + 5))
            
        pg.display.flip()


pg.quit()
sys.exit()