nyckel = input("Skriv din nyckel ")
meddelande = input("Skriv ditt meddelande ")
alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
nyckel = nyckel.lower()
meddelande = meddelande.lower()

output = []
nyckel_index = 0
for i in meddelande:
    if i in alfabet:
        skift = alfabet.index(nyckel[nyckel_index % len(nyckel)])
        alfabetpos = alfabet.index(i)
        nypos = (alfabetpos + skift) % len(alfabet)
        output.append(alfabet[nypos])
        nyckel_index += 1
    else:
        output.append(i)

print("".join(output))