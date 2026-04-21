def min_max_skalierung(daten: list[int])-> list[float]:
    max_wert = max(daten)
    min_wert = min(daten)
    return [(x-min_wert)/(max_wert-min_wert) for x in daten]

print(min_max_skalierung([1,2,3]))