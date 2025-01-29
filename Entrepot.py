class Entrepot:
    def __init__(self, nom, stocks, stock_oeufs, stock_farine):
        self.nom = nom
        self.stocks = stocks  # Dictionnaire {VarietePate: quantité actuelle}
        self.stock_initial = stocks.copy()
        self.stock_oeufs = stock_oeufs
        self.stock_farine = stock_farine

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

    def utiliser_farine(self, quantite):
        if self.stock_farine >= quantite:
            self.stock_farine -= quantite
            return True
        return False

    def approvisionner_oeufs(self, quantite):
        self.stock_oeufs += quantite

    def approvisionner_farine(self, quantite):
        self.stock_farine += quantite

    def afficher_stock(self):
        for variete, quantite in self.stocks.items():
            print(f"{variete.nom}: {quantite} cartons 📦")
