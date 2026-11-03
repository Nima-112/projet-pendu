"""test_jeu.py - Tests unitaires des règles (Personne B)."""
import unittest
from jeu import Pendu, normaliser
 
 
class TestPendu(unittest.TestCase):
    def test_normaliser(self):
        self.assertEqual(normaliser("Été"), "ete")
 
    def test_bonne_lettre(self):
        p = Pendu("python")
        self.assertEqual(p.proposer("p"), "bon")
        self.assertEqual(p.mot_affiche(), "p _ _ _ _ _")
 
    def test_mauvaise_lettre(self):
        p = Pendu("python")
        self.assertEqual(p.proposer("z"), "mauvais")
        self.assertEqual(p.erreurs, 1)
 
    def test_lettre_deja_jouee(self):
        p = Pendu("python")
        p.proposer("z")
        self.assertEqual(p.proposer("z"), "deja")
        self.assertEqual(p.erreurs, 1)
 
    def test_saisie_invalide(self):
        p = Pendu("python")
        self.assertEqual(p.proposer("ab"), "invalide")
        self.assertEqual(p.proposer("1"), "invalide")
        self.assertEqual(p.proposer(""), "invalide")
 
    def test_victoire(self):
        p = Pendu("pi")
        p.proposer("p")
        p.proposer("i")
        self.assertTrue(p.est_gagne())
        self.assertTrue(p.est_termine())
 
    def test_defaite(self):
        p = Pendu("python", max_erreurs=2)
        p.proposer("z")
        p.proposer("x")
        self.assertTrue(p.est_perdu())
 
 
if __name__ == "__main__":
    unittest.main()
