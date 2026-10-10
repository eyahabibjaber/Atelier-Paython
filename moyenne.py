# Lecture de la moyenne
m = float(input("Donner la moyenne (entre 0 et 20) : "))

# Vérification de la contrainte de borne
while m < 0 or m > 20:
    print("Erreur ! La moyenne doit être entre 0 et 20.")
    m = float(input("Donner la moyenne : "))

# Détermination de la mention
if m >= 16:
    print("Très bien")
elif m >= 14:
    print("Bien")
elif m >= 12:
    print("Assez bien")
elif m >= 10:
    print("Passable")
else:
    print("Ajourné")
