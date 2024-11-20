class PlanProduction:
    def __init__(self):
        self.ordres = []  # Liste de OrdreProduction

    def ajouter_ordre(self, ordre):
        self.ordres.append(ordre)

    def afficher_plan(self):
        for ordre in self.ordres:
            ordre.afficher_ordre()
