import numpy as np

# leer archivo
# input = np.loadtxt("D:\Documents\GitHub\Res_unit\instance.txt",dtype='i', delimiter=',')

# matriz aleatoria
size = np.random.randint(low=0, high=10, size=(2,))
input = np.random.randint(-1, high=2, size=(size[0], size[1]), dtype=int)

print(input)

unitarias = [a.tolist() for a in input if (a == 0).sum() == (len(a)-1)]

no_unitarias = [a.tolist() for a in input if (a == 0).sum() < (len(a)-1)]

print(unitarias)
print(no_unitarias)

size = len(unitarias)+len(no_unitarias)
nsize = None

nill = False

ua = None
ub = None

while (not nill) and size != nsize:
    size = nsize or size
    # recorremos las unitarias
    for a in no_unitarias:
        for b in no_unitarias:
            ocurrences = 0
            # revisar si son compatibles
            for j in range(len(a)):
                if a[j]+b[j] == 0 and b[j] != 0:
                    ocurrences += 1
            # si son compatibles crear el resultado
            if ocurrences == 1:
                n = []
                for j in range(len(a)):
                    n.append(a[j]+b[j])
                n = np.clip(n, -1, 1).tolist()
                if n.count(0) == (len(a)-1):
                    unitarias.append(n) if n not in unitarias else unitarias
                else:
                    no_unitarias.append(
                        n) if n not in no_unitarias else no_unitarias

    # recorremos las unitarias
    for a in unitarias:
        for b in no_unitarias:
            ocurrences = 0
            # revisar si son compatibles
            for j in range(len(a)):
                if a[j]+b[j] == 0 and b[j] != 0:
                    ocurrences += 1
            # si son compatibles crear el resultado
            if ocurrences == 1:
                n = []
                for j in range(len(a)):
                    n.append(a[j]+b[j])
                n = np.clip(n, -1, 1).tolist()
                if n.count(0) == (len(a)-1):
                    unitarias.append(n) if n not in unitarias else unitarias
                else:
                    no_unitarias.append(
                        n) if n not in no_unitarias else no_unitarias

    # revisamos si hay contradicciones
    for a in unitarias:
        for b in unitarias:
            n = (np.sum([a, b], axis=0))
            if list(n) == [0] * len(n):
                nill = True
                ua = unitarias.index(a)
                ub = unitarias.index(b)
                break
        if nill:
            break

    nsize = len(unitarias)+len(no_unitarias)

print('***********************************************')
print(unitarias)
print(no_unitarias)
print(nill)
print(ua)
print(ub)
