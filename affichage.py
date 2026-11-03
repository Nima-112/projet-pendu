"""affichage.py - Affichage du jeu du pendu (Personne A).
 
Ce module ne contient AUCUNE règle du jeu : il reçoit des valeurs
et les affiche (print) ou lit le clavier (input).
"""
 
DESSINS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]
 
 
def afficher_titre():
    print("=" * 40)
    print("        JEU DU PENDU")
    print("=" * 40)

def afficher_etat(mot_affiche, lettres_ratees, erreurs, max_erreurs):
    """Affiche le dessin, le mot masqué et les lettres ratées."""
    index = min(erreurs * (len(DESSINS) - 1) // max_erreurs, len(DESSINS) - 1)
    print(DESSINS[index])
    print()
    print("Mot :", mot_affiche)
    print("Lettres ratées :", " ".join(lettres_ratees) if lettres_ratees else "-")
    print("Erreurs : {}/{}".format(erreurs, max_erreurs))

def demander_lettre():
    return input("\nProposez une lettre : ").strip()
 
 
def afficher_message(statut):
    messages = {
        "invalide": "Saisie invalide : tapez UNE seule lettre.",
        "deja": "Vous avez déjà essayé cette lettre.",
        "bon": "Bien vu, la lettre est dans le mot !",
        "mauvais": "Raté, cette lettre n'est pas dans le mot.",
    }
    print(messages.get(statut, ""))
 
 
def afficher_victoire(mot):
    print("\nBRAVO ! Vous avez trouvé le mot :", mot)
 
 
def afficher_defaite(mot):
    print("\nPERDU ! Le mot était :", mot)
 
 
def demander_rejouer():
    return input("\nRejouer ? (o/n) : ").strip().lower() == "o"
