import pandas as pd


def z_score_skalierung(daten: list[int]) -> list[float]:
    ds = pd.Series(daten)
    return [float((x-ds.mean())/ds.std()) for x in daten] #kast auf float, sonst kommt er als np.float zurück für doppelte Genauigkeit, aber das brauche ich jetzt nicht
print(z_score_skalierung([1,2,3,4,5,6]))
