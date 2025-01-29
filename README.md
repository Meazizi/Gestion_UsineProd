# Gestion_UsineProd
Un petit programme orienté objet qui simule la production d'une usine de pâtes.
Le fichier utils.py contient des fonctions utilitaires permettant entre autre d'importer les données du fichier data.json.
Les différents classes sont contenues dans les fichiers .py portant le même nom (ex: la classe VarietePate est contenue dans le fichier VarietePate.py).

En ce qui concerne la gestion de la production et de l'approvisionnement : 
- Le nombre de jours de production est déterminé à l'avance.
- J'ai choisi de traiter les commandes et l'approvisionnement à la fin de chaque semaine.
- Une commande peut-être traitée uniquement si l'ensemble des produits peuvent être livrés dans les bonnes quantités.
- Une ligne peut continuer sa production uniquement si l'ensemble des ingrédients sont en quantité suffisante.
- Pour l'utilisation de la farine, j'ai choisi de définir les quantités en kg.
- L'approvisionnement concerne tous les ingrédients à la fois.