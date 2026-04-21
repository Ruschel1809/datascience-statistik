zahlenliste = input("Gib eine Liste von Zahlen ein, getrennt durch Komma: ").strip().split(",")
int_list = [int(x) for x in zahlenliste]
print(int_list)
sorted_list = sorted(int_list)
print(sorted_list)
n = len(sorted_list)
if n % 2 == 0:
    median = (sorted_list[(n // 2) - 1 ]+ sorted_list[ n // 2]) / 2
elif len(zahlenliste) % 2 == 1:
    median = sorted_list[n // 2]
else:
    median = 0
    print("Fehler")
print("Median: ", median)