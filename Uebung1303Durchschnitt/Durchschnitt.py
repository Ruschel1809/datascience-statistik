zahlenliste = input("Gib eine Liste von Zahlen ein, getrennt durch Komma: ").strip().split(",")
int_list = [int(x) for x in zahlenliste]

durchschnitt = 0
for x in int_list:
    durchschnitt += x
durchschnitt /= len(int_list)
print(f"\nDurchschnitt: {durchschnitt}")