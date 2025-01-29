import json
from VarietePate import VarietePate
from PlanProduction import PlanProduction
from OrdreProduction import OrdreProduction
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
            oeufs_par_carton=variete_data["oeufs_par_carton"],
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
