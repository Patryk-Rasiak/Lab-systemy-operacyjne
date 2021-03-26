from algorytmy import fcfs, srtf, rr
from random import randint, seed
from proces import Proces


def srednie_wyniki(kwant, ilosc_cykli, ilosc_procesow):

    seed(30)

    wyniki = {}
    procesy = []
    suma_fcfs = 0
    suma_srtf = 0
    suma_rr = 0
    
    for c in range(ilosc_cykli):
        for i in range(ilosc_procesow):
            a = randint(1, 29)
            proces = Proces(i, randint(0, 29), a, a, 0)
            procesy.append(proces)
            print(proces)

        print("\n\n\n")

        suma_fcfs += fcfs(procesy)
        suma_srtf += srtf(procesy)
        suma_rr += rr(kwant, procesy)

        procesy.clear()

    wynik_fcfs = round(suma_fcfs/ilosc_cykli, 2)
    wynik_srtf = round(suma_srtf/ilosc_cykli, 2)
    wynik_rr = round(suma_rr/ilosc_cykli, 2)

    wyniki["FCFS"] = wynik_fcfs
    wyniki["SRTF"] = wynik_srtf
    wyniki["RR"] = wynik_rr

    return wyniki
