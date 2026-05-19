# hello.py (version compatible Jenkins)
import sys

print("=" * 40)
print("Bienvenue dans mon premier job Jenkins !")
print("=" * 40)

# Nom passé en argument, sinon valeur par défaut
if len(sys.argv) > 1:
    nom = sys.argv[1]
else:
    nom = "Etudiant Jenkins"

print(f"Bonjour {nom}, ton job Jenkins a reussi !")

# Petit calcul
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")

# Test automatique
assert a + b == 15, "Le test a echoue !"
print("Tous les tests passent avec succes !")