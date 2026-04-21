liste = input("Gib eine Liste ein, getrennt durch Komma: ").strip().split(",")
dic_modus = {}

for x in liste:
    if x not in dic_modus:
        dic_modus[x] = 1
    else:
        dic_modus[x] += 1
modus_value = max(dic_modus.values())

for k,v in dic_modus.items():
    if v == modus_value:
        modus = k
        break
    else:
        modus = 0


print(f"Modus: {modus}")