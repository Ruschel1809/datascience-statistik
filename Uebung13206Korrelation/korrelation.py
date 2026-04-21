import numpy as np


def kovarianz(listei: list[int], listej: list[int]):
    meanx = np.mean(listei)
    meany = np.mean(listej)
    return sum((x-meanx)*(y-meany) for x,y in zip(listei, listej))/(len(listei)-1)

def korrelation(listei: list[int], listej: list[int]):
    kov = kovarianz(listei, listej)
    abweichugni = np.std(listei)
    abweichungj = np.std(listej)
    return kov/(abweichugni*abweichungj)


liste1 = [170,180,190]
liste2 = [42,44,43]

print("Mittelwert Körper: ", np.mean(liste1))
print("Mittelwert Schuh: ", np.mean(liste2))
print("STD Körper: ", np.std(liste1))
print("STD Schuh: ", np.std(liste2))
print("Kovarianz: ", kovarianz(liste1, liste2))
print("Korrelation: ", korrelation(liste1, liste2))