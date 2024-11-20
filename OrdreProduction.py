class OrdreProduction:
    def __init__(self, identifiant, variete, quantite):
        self.identifiant = identifiant
        self.variete = variete  # Type : VarietePate
        self.quantite = quantite

    def afficher_ordre(self):
        print(
            f"Ordre {self.identifiant}: {self.variete.nom}, Quantité: {self.quantite} cartons"
        )
