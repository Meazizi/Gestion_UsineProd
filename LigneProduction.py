class LigneProduction:
    def __init__(self, nom, ordre_en_cours=None):
        self.nom = nom
        self.ordre_en_cours = ordre_en_cours  # Type : OrdreProduction
        self.variete_actuelle = None  # VarietePate actuellement produite

    def change_variete(self, nouvel_ordre):
        """
        Change la variété de pâte à produire en fonction du nouvel ordre.
        Si une variété était déjà en production, applique le temps de setup avant de changer.

        :param nouvel_ordre: OrdreProduction - Le nouvel ordre de production à affecter.
        """
        if self.ordre_en_cours and self.variete_actuelle:
            # Calculer le temps de setup nécessaire
            temps_setup = self.variete_actuelle.obtenir_temps_setup()
            print(
                f"Changement de variété : Temps de nettoyage nécessaire ({temps_setup} jours)"
            )
        else:
            print("Aucun temps de setup nécessaire (première production).")

        # Mettre à jour la variété actuelle et l'ordre en cours
        self.ordre_en_cours = nouvel_ordre
        self.variete_actuelle = nouvel_ordre.variete
        print(
            f"Nouvelle variété en production sur la ligne {self.nom} : {self.variete_actuelle.nom}"
        )
