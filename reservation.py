
# Lire l'age et le convertir en entier
iAge = int (input("donner votre age"))

#Lire O/N le transformer en majuscule et le comparer a 'O'
#bJournee devient booleenne
bJournee= input (" seance en journee ?( O | N )").upper() == "O";

if (iAge < 18 or iAge > 65 ) and bJournee :
    print (" tarif reduit ")
else :
    print ( " tarif normal ")
    
  