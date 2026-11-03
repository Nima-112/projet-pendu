"""main.py - Point d'entrée : relie l'affichage (A) et les règles (B)."""
import affichage
import jeu
 
 
def jouer_une_partie():
    partie = jeu.Pendu(jeu.choisir_mot())
    affichage.afficher_titre()
 
    while not partie.est_termine():
        affichage.afficher_etat(
            partie.mot_affiche(),
            partie.lettres_ratees,
            partie.erreurs,
            partie.max_erreurs,
        )
        lettre = affichage.demander_lettre()
        statut = partie.proposer(lettre)
        affichage.afficher_message(statut)
 
    affichage.afficher_etat(
        partie.mot_affiche(), partie.lettres_ratees,
        partie.erreurs, partie.max_erreurs,
    )
    if partie.est_gagne():
        affichage.afficher_victoire(partie.mot)
    else:
        affichage.afficher_defaite(partie.mot)
 
 
def main():
    jouer_une_partie()
    while affichage.demander_rejouer():
        jouer_une_partie()
    print("Merci d'avoir joué !")
 
 
if __name__ == "__main__":
    main()
