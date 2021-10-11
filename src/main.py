import os
import eel
import numpy as np

input = None

eel.init('gui')


@eel.expose
def open_file_inut(txt):
    try:
        file1 = open("instances.csv", "w")
        file1.write(txt)
        file1.close()
        input = np.loadtxt("instances.csv", dtype='i', delimiter=',')
        eel.show_run(True)
    except:
        eel.show_run(False)


@eel.expose
def run_res_unit():
    input = np.loadtxt("instances.csv", dtype='i', delimiter=',')
    try:
        unitarias = [a.tolist() for a in input if (a == 0).sum() == (len(a)-1)]
        no_unitarias = [a.tolist()
                        for a in input if (a == 0).sum() < (len(a)-1)]

        size = len(unitarias)+len(no_unitarias)
        nsize = None

        nill = False

        ua = None
        ub = None

        hist = []

        while (not nill) and size != nsize:
            size = nsize or size
            # recorremos las unitarias
            for a in no_unitarias:
                if nill:
                    break
                for b in no_unitarias:
                    if nill:
                        break
                    ocurrences = 0
                    # revisar si son compatibles
                    for j in range(len(a)):
                        if a[j]+b[j] == 0 and b[j] != 0:
                            ocurrences += 1
                    if ocurrences == 1:
                        n = np.sum([a, b], axis=0)
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) == (len(a)-1):
                            unitarias.append(
                                n) if n not in unitarias else unitarias
                            hist.append(['unit', no_unitarias.index(
                                a)+1, no_unitarias.index(b)+1,  unitarias.index(n)+1])
                            # revisamos si hay contradicciones
                            for a1 in unitarias:
                                for b1 in unitarias:
                                    n1 = (np.sum([a1, b1], axis=0))
                                    if list(n1) == [0] * len(n1):
                                        nill = True
                                        ua = unitarias.index(a1)
                                        ub = unitarias.index(b1)
                                        break
                                if nill:
                                    break
                        else:
                            no_unitarias.append(
                                n) if n not in no_unitarias else no_unitarias
                            hist.append(['no unit', no_unitarias.index(
                                a)+1, no_unitarias.index(b)+1,  no_unitarias.index(n)+1])

            # recorremos las unitarias
            for a in unitarias:
                if nill:
                    break
                for b in no_unitarias:
                    if nill:
                        break
                    ocurrences = 0
                    # revisar si son compatibles
                    for j in range(len(a)):
                        if a[j]+b[j] == 0 and b[j] != 0:
                            ocurrences += 1
                    # si son compatibles crear el resultado
                    if ocurrences == 1:
                        n = np.sum([a, b], axis=0)
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) == (len(a)-1):
                            unitarias.append(
                                n) if n not in unitarias else unitarias
                            hist.append(['unit', 'u'+str(unitarias.index(
                                a)+1), no_unitarias.index(b)+1,  unitarias.index(n)+1])
                            # revisamos si hay contradicciones
                            for a1 in unitarias:
                                for b1 in unitarias:
                                    n1 = (np.sum([a1, b1], axis=0))
                                    if list(n1) == [0] * len(n1):
                                        nill = True
                                        ua = unitarias.index(a1)
                                        ub = unitarias.index(b1)
                                        break
                                if nill:
                                    break
                        else:
                            no_unitarias.append(
                                n) if n not in no_unitarias else no_unitarias
                            hist.append(['no unit', 'u'+str(unitarias.index(
                                a)+1), no_unitarias.index(b)+1,  no_unitarias.index(n)+1])

            nsize = len(unitarias)+len(no_unitarias)
        eel.show_res([unitarias, no_unitarias, nill,
                     ua, ub, input.tolist(), hist])
    except Exception as e:
        print(e)
        print(input)
        eel.show_run(True)


@eel.expose
def run_res_unit_rand():
    size = np.random.randint(low=1, high=10, size=(2,))
    input = np.random.randint(-1, high=2, size=(size[0], size[1]), dtype=int)
    try:
        unitarias = [a.tolist() for a in input if (a == 0).sum() == (len(a)-1)]
        no_unitarias = [a.tolist()
                        for a in input if (a == 0).sum() < (len(a)-1)]

        size = len(unitarias)+len(no_unitarias)
        nsize = None

        nill = False

        ua = None
        ub = None

        hist = []

        while (not nill) and size != nsize:
            size = nsize or size
            # recorremos las unitarias
            for a in no_unitarias:
                if nill:
                    break
                for b in no_unitarias:
                    if nill:
                        break
                    ocurrences = 0
                    # revisar si son compatibles
                    for j in range(len(a)):
                        if a[j]+b[j] == 0 and b[j] != 0:
                            ocurrences += 1
                    if ocurrences == 1:
                        n = np.sum([a, b], axis=0)
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) == (len(a)-1):
                            unitarias.append(
                                n) if n not in unitarias else unitarias
                            hist.append(['unit', no_unitarias.index(
                                a)+1, no_unitarias.index(b)+1,  unitarias.index(n)+1])
                            # revisamos si hay contradicciones
                            for a1 in unitarias:
                                for b1 in unitarias:
                                    n1 = (np.sum([a1, b1], axis=0))
                                    if list(n1) == [0] * len(n1):
                                        nill = True
                                        ua = unitarias.index(a1)
                                        ub = unitarias.index(b1)
                                        break
                                if nill:
                                    break
                        else:
                            no_unitarias.append(
                                n) if n not in no_unitarias else no_unitarias
                            hist.append(['no unit', no_unitarias.index(
                                a)+1, no_unitarias.index(b)+1,  no_unitarias.index(n)+1])

            # recorremos las unitarias
            for a in unitarias:
                if nill:
                    break
                for b in no_unitarias:
                    if nill:
                        break
                    ocurrences = 0
                    # revisar si son compatibles
                    for j in range(len(a)):
                        if a[j]+b[j] == 0 and b[j] != 0:
                            ocurrences += 1
                    # si son compatibles crear el resultado
                    if ocurrences == 1:
                        n = np.sum([a, b], axis=0)
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) == (len(a)-1):
                            unitarias.append(
                                n) if n not in unitarias else unitarias
                            hist.append(['unit', 'u'+str(unitarias.index(
                                a)+1), no_unitarias.index(b)+1,  unitarias.index(n)+1])
                            # revisamos si hay contradicciones
                            for a1 in unitarias:
                                for b1 in unitarias:
                                    n1 = (np.sum([a1, b1], axis=0))
                                    if list(n1) == [0] * len(n1):
                                        nill = True
                                        ua = unitarias.index(a1)
                                        ub = unitarias.index(b1)
                                        break
                                if nill:
                                    break
                        else:
                            no_unitarias.append(
                                n) if n not in no_unitarias else no_unitarias
                            hist.append(['no unit', 'u'+str(unitarias.index(
                                a)+1), no_unitarias.index(b)+1,  no_unitarias.index(n)+1])

            nsize = len(unitarias)+len(no_unitarias)
        eel.show_res([unitarias, no_unitarias, nill,
                     ua, ub, input.tolist(), hist])
    except Exception as e:
        print(e)
        print(input)
        eel.show_run(True)


eel.start('index.html')
