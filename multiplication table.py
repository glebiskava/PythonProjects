import os

a = int(input("Gib eine Zahl ein, die multipliziert werden soll: "))
b = int(input("Gib ein, bis zu welchen Wert deine Zahl multipliziert werden soll: "))

def table(nb, maximum):
    i = 1 
    maximum = maximum + 1
    while i < maximum:
        print(f"{i} * {nb} = {i * nb}")
        i += 1

table(a, b)

while True:
    print("Willst du noch eine Zahl multipliziert haben?")

    Wahl = int(input("Gib 1 für 'Ja' ein und 0 für 'Nein' ein: "))

    if Wahl == 1:
        table(int(input("Gib eine Zahl ein, die multipliziert werden soll: ")), int(input("Gib ein, bis zu welchen Wert deine Zahl multipliziert werden soll: ")))
    else:
         print("Make it good!")

os.system("pause")

      





