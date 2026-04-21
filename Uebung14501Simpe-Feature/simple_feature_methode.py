def simple_feature(daten: list[int]) -> list:
    max_wert = max(daten)
    return [x/max_wert for x in daten]

print(simple_feature([1,2,3]))