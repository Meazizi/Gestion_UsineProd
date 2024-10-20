class Usine:
    def __init__(self):
        self.lignes_production = []
        self.varietes_pates = []

    def ajouter_ligne(self, ligne):
        """Ajoute une ligne de production à l'usine."""
        self.lignes_production.append(ligne)

    def ajouter_variete(self, variete):
        """Ajoute une variété de pâtes à l'usine."""
        self.varietes_pates.append(variete)

    def planifier_production(self, ligne, variete):
        """Planifie la production d'une variété sur une ligne."""
        ligne.changer_variete(variete)

    def produire_jour(self):
        """Simule une journée de production pour toutes les lignes."""
        for ligne in self.lignes_production:
            ligne.produire()

    def afficher_etat_stocks(self):
        """Affiche l'état des stocks pour toutes les variétés."""
        for variete in self.varietes_pates:
            print(variete.etat_stock())
