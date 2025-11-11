class CompteBancaire:
    """
    Classe CompteBancaire illustrant les principes d'encapsulation en Python :
    - attribut protégé : _titulaire
    - attribut privé : __solde
    - propriété en lecture seule : solde
    """

    def __init__(self, titulaire, solde_initial=0):
        # Attribut protégé : accessible dans les sous-classes
        self._titulaire = titulaire
        # Attribut privé : inaccessible directement depuis l’extérieur
        self.__solde = solde_initial

    def deposer(self, montant):
        """Ajoute de l'argent au solde si le montant est valide."""
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        """Retire de l'argent si le solde est suffisant."""
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        """Propriété en lecture seule représentant le solde."""
        return self.__solde

    def __str__(self):
        """Affichage lisible du compte."""
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    # Tentative de modification directe
    compte.solde = 500  # Ne fonctionnera pas
