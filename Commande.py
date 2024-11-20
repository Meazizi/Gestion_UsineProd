class Commande:
    def __init__(self, identifiant, donnees_commande):
        self.identifiant = identifiant
        self.donnees_commande = (
            donnees_commande  # Dictionnaire {VarietePate: quantité demandée}
        )

    def traiter_commande(self, entrepot):
        for variete, quantite in self.donnees_commande.items():
            if not entrepot.retirer_stock(variete, quantite):
                print(
                    f"Commande {self.identifiant} échouée: Stock insuffisant pour {variete.nom}"
                )
                return False
        return True
