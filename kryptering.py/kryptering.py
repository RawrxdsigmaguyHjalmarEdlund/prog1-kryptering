meddelande = input("Skriv ditt meddelande!! ")
for i in range(len(list(meddelande))):
    print("abcdefghijklmnopqrstuvwxyzåäö"[(list("abcdefghijklmnopqrstuvwxyzåäö").index(list(meddelande)[i])+60) % len("abcdefghijklmnopqrstuvwxyzåäö")])