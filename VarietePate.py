class VarietePate:
    def __init__(self, nom, temps_setup, quantite_produite, stock_initial):
        self.nom = nom
        self.temps_setup = temps_setup  # en jours
        self.quantite_produite = quantite_produite  # cartons produits par jour
        self.stock_initial = stock_initial
        self.stock = stock_initial

    def ajouter_stock(self, quantite):
        """Ajoute des cartons au stock."""
        self.stock += quantite

    def retirer_stock(self, quantite):
        """Retire des cartons du stock (pour les commandes)."""
        if quantite <= self.stock:
            self.stock -= quantite
        else:
            print(f"Pas assez de stock pour {self.nom}.")

    def etat_stock(self):
        """Affiche l'état du stock."""
        return f"{self.nom} - Stock: {self.stock} cartons"
