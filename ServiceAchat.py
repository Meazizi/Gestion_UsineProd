class ServiceAchat:
    def __init__(self, commandes):
        self.commandes = commandes  # Dict de {variete_nom: quantite}

    def traiter_commandes(self, usine):
        """Réduit les stocks en fonction des commandes hebdomadaires."""
        for variete in usine.varietes_pates:
            if variete.nom in self.commandes:
                quantite_commande = self.commandes[variete.nom]
                variete.retirer_stock(quantite_commande)
