class LigneProduction:
    def __init__(self, nom):
        self.nom = nom
        self.variete_actuelle = None
        self.temps_restaurant_setup = 0

    def changer_variete(self, nouvelle_variete):
        """Change la variété produite sur la ligne et gère le temps de setup."""
        if self.variete_actuelle != nouvelle_variete:
            print(
                f"Changement de variété sur {self.nom}: {self.variete_actuelle} -> {nouvelle_variete.nom}"
            )
            self.temps_restaurant_setup = nouvelle_variete.temps_setup
            self.variete_actuelle = nouvelle_variete

    def produire(self):
        """Produire des cartons si le setup est terminé."""
        if self.temps_restaurant_setup > 0:
            self.temps_restaurant_setup -= 1
            print(
                f"Setup en cours sur {self.nom}, encore {self.temps_restaurant_setup} jour(s) à attendre."
            )
        elif self.variete_actuelle:
            print(f"Production en cours sur {self.nom} de {self.variete_actuelle.nom}")
            self.variete_actuelle.ajouter_stock(self.variete_actuelle.quantite_produite)
        else:
            print(f"Aucune production sur {self.nom}")
