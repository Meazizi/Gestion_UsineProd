class Entrepot:
    def __init__(self, nom, stocks, stock_oeufs):
        self.nom = nom
        self.stocks = stocks  # Dictionnaire {VarietePate: quantité actuelle}
        self.stock_initial = stocks.copy()
        self.stock_oeufs = stock_oeufs

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

    def utiliser_oeufs(self, quantite):
        if self.stock_oeufs >= quantite:
            self.stock_oeufs -= quantite
            return True
        return False

    def approvisionner_oeufs(self, quantite):
        self.stock_oeufs += quantite

    def afficher_stock(self):
        for variete, quantite in self.stocks.items():
            print(f"{variete.nom}: {quantite} cartons 📦")
