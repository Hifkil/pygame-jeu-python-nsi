# -*- coding: utf-8 -*-

""" Module Stockant la classe Personnage du Jeu Vidéal """

#- Section importation ----------------------------------------------------------------------------
import pygame as pg
pg.init() # On initialise pygame pour utiliser pygame.font et display

#- Section constantes -----------------------------------------------------------------------------
WIDTH, HEIGHT = 1400, 850
FEN = pg.display.set_mode((WIDTH, HEIGHT))

COTE_CASE = 50
PERSO_VITESSE = 150 # En millisecondes

VERT = (111, 210, 46)

POLICE_VIE = pg.font.SysFont('chalkduster.ttf', 30) # On definit la police (nom de la police, taille de la police)
BARRE_DE_VIE = POLICE_VIE.render('Barre de vie :', True, VERT) # On met le texte et la couleur

#- Section classe ---------------------------------------------------------------------------------
class Personnage:
    """ Définie le personnage
    Méthodes  : __init__(self)
                deplacement(self, coord_cases_dures)
                barre_hp(self, fenetre)
    Attributs : self.perso -> hitbox du personnage
                self.vie   -> nombre de points de vie du personnage """
    def __init__(self):
        self.perso = pg.Rect(14*COTE_CASE, 13*COTE_CASE, # Coordonnées d'apparition
                             COTE_CASE, COTE_CASE)       # Taille de la hitbox
        self.vie = 3

    def barre_hp(self, fenetre):
        """ Fonction qui affiche les points de vie du personnage.
        Prends en paramètre self et la fenetre
        Renvoie un rectangle vert situé en dessous du niveau avec le texte """
        # On dessine une barre de vie  
        # Légende :                 | abscisse  | ordonnée      | longueur          | hauteur
        pg.draw.rect(fenetre, VERT, [3*COTE_CASE, 16.5*COTE_CASE, self.vie*COTE_CASE, 15])
        FEN.blit(BARRE_DE_VIE, (3*COTE_CASE, 16*COTE_CASE))  

    def deplacement(self, coord_cases_utiles):
        """ Gère les déplacements du joueur grâce aux touches flèchées
        Fait en sorte que le joueur ne puisse pas sortir de l'écran ou 
        rentrer dans un bloc dans lequel il ne doit pas rentrer
        coord_cases_utiles -> liste contenant les coordonnées x et y en tuple
                              des blocs durs   -> coord_cases_utiles[0]
                              des blocs clef   -> coord_cases_utiles[1] => [1][0] jaune / [1][1] verte
                              des blocs porte  -> coord_cases_utiles[2] => [2][0] jaune / [2][1] verte
                              des blocs sortie -> coord_cases_utiles[3] """
        touche = pg.key.get_pressed()
        if (self.perso.x, self.perso.y) not in coord_cases_utiles[3]: # Le joueur bouge tant qu'il ne touche pas la sortie
            # Vérifie si :        | Le joueur sortira de l'écran      | Le joueur va toucher un bloc mur dans lequel il ne doit pas rentrer |
            if touche[pg.K_LEFT] and (self.perso.x - COTE_CASE) > -1 and (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles[0]:       # GAUCHE
                #  | Le joueur touchera une case porte jaune                                 | Le joueur touchera une case porte verte                                  |
                if (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles[2][0] and (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles[2][1]:
                    self.perso.x -= COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles[4]:
                        self.vie-=1
                    pg.time.delay(PERSO_VITESSE)
            elif touche[pg.K_RIGHT] and (self.perso.x + COTE_CASE) < WIDTH and (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles[0]: # DROITE
                if (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles[2][0] and (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles[2][1]:
                    self.perso.x += COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles[4]:
                        self.vie-=1
                    pg.time.delay(PERSO_VITESSE)
            elif touche[pg.K_UP] and (self.perso.y - COTE_CASE) > -1 and (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles[0]:       # HAUT
                if (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles[2][0] and (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles[2][1]:
                    self.perso.y -= COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles[4]:
                        self.vie-=1
                    pg.time.delay(PERSO_VITESSE)
            elif touche[pg.K_DOWN] and (self.perso.y + COTE_CASE) < HEIGHT and (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles[0]: # BAS
                if (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles[2][0] and (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles[2][1]:
                    self.perso.y += COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles[4]:
                        self.vie-=1
                    pg.time.delay(PERSO_VITESSE)
            
        else: # Ce qui se passe si le joueur touche la sortie
            print('gg') # C'est nul