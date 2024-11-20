class Entrepot:
    def __init__(self, nom, stocks):
        self.nom = nom
        self.stocks = stocks  # Dictionnaire {VarietePate: quantité actuelle}
        self.stock_initial = stocks.copy()

    def ajouter_stock(self, variete, quantite):
        if variete in self.stocks:
            self.stocks[variete] += quantite
        else:
            self.stocks[variete] = quantite

    def retirer_stock(self, variete, quantite):
        if self.stocks.get(variete, 0) >= quantite:
            self.stocks[variete] -= quantite
            return True
        return False

    def afficher_stock(self):
        for variete, quantite in self.stocks.items():
            print(f"{variete.nom}: {quantite} cartons")
