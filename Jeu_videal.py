# -*- coding: utf-8 -*-

""" Jeu vidéo de labyrinthe utilisant pygame pour un DM en NSI
La map du jeu est stockée dans un fichier texte, chaque caractère correspond à une case
Le but est de trouver la sortie en franchissant des obstacles pas du tout variés
Auteurs : Harry, Corentin 
Version : 21w47b """

#- Section importations ---------------------------------------------------------------------------
from utilitaire import *
from Case import Case
from Personnage import Personnage

import pygame as pg

#- Section classes --------------------------------------------------------------------------------
class Jeu:
    """ Classe principale permettant de jouer au jeu,\n
    Méthodes :
    - __init__(self, map)
    - cinematique_fin()
    - afficher_images(self, personnage, cases)
    - ouvrir_portes(self, couleur)
    - demarre(self, vie)

    Attributs :
    - self.laby -> liste stockant chaque instance de Case, et donc leurs données :
        - type  -> self.laby[n].type   où n est l'indice de la case recherchée
        - coord -> self.laby[n].coord
        - image -> self.laby[n].image
    - self.coord_cases_utiles -> dictionnaire contenant 10 clefs :
        - self.coord_cases_utiles['blocs_durs']
        - self.coord_cases_utiles['depart']
        - self.coord_cases_utiles['sortie']
        - self.coord_cases_utiles['torches']
        - self.coord_cases_utiles['clefs']['jaune']
        - self.coord_cases_utiles['clefs']['verte']
        - self.coord_cases_utiles['clefs']['rouge']
        - self.coord_cases_utiles['portes']['jaune']
        - self.coord_cases_utiles['portes']['verte']
        - self.coord_cases_utiles['portes']['rouge'] """
    def __init__(self, map):
        """ - map -> nom du fichier texte de la map choisie """
        # Vérifie si il y a bien un point de départ dans le fichier
        with open(map, 'r') as test:
            assert '.' in test.read(), "Il n'y a aucun point d'apparition dans le fichier (.)"

        self.laby = []
        self.coord_cases_utiles = {}

        coord_cases_dures = []

        coord_clefs      = {}
        coord_clef_jaune = []
        coord_clef_verte = []
        coord_clef_rouge = []

        coord_portes      = {}
        coord_porte_jaune = []
        coord_porte_verte = []
        coord_porte_rouge = []

        coord_sortie = []
        coord_depart = []

        coord_coffres_fermes = []

        coord_torches = []

        fichier = open(map, 'r')
        lignes  = fichier.readlines()

        ordonee = -1 # ordonee et abscisse commencent à -1 car il augmentent de 1 dès le début, on pourrais juste déplacer les lignes plus bas si besoin, mais les bonnes
        for y in range(len(lignes)):
            abscisse = -1
            ordonee += 1
            for x in range(len(lignes[y])):
                abscisse += 1
                # Attribut un type à chaque caractère reconnu dans le fichier
                for symbole, type_case in DICO_CARACTERE.items():
                    if lignes[y][x] == symbole:
                        type = type_case
                        # Met une case vide en arrière-plan, parce que c'est moche sinon
                        if type != 'mur' and type != 'vide': # Inutile pour ces deux cases
                            case = Case('vide', (abscisse*COTE_CASE, ordonee*COTE_CASE))
                            self.laby.append(case)
                    # Gère les caractères non reconnus
                    else:
                        type = None

                    # Convertit les caractères en cases si le caractère est reconnu
                    if type != None:
                        case = Case(type, (abscisse*COTE_CASE, ordonee*COTE_CASE))
                        self.laby.append(case)
                        # Liste les coordonnées de chaque case utile
                        if type == 'mur' or type == 'porte_depart': # Cases dures
                            coord_cases_dures.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'sortie':
                            coord_sortie.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'clef_jaune':
                            coord_clef_jaune.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'clef_verte':
                            coord_clef_verte.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'clef_rouge':
                            coord_clef_rouge.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'porte_jaune':
                            coord_porte_jaune.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'porte_verte':
                            coord_porte_verte.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'porte_rouge':
                            coord_porte_rouge.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'coffre_ferme':
                            coord_coffres_fermes.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'torche':
                            coord_torches.append((abscisse*COTE_CASE, ordonee*COTE_CASE))
                        elif type == 'depart':
                            coord_depart.append(abscisse*COTE_CASE) # 2 lignes différentes car il n'y a qu'un seul point de départ, c'est plus pratique comme ça
                            coord_depart.append(ordonee*COTE_CASE)

        # Déplace chaque liste de coordonnées dans une seule
        coord_clefs['jaune'] = coord_clef_jaune
        coord_clefs['verte'] = coord_clef_verte
        coord_clefs['rouge'] = coord_clef_rouge

        coord_portes['jaune'] = coord_porte_jaune
        coord_portes['verte'] = coord_porte_verte
        coord_portes['rouge'] = coord_porte_rouge

        self.coord_cases_utiles['clefs']  = coord_clefs
        self.coord_cases_utiles['portes'] = coord_portes

        self.coord_cases_utiles['blocs_durs'] = coord_cases_dures
        self.coord_cases_utiles['depart'] = coord_depart
        self.coord_cases_utiles['sortie'] = coord_sortie

        self.coord_cases_utiles['coffres_fermes'] = coord_coffres_fermes

        self.coord_cases_utiles['torches'] = coord_torches
        
        fichier.close()

    def cinematique_fin():
        """ Affiche une "Cinématique" de fin """
        FEN.fill(NOIR)
        FEN.blit(TEXTE_FIN, ((WIDTH//2)-(TEXTE_FIN.get_width()//2), (HEIGHT//2)-(TEXTE_FIN.get_height()//2))) # Affiche le texte
        FEN.blit(JOUEUR, (WIDTH//2 - COTE_CASE, COTE_CASE*5))
        # Affiche les torches
        for x in range(1, LONGUEUR_MAP-1):
            FEN.blit(TORCHE, (x*COTE_CASE, COTE_CASE))
            FEN.blit(TORCHE, (((LONGUEUR_MAP-1)-x)*COTE_CASE, HEIGHT - 2*COTE_CASE)) # (27-x) permet de faire la même cinématique mais à l'envers
            pg.time.delay(50)
            pg.display.update()
        for y in range(1, HAUTEUR_MAP-1):
            FEN.blit(TORCHE, (COTE_CASE, y*COTE_CASE))
            FEN.blit(TORCHE, (WIDTH - 2*COTE_CASE, ((HAUTEUR_MAP-1)-y)*COTE_CASE))
            pg.time.delay(50)
            pg.display.update()

        pg.time.delay(6000) # Durée de la "cinématique" en millisecondes

    def afficher_images(self, personnage, cases):
        """ Affiche les éléments de la fenêtre
        - personnage -> instance de la classe Personnage
        - cases -> liste stockant chaque instance des cases du labyrinthe """
        for case in cases:
            FEN.blit(case.image, case.coord)

        FEN.blit(JOUEUR, (personnage.perso.x, personnage.perso.y))

    def ouvrir_portes(self, couleur:str):
        """ Ouvre les portes
        - couleur -> couleur des portes et des clefs à suprimmer """
        self.coord_cases_utiles['portes'][couleur] = [] # Supprimme des cases utiles les coords des portes
        self.coord_cases_utiles['clefs'][couleur]  = [] # et des clefs de la couleur choisie
        n = 0
        for case in self.laby:
            if case.type == 'porte_' + couleur or case.type == 'clef_' + couleur: # Les portes et les clefs de la couleur deviennent des cases vides
                self.laby[n].changer_type('vide') # NOTE : on pourrait remplacer une porte par une image de porte ouverte plutôt qu'une case vide
            n += 1

    def demarre(self, vie:int) -> int:
        """ Démarre une partie 
        - vie -> nombre de points de vie lorsqu'on démarre le niveau """
        pg.display.set_caption('Jeu Vidéal') # Titre de la fenêtre
        pg.display.set_icon(COFFRE_OUVERT)   # Icone de la fenêtre

        personnage = Personnage(self.coord_cases_utiles['depart'], vie)

        clock = pg.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT: # Nécéssaire pour quitter la fenêtre, sinon le jeu crash
                    running = False
                    pg.quit()

            # Codes de triche
            touche = pg.key.get_pressed()
            if touche[pg.K_n]:      # N : Niveau suivant
                running = False
                pg.time.delay(500)
            elif touche[pg.K_h]:    # H : +1 PdV
                personnage.vie += 1
                pg.time.delay(200)

            # Relance la même partie chaque fois que le personnage meurt
            if personnage.vie <= 0:
                running = False
                partie = Jeu(map)
                return partie.demarre(PV_DEBUT)

            # La partie s'arrête si le joueur touche la sortie
            if (personnage.perso.x, personnage.perso.y) in self.coord_cases_utiles['sortie']:
                running = False

            # Ouverture des portes si une clef est ramassée
            if (personnage.perso.x, personnage.perso.y) in self.coord_cases_utiles['clefs']['jaune']:
                Jeu.ouvrir_portes(self, 'jaune')
            elif (personnage.perso.x, personnage.perso.y) in self.coord_cases_utiles['clefs']['verte']:
                Jeu.ouvrir_portes(self, 'verte')
            elif (personnage.perso.x, personnage.perso.y) in self.coord_cases_utiles['clefs']['rouge']:
                Jeu.ouvrir_portes(self, 'rouge')

            # Ouvre le coffre sur lequel est le perso et lui donne 1 PdV
            if (personnage.perso.x, personnage.perso.y) in self.coord_cases_utiles['coffres_fermes']:
                # Ouvre visuelement le coffre sur lequel est le perso
                n = 0
                for case in self.laby:
                    if case.type == 'coffre_ferme' and case.coord == (personnage.perso.x, personnage.perso.y): # Vérifie aussi si le coffre est au même endroit que le joueur
                        self.laby[n].changer_type('coffre_ouvert')
                    n += 1
                # Retire le coffre sur lequel est le perso des cases_utiles
                n = 0
                for coord_coffre in self.coord_cases_utiles['coffres_fermes']:
                    if coord_coffre == (personnage.perso.x, personnage.perso.y):
                        del self.coord_cases_utiles['coffres_fermes'][n]
                    n += 1
                personnage.vie += 1 # Important pour que le coffre soit utile :)

            FEN.fill(GRIS) # Couleur de fond

            personnage.deplacement(self.coord_cases_utiles)    ##
            Jeu.afficher_images(self, personnage, self.laby)   ##    L'ORDRE A UNE IMPORTANCE
            personnage.afficher_vie()                          ##
            Case.afficher_grille()                             ##

            pg.display.update() # Actualise la fenêtre, permet d'afficher quelque chose à l'écran, sinon écran noir

        return personnage.vie # Permet de communiquer le nombre de points de vie entre chaque niveau

#- Section principale -----------------------------------------------------------------------------
if __name__ == '__main__': # Permet de ne pas lancer le jeu si on l'importe en tant que module
    try:
        vie = PV_DEBUT
        for map in MAPS:
            partie = Jeu(map)
            vie = partie.demarre(vie) # Retient le nombre de PV à la fin de la partie pour relancer une partie avec le même nombre de PV

        Jeu.cinematique_fin()

    except pg.error: # "L'erreur" pouvant survenir est lorsque l'utilisateur quitte le jeu en pleine partie
        print("Fin de la partie") # Nul
    finally:
        pg.quit()