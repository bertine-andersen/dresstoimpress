import pygame as pg
import sys

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


# laster opp jenta
silje = pg.image.load("bilder/jente.png").convert_alpha()

SILJE_BREDDE = 240
SILJE_HOYDE = 480

silje = pg.transform.scale(silje, (SILJE_BREDDE, SILJE_HOYDE))
silje_rect = silje.get_rect(topleft=(130, 10))


# laster opp bilder
gensere = [
    pg.image.load("bilder/overdeler/topp1.png").convert_alpha(),
    pg.image.load("bilder/overdeler/topp2.png").convert_alpha(),
    pg.image.load("bilder/overdeler/topp3.png").convert_alpha(),
    pg.image.load("bilder/overdeler/topp4.png").convert_alpha(),
    pg.image.load("bilder/overdeler/topp5.png").convert_alpha()
]

GENSER_BREDDE = int(SILJE_BREDDE * 0.65)
GENSER_HOYDE = int(SILJE_HOYDE * 0.3)

# skalerer genserene
gensere = [
    pg.transform.scale(genser, (GENSER_BREDDE, GENSER_HOYDE))
    for genser in gensere
]

valgt_genser = 0


bukser = [
    pg.image.load("bilder/underdeler/bunn1.png").convert_alpha(),
    pg.image.load("bilder/underdeler/bunn2.png").convert_alpha(),
    pg.image.load("bilder/underdeler/bunn3.png").convert_alpha(),
    pg.image.load("bilder/underdeler/bunn4.png").convert_alpha(),
    pg.image.load("bilder/underdeler/bunn5.png").convert_alpha(),


]

BUKSE_BREDDE = int(SILJE_BREDDE * 0.65)
BUKSE_HOYDE = int(SILJE_HOYDE * 0.3)

# skalerer bukser
bukser = [
    pg.transform.scale(bukse, (BUKSE_BREDDE, BUKSE_HOYDE))
    for bukse in bukser
]

valgt_bukse = 0


font = pg.font.SysFont("Arial", 10)



running = True


#knapp = pg.draw.rect(vindu, (255,192,203),(203,450,100,40) )
knapp = pg.Rect(200,450,100,40)


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and knapp.collidepoint(event.pos):
            print("Du klikket")
            



    
        # Fyll bakgrunn (valgfritt, men anbefalt)
        vindu.fill((255, 255, 255))

        # Tegn jenta
        vindu.blit(silje, silje_rect)

        # Tegn valgt genser og bukse
        genser_rect = gensere[valgt_genser].get_rect()
        genser_rect.centerx = silje_rect.centerx
        genser_rect.top = silje_rect.top + 90

        bukse_rect = bukser[valgt_bukse].get_rect()
        bukse_rect.centerx = silje_rect.centerx
        bukse_rect.top = silje_rect.top + int(SILJE_HOYDE * 0.5)

        vindu.blit(bukser[valgt_bukse], bukse_rect)
        vindu.blit(gensere[valgt_genser], genser_rect)

    
        # Lager en tekst i form av et bilde og legger til bildet i vinduet
        pg.draw.rect(vindu,(255,192,203),knapp)
        bilde = font.render("Ferdig", True, (255, 0, 0)).convert_alpha()
        vindu.blit(bilde, (knapp.x+15, knapp.y+5))

        

        
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
                valgt_bukse = 0
            if event.key == pg.K_w:
                valgt_bukse = 1
            if event.key == pg.K_e:
                valgt_bukse = 2
            if event.key == pg.K_r:
                valgt_bukse = 3
            if event.key == pg.K_t:
                valgt_bukse = 4
    





pg.quit()
sys.exit()