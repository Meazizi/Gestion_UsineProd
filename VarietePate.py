class VarietePate:
    def __init__(self, nom, temps_setup, cartons_par_jour, stock_initial):
        self.nom = nom
        self.temps_setup = temps_setup
        self.cartons_par_jour = cartons_par_jour
        self.stock_initial = stock_initial

    def obtenir_temps_setup(self):
        return self.temps_setup
