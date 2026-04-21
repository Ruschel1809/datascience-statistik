import math

# zahlenliste = input("Gib eine Liste von Zahlen ein, getrennt durch Komma: ").strip().split(",")
# int_list = [int(x) for x in zahlenliste]


def durchschnitt(liste: list[int]) -> float:
    mittelwert = 0
    for x in liste:
        mittelwert += x
    mittelwert /= len(liste)
    return mittelwert

def wahr(liste: list[int]):
    haeufigkeit = {}
    for x in liste:
        if x not in haeufigkeit:
            haeufigkeit[x] = 1
        else:
            haeufigkeit[x] += 1
    return {k: v / len(liste) for k, v in haeufigkeit.items()}


def varianz (abweichung: list[int]) -> float:
    mittelwert = durchschnitt(abweichung)
    wahrscheinlichkeit = wahr(abweichung)
    # Nur über eindeutige Werte iterieren!
    return sum((x - mittelwert) ** 2 * p for x, p in wahrscheinlichkeit.items())

def varianz_gleichverteilt(abweichung: list[int]) -> float:
    mittelwert = durchschnitt(abweichung)
    return sum((x-mittelwert)**2 for x in abweichung)/len(abweichung)

def varianz_gleichverteilt_stichprobe(abweichung: list[int]) -> float:
    mittelwert = durchschnitt(abweichung)
    return sum((x - mittelwert) ** 2 for x in abweichung) / (len(abweichung)-1)

def standardabweichung(varianz):
    return math.sqrt(varianz)

liste = [2, 3, 7, 5, 3]

print("Varianz (korrekt gewichtet):", varianz(liste))
print("Standardabweichung (korrekt gewichtet):", standardabweichung(varianz(liste)))

print("Varianz (gleichverteilt):", varianz_gleichverteilt(liste))
print("Standardabweichung (gleichverteilt):", standardabweichung(varianz_gleichverteilt(liste)))