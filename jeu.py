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
