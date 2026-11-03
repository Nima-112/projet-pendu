import random
import unicodedata
 
MOTS = [
    "python", "ordinateur", "clavier", "souris", "programme",
    "variable", "fonction", "algorithme", "internet", "reseau",
    "fichier", "dossier", "boucle", "condition", "projet",
]
 
MAX_ERREURS = 7
 
 
def normaliser(texte):
    """Met en minuscules et retire les accents (é -> e)."""
    texte = unicodedata.normalize("NFD", texte.lower())
    return "".join(c for c in texte if unicodedata.category(c) != "Mn")
 
 
def choisir_mot():
    """Retourne un mot au hasard dans la liste MOTS."""
    return random.choice(MOTS)
class Pendu:
    """Représente une partie de pendu."""
 
    def __init__(self, mot, max_erreurs=MAX_ERREURS):
        self.mot = normaliser(mot)
        self.max_erreurs = max_erreurs
        self.lettres_trouvees = set()
        self.lettres_ratees = []
 
    @property
    def erreurs(self):
        return len(self.lettres_ratees)
 
    def proposer(self, lettre):
        """Traite une proposition.
 
        Retourne : "invalide", "deja", "bon" ou "mauvais".
        """
        lettre = normaliser(lettre)
        if len(lettre) != 1 or not lettre.isalpha():
            return "invalide"
        if lettre in self.lettres_trouvees or lettre in self.lettres_ratees:
            return "deja"
        if lettre in self.mot:
            self.lettres_trouvees.add(lettre)
            return "bon"
        self.lettres_ratees.append(lettre)
        return "mauvais"
