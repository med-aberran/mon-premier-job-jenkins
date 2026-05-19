# hello.py (version sans input)
import sys

print("=" * 40)
print("Bienvenue dans mon premier job Jenkins !")
print("=" * 40)

# On utilise un argument ou une variable par défaut
if len(sys.argv) > 1:
    nom = sys.argv[1]
else:
    nom = "Étudiant Jenkins"

print(f"Bonjour {nom}, ton job Jenkins a réussi !")

# Petit calcul
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")

# Simuler un test
assert a + b == 15, "Le test a échoué !"
print("✅ Tous les tests passent avec succès")
