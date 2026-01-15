import pygame as pg 

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

GENSER_BREDDE = int(SILJE_BREDDE * 0.6)
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


font = pg.font.SysFont("Arial", 20)

running = True
ferdig_trykket = False  # NY VARIABEL!

#knapp = pg.draw.rect(vindu, (255,192,203),(203,450,100,40) )
knapp = pg.Rect(200,450,100,40)


FPS = 60