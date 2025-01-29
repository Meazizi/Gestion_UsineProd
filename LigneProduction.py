class LigneProduction:
    def __init__(self, nom, ordre_en_cours=None):
        self.nom = nom
        self.ordre_en_cours = ordre_en_cours  # Type : OrdreProduction
        self.variete_actuelle = None  # VarietePate actuellement produite
        self.en_pause = False

    def change_variete(self, nouvel_ordre):
        if self.ordre_en_cours and self.variete_actuelle:
            temps_setup = self.variete_actuelle.obtenir_temps_setup()
            print(
                f"Changement de variété : Temps de setup nécessaire ({temps_setup} jours)"
            )
        else:
            print("Aucun temps de setup nécessaire (première production).")

        self.ordre_en_cours = nouvel_ordre
        self.variete_actuelle = nouvel_ordre.variete
        print(
            f"Nouvelle variété en production sur {self.nom} : {self.variete_actuelle.nom}"
        )

    def produire(self, entrepot):
        if self.ordre_en_cours and not self.en_pause:
            variete = self.ordre_en_cours.variete
            oeufs_requis = variete.cartons_par_jour * variete.oeufs_par_carton
            if entrepot.utiliser_oeufs(oeufs_requis):
                entrepot.ajouter_stock(variete, variete.cartons_par_jour)
                print(
                    f"{self.nom} a produit {variete.cartons_par_jour} cartons de {variete.nom}."
                )
                self.ordre_en_cours.quantite -= variete.cartons_par_jour
                if self.ordre_en_cours.quantite <= 0:
                    print(f"{self.nom} a terminé la production de {variete.nom}.")
                    self.ordre_en_cours = None
            else:
                print(
                    f"{self.nom} en pause : pas assez d'œufs pour produire {variete.nom}."
                )
                self.en_pause = True
        elif self.en_pause:
            oeufs_requis = (
                self.variete_actuelle.cartons_par_jour
                * self.variete_actuelle.oeufs_par_carton
            )
            if entrepot.utiliser_oeufs(oeufs_requis):
                self.en_pause = False
                print(
                    f"{self.nom} reprend la production de {self.variete_actuelle.nom}."
                )
