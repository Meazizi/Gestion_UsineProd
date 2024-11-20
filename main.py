import json
from datetime import datetime, timedelta

# Import des classes
from LigneProduction import LigneProduction
from VarietePate import VarietePate
from OrdreProduction import OrdreProduction
from PlanProduction import PlanProduction
from Entrepot import Entrepot
from Commande import Commande


def charger_donnees():
    """Charge les données depuis le fichier data.json."""
    with open("data.json", "r") as file:
        return json.load(file)


def creer_varietes(data):
    """Crée les objets VarietePate à partir des données."""
    varietes = {}
    for variete_data in data["varietes_pates"]:
        variete = VarietePate(
            nom=variete_data["nom"],
            temps_setup=variete_data["temps_setup"],
            cartons_par_jour=variete_data["cartons_par_jour"],
            stock_initial=variete_data["stock_initial"],
        )
        varietes[variete.nom] = variete
    return varietes


def creer_plan_production(data, varietes):
    """Crée le plan de production à partir des données."""
    plan_production = PlanProduction()
    for ordre_data in data["plan_production"]:
        variete = varietes[ordre_data["variete"]]
        ordre = OrdreProduction(
            identifiant=ordre_data["reference"],
            variete=variete,
            quantite=ordre_data["quantite"],
        )
        plan_production.ajouter_ordre(ordre)
    return plan_production


def creer_commandes(data, varietes):
    """Crée les commandes à partir des données."""
    commandes = []
    for commande_data in data["plan_commandes"]:
        donnees_commande = {
            varietes[cmd["variete"]]: cmd["quantite"]
            for cmd in commande_data["commandes"]
        }
        commande = Commande(
            identifiant=commande_data["reference"], donnees_commande=donnees_commande
        )
        commandes.append(commande)
    return commandes


def main():
    data = charger_donnees()
    varietes = creer_varietes(data)
    plan_production = creer_plan_production(data, varietes)
    commandes = creer_commandes(data, varietes)

    entrepot = Entrepot(
        nom="Entrepôt principal",
        stocks={variete: variete.stock_initial for variete in varietes.values()},
    )

    # Initialisation des lignes de production
    lignes = [LigneProduction(nom) for nom in data["lignes_production"]]

    jour = 0
    while jour < 7:
        print(f"=== Jour {jour + 1} ===")

        # Simulation de la production pour chaque ligne
        for ligne in lignes:
            if ligne.ordre_en_cours is None and plan_production.ordres:
                # Affecter un nouvel ordre de production
                nouvel_ordre = plan_production.ordres.pop(0)
                ligne.change_variete(nouvel_ordre)
                print(f"{ligne.nom} commence à produire {nouvel_ordre.variete.nom}.")

            if ligne.ordre_en_cours:
                variete = ligne.ordre_en_cours.variete
                quantite_produite = variete.cartons_par_jour
                entrepot.ajouter_stock(variete, quantite_produite)
                print(
                    f"{ligne.nom} a produit {quantite_produite} cartons de {variete.nom}."
                )

                # Réduction de la quantité restante à produire
                ligne.ordre_en_cours.quantite -= quantite_produite
                if ligne.ordre_en_cours.quantite <= 0:
                    print(f"{ligne.nom} a terminé la production de {variete.nom}.")
                    ligne.ordre_en_cours = None

        # Afficher l'état de l'entrepôt
        entrepot.afficher_stock()
        jour += 1

    # Traiter les commandes en fin de semaine
    print("=== Traitement des commandes ===")
    for commande in commandes:
        print(f"Traitement de la commande {commande.identifiant}:")
        commande.traiter_commande(entrepot)

    # Afficher le stock final
    print("=== État final des stocks ===")
    entrepot.afficher_stock()


if __name__ == "__main__":
    main()
