alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = "hej"
nyckel = 1
alfabetl=list(alfabet)
meddelandel=list(meddelande)
for i in range(len(meddelandel)):
    print(alfabet[alfabetl.index(meddelandel[i])+nyckel])