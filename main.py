from VarietePate import VarietePate
from LigneProduction import LigneProduction
from Usine import Usine
from ServiceAchat import ServiceAchat

# Initialisation des variétés de pâtes
spaghetti = VarietePate("Spaghetti", 2, 100, 500)
penne = VarietePate("Penne", 1, 80, 400)
fusilli = VarietePate("Fusilli", 3, 90, 600)

# Création de l'usine
usine = Usine()
usine.ajouter_variete(spaghetti)
usine.ajouter_variete(penne)
usine.ajouter_variete(fusilli)

# Ajout de deux lignes de production
ligne1 = LigneProduction("Ligne 1")
ligne2 = LigneProduction("Ligne 2")
usine.ajouter_ligne(ligne1)
usine.ajouter_ligne(ligne2)

# Plan de production
usine.planifier_production(ligne1, spaghetti)
usine.planifier_production(ligne2, penne)

# Simuler 5 jours de production
for jour in range(5):

    print(f"Jour {jour + 1}:")
    usine.produire_jour()
    usine.afficher_etat_stocks()
    print()

# Service Achat prend des commandes
commandes = {"Spaghetti": 200, "Penne": 100}
service_achat = ServiceAchat(commandes)
service_achat.traiter_commandes(usine)

# Afficher les stocks après les commandes
print("Stocks après les commandes:")
usine.afficher_etat_stocks()
