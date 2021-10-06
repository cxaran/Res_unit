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
        print(input)
        eel.show_run(True)
    except:
        eel.show_run(False)


@eel.expose
def run_res_unit():
    try:
        input = np.loadtxt("instances.csv", dtype='i', delimiter=',')
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
                        # comprueba si se pueden elimnar
                        if a[j]+b[j] == 0 and b[j] != 0:
                            # guardar el numero de variables que se pueden eliminar
                            ocurrences += 1
                    # si son compatibles crear el resultado
                    # if ocurrences == 1:
                    if ocurrences >= 1:
                        n = []
                        for j in range(len(a)):
                            n.append(a[j]+b[j])
                        n = np.clip(n, -1, 1).tolist()
                        print(n)
                        if n.count(0) < (len(a)):
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
                        n = []
                        for j in range(len(a)):
                            n.append(a[j]+b[j])
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) == (len(a)-1):
                            unitarias.append(
                                n) if n not in unitarias else unitarias
                            hist.append(['unit', 'u'+(unitarias.index(
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
                            hist.append(['no unit', 'u'+(unitarias.index(
                                a)+1), no_unitarias.index(b)+1,  no_unitarias.index(n)+1])

            # # revisamos si hay contradicciones
            # for a in unitarias:
            #     for b in unitarias:
            #         n = (np.sum([a, b], axis=0))
            #         if list(n) == [0] * len(n):
            #             nill = True
            #             ua = unitarias.index(a)
            #             ub = unitarias.index(b)
            #             break
            #     if nill:
            #         break

            nsize = len(unitarias)+len(no_unitarias)
        print([unitarias, no_unitarias, nill, ua, ub])
        eel.show_res([unitarias, no_unitarias, nill,
                     ua, ub, input.tolist(), hist])
    except:
        eel.show_run(True)


@eel.expose
def run_res_unit_rand():
    try:
        size = np.random.randint(low=1, high=8, size=(2,))
        input = np.random.randint(-1, high=2,
                                  size=(size[0], size[1]), dtype=int)
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
                        # comprueba si se pueden elimnar
                        if a[j]+b[j] == 0 and b[j] != 0:
                            # guardar el numero de variables que se pueden eliminar
                            ocurrences += 1
                    # si son compatibles crear el resultado
                    # if ocurrences == 1:
                    if ocurrences >= 1:
                        n = []
                        for j in range(len(a)):
                            n.append(a[j]+b[j])
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) < (len(a)):
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
                        n = []
                        for j in range(len(a)):
                            n.append(a[j]+b[j])
                        n = np.clip(n, -1, 1).tolist()
                        if n.count(0) == (len(a)-1):
                            unitarias.append(
                                n) if n not in unitarias else unitarias
                            hist.append(['unit', 'u'+(unitarias.index(
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
                            hist.append(['no unit', 'u'+(unitarias.index(
                                a)+1), no_unitarias.index(b)+1,  no_unitarias.index(n)+1])

            # # revisamos si hay contradicciones
            # for a in unitarias:
            #     for b in unitarias:
            #         n = (np.sum([a, b], axis=0))
            #         if list(n) == [0] * len(n):
            #             nill = True
            #             ua = unitarias.index(a)
            #             ub = unitarias.index(b)
            #             break
            #     if nill:
            #         break

            nsize = len(unitarias)+len(no_unitarias)
        print([unitarias, no_unitarias, nill, ua, ub])
        eel.show_res([unitarias, no_unitarias, nill,
                     ua, ub, input.tolist(), hist])
    except:
        eel.show_run(True)


eel.start('index.html')
