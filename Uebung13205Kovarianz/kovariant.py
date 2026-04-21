import numpy as np

def kovarianz(listei: list[int], listej: list[int]):
    meanx = np.mean(listei)
    meany = np.mean(listej)
    return sum((x-meanx)*(y-meany) for x,y in zip(listei, listej))/len(listei)


