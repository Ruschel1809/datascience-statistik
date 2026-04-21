import math

def berechne_entropie(p_list):
    entropie = 0
    for p in p_list:
        if p > 0:
            entropie += p * math.log2(1 / p)
    return entropie

def ist_gueltige_verteilung(p_list):
    summe = sum(p_list)
    return abs(summe - 1.0) < 1e-6  # Toleranz wegen Rundungsfehlern

def main():
    print("Entropie-Rechner")
    print("Gib Wahrscheinlichkeiten ein, getrennt durch Leerzeichen (z.B.: 0.5 0.25 0.25):")

    eingabe = input("> ")
    try:
        p_list = [float(p) for p in eingabe.strip().split()]
    except ValueError:
        print("Fehler: Bitte nur gültige Zahlen eingeben.")
        return

    if not all(0 <= p <= 1 for p in p_list):
        print("Fehler: Alle Wahrscheinlichkeiten müssen zwischen 0 und 1 liegen.")
        return

    if not ist_gueltige_verteilung(p_list):
        print("Fehler: Die Wahrscheinlichkeiten müssen sich zu 1 summieren.")
        return

    entropie = berechne_entropie(p_list)
    print(f"Entropie H = {entropie:.4f} Bit")

if __name__ == "__main__":
    main()

