import json
from datetime import datetime, timedelta
from utils import (
    charger_donnees,
    creer_varietes,
    creer_plan_production,
    creer_commandes,
    creer_approvisionnement,
)

# Import des classes
from LigneProduction import LigneProduction
from VarietePate import VarietePate
from OrdreProduction import OrdreProduction
from PlanProduction import PlanProduction
from Entrepot import Entrepot
from Commande import Commande
from Approvisionnement import Approvisionnement


def main():
    data = charger_donnees()
    varietes = creer_varietes(data)
    plan_production = creer_plan_production(data, varietes)
    commandes = creer_commandes(data, varietes)
    approvisionnements = creer_approvisionnement(data)

    entrepot = Entrepot(
        nom="Entrepôt principal",
        stocks={variete: variete.stock_initial for variete in varietes.values()},
        stock_oeufs=1500000,
    )

    lignes = [LigneProduction(nom) for nom in data["lignes_production"]]

    total_jours = 28  # Simule 4 semaines
    for jour in range(total_jours):
        print(f"\n=== Jour {jour + 1} ===")

        for ligne in lignes:
            if ligne.ordre_en_cours is None and plan_production.ordres:
                nouvel_ordre = plan_production.ordres.pop(0)
                ligne.change_variete(nouvel_ordre)
                print(f"{ligne.nom} commence à produire {nouvel_ordre.variete.nom}.")

            ligne.produire(entrepot)

        entrepot.afficher_stock()

        # 📦 À la fin de chaque semaine (tous les 7 jours), on gère les commandes et l'approvisionnement en œufs
        if (jour + 1) % 7 == 0:
            print("\n=== Fin de semaine : Traitement des commandes ===")
            for commande in commandes:
                print(f"Traitement de la commande {commande.identifiant}:")
                commande.traiter_commande(entrepot)

            print("\n=== Approvisionnement en oeufs ===")
            if approvisionnements:
                approvisionnement = approvisionnements.pop(0)
                entrepot.approvisionner_oeufs(approvisionnement.quantite)
                print(f"🛒 {approvisionnement.quantite} oeufs 🥚 ajoutés au stock.")

    print("\n=== État final des stocks ===")
    entrepot.afficher_stock()


if __name__ == "__main__":
    main()
