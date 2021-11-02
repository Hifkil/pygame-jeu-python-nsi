# -*- coding: utf-8 -*-

""" Jeu vidéo de labyrinthe utilisant pygame pour un DM en NSI
Auteurs : Harry, Corentin """

#- Section importations et initialisations --------------------------------------------------------
from Case import Case
from Personnage import Personnage
from fonctions import scale_image

import pygame as pg
import os # L'utilisation de ce module permet la compatibilité du jeu sur d'autres plateformes

pg.init() # Initialise les modules de pygame, on ne les utilises pas encore

#- Section constantes -----------------------------------------------------------------------------
WIDTH, HEIGHT = 1400, 850
FEN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60

MAP = os.path.join('Assets', 'Map.txt')

COTE_CASE = 50

#                                pygame          os      nom dossier, nom image  Nouv. taille
# Redimensionne les images   [             {            (                      )}           ]
PERSO_PRINCIPAL = scale_image(pg.image.load(os.path.join('Assets', 'joueur.png')), COTE_CASE)

#Couleurs  R    V    B
GRIS   = (128, 128, 128)

#- Section classe ---------------------------------------------------------------------------------
class Jeu:
    """ Classe principale Permettant de jouer au jeu
    Méthodes  : __init__(self, map)
                afficher_images(self, personnage, cases)
                afficher_grille(afficher=False)
                demmare(self)
    Attributs : self.laby -> liste stockant l'image des cases de la map et leur coordonnées
                self.coord_cases_utiles -> Liste contenant 3 listes :
                    self.coord_cases_dures -> Liste contenant les coordonnées des blocs 'durs'
                    self.coord_clefs       -> Liste contenant les coordonnées des blocs 'clefs'
                    self.coord_sortie      -> Liste contenant les coordonnées des blocs 'sortie' """
    def __init__(self, map):
        """ map -> nom du fichier texte de la map choisie """
        self.laby = []
        self.coord_cases_utiles = []

        self.coord_cases_dures = []

        self.coord_clefs      = []
        self.coord_clef_jaune = []
        self.coord_clef_verte = []

        self.coord_portes      = []
        self.coord_porte_jaune = []
        self.coord_porte_verte = []

        self.coord_torches = []
        self.coord_sortie = []

        fichier = open(map, 'r')
        lignes  = fichier.readlines()

        ordonee = -1
        for y in range(len(lignes)):
            abscisse = -1
            ordonee += 1
            for x in range(len(lignes[y])):
                abscisse += 1
                # Attribut un type à chaque caractère reconnu
                if lignes[y][x]   == '#':                                        # MUR
                    type = 'mur'
                elif lignes[y][x] == ' ':                                        # VIDE
                    type = 'vide'
                elif lignes[y][x] == '+':                                        # TELEPORTEUR
                    type = 'teleporteur'
                    # Met une case vide en arrière-plan, parce que c'est moche sinon
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == '|':                                        # SORTIE
                    type = 'sortie'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == 'j':                                        # CLEF JAUNE
                    type = 'clef_jaune'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == 'v':                                        # CLEF VERTE
                    type = 'clef_verte'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == 'J':                                        # PORTE JAUNE
                    type = 'porte_jaune'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == 'V':                                        # PORTE VERTE
                    type = 'porte_verte'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == '*':                                        # COFFRE FERME
                    type = 'coffre_ferme'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                elif lignes[y][x] == '!':                                        # TORCHE
                    type = 'torche'
                    case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                else:
                    type = None # Gère les caractères non reconnus

                if type != None:
                    # Convertit les caractères en cases
                    case = Case(type, (abscisse*COTE_CASE, ordonee*COTE_CASE))
                    self.laby.append((case.image, (case.coord)))
                    # Liste les coordonnées de chaque case utile
                    if type == 'mur': 
                        self.coord_cases_dures.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                    elif type == 'sortie':
                        self.coord_sortie.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                    elif type == 'clef_jaune':
                        self.coord_clef_jaune.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                    elif type == 'clef_verte':
                        self.coord_clef_verte.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                    elif type == 'porte_jaune':
                        self.coord_porte_jaune.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                    elif type == 'porte_verte':
                        self.coord_porte_verte.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                    elif type == 'torche':
                        self.coord_torches.append((abscisse*COTE_CASE, ordonee*COTE_CASE))

        # Déplace chaque liste de coordonnées dans une seule
        self.coord_clefs.append(self.coord_clef_jaune)
        self.coord_clefs.append(self.coord_clef_verte)

        self.coord_portes.append(self.coord_porte_jaune)
        self.coord_portes.append(self.coord_porte_verte)

        self.coord_cases_utiles.append(self.coord_cases_dures) # [0] -> blocs 'durs'
        self.coord_cases_utiles.append(self.coord_clefs)       # [1][0] -> clef jaune  / [1][1] -> clef verte
        self.coord_cases_utiles.append(self.coord_portes)      # [2][0] -> porte jaune / [2][1] -> porte verte

        self.coord_cases_utiles.append(self.coord_sortie)      # [3] -> blocs 'sortie'
        self.coord_cases_utiles.append(self.coord_torches)     # [4] -> blocs 'torche'

        fichier.close()

    def afficher_images(self, personnage, cases):
        """ Affiche les éléments de la fenêtre
        personnage -> instance de la classe Personnage
        cases -> liste stockant chaque instance des cases du labyrinthe """
        for img, coord in cases:
            FEN.blit(img, coord)

        FEN.blit(PERSO_PRINCIPAL, (personnage.perso.x, personnage.perso.y))

    def afficher_grille(afficher=False):
        """ Affiche une grille montrant les cases du jeu,
        n'affiche rien par défaut, nécéssite d'appuyer sur la touche G """
        touche = pg.key.get_pressed()
        if touche[pg.K_g]:  # Permet d'afficher la grille quand G est pressé
            if afficher == True:
                afficher = False
            elif afficher == False:
                afficher = True

        # Affiche la grille si afficher est True
        if afficher:
            for x in range(0, WIDTH, COTE_CASE):
                for y in range(0, HEIGHT, COTE_CASE):
                    case = pg.Rect(x, y, COTE_CASE, COTE_CASE)
                    pg.draw.rect(FEN, GRIS, case, 1)

    def demarre(self):
        """ Démarre une partie """
        pg.display.set_caption("Jeu Vidéal") # Titre de la fenêtre
        pg.display.set_icon(PERSO_PRINCIPAL) # Icone de la fenêtre
        personnage = Personnage()

        clock = pg.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    
            if (personnage.perso.x, personnage.perso.y)   in self.coord_cases_utiles[1][0]:
                self.coord_cases_utiles[2][0] = [()]
            elif (personnage.perso.x, personnage.perso.y) in self.coord_cases_utiles[1][1]:
                self.coord_cases_utiles[2][1] = [()]
    
            FEN.fill(GRIS)

            personnage.deplacement(self.coord_cases_utiles)
            Jeu.afficher_images(self, personnage, self.laby)
            personnage.barre_hp(FEN)
            Jeu.afficher_grille()

            pg.display.update()

#- Section principale -----------------------------------------------------------------------------
if __name__ == '__main__': # Permet de ne pas lancer le jeu si on l'importe en tant que module
    partie = Jeu(MAP)
    partie.demarre()
    pg.quit()