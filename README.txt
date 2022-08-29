Instructions pour cr�er une nouvelle map / niveau

Pour cr�er une map :
- Ins�rer un fichier texte dans le dossier 'Assets'
- Ajouter une constante MAP_x dans le fichier utilitaire.py menant vers
  le fichier et l'ins�rer dans la liste MAPS en se fiant aux autres constantes MAP

---------------------------------------------------------------------------------------------------
L�gende :
- # -> mur
-   -> vide
- + -> t�l�porteur (inutilis�)
- * -> coffre ferm�
- $ -> coffre ouvert
- ! -> torche
- D -> porte d�part (grise)
- | -> porte sortie (marron)
- . -> point d'apparition du joueur

    - j -> clef jaune
    - v -> clef verte
    - r -> clef rouge

    - J -> porte jaune
    - V -> porte verte
    - R -> porte rouge

---------------------------------------------------------------------------------------------------
Exemple du niveau 2  :

#D##########################
#.                        !#
#########################  #
#                          #
##### #################### #
#!#                   R !# #
#v######### ###########  # #
#J#   #   #   ####   ### # #
#   #   # # ## j#  #  ##*# #
######### # #  ### ## #### #
#           #       #    # #
#V#### ################# ###
#r#                      #|#
#J######################## #
#           !!!            *
############################