import copy
from proces import Proces


def fcfs(procesy):

    procesy1 = copy.deepcopy(procesy)

    procesy1.sort(key=lambda x: x.moment_wejscia)

    calkowity_czas_oczekiwania = 0
    calkowity_czas_zakonczenia = procesy[0].dlugosc_fazy

    for i in range(1, len(procesy1)):

        proces = procesy1[i]

        if calkowity_czas_zakonczenia <= proces.moment_wejscia:
            calkowity_czas_zakonczenia = proces.moment_wejscia + proces.dlugosc_fazy

        else:
            calkowity_czas_oczekiwania += calkowity_czas_zakonczenia - proces.moment_wejscia
            calkowity_czas_zakonczenia += proces.dlugosc_fazy
    return calkowity_czas_oczekiwania / len(procesy1)


def srtf(procesy):

    kolejka = []
    czas_aktualny = 0
    calkowity_czas_oczekiwania = 0

    procesy1 = copy.deepcopy(procesy)

    procesy1.sort(key=lambda x: x.moment_wejscia)

    while True:
        for proces in procesy1:
            if czas_aktualny == proces.moment_wejscia:
                kolejka.append(Proces(0, 0, 0, proces.czas_pozostaly, 0))

                kolejka.sort(key=lambda x: x.czas_pozostaly)

        czas_aktualny += 1

        if len(kolejka) != 0:
            kolejka[0].czas_pozostaly -= 1

            for j in range(1, len(kolejka)):
                kolejka[j].czas_oczekiwania += 1

            if kolejka[0].czas_pozostaly == 0:
                calkowity_czas_oczekiwania += kolejka[0].czas_oczekiwania
                kolejka.pop(0)

        if czas_aktualny == 100000:
            break

    return calkowity_czas_oczekiwania / len(procesy)


def rr(k, procesy):

    kwant = 0
    czas_akutalny = 0
    calkowity_czas_oczekiwania = 0
    kolejka = []

    procesy1 = copy.deepcopy(procesy)

    procesy1.sort(key=lambda x: x.moment_wejscia)

    while True:

        for proces in procesy1:

            if czas_akutalny == proces.moment_wejscia:
                kolejka.append(Proces(0, proces.moment_wejscia, 0, proces.czas_pozostaly, 0))

        if kwant <= 0 and len(kolejka) != 0:

            if kolejka[0].czas_pozostaly == 0:
                calkowity_czas_oczekiwania += kolejka[0].czas_oczekiwania
                kolejka.pop(0)
                kolejka.sort(key=lambda x: (x.numer_procesu, x.moment_wejscia))

                if len(kolejka) != 0:
                    kolejka[0].numer_procesu += 1

                    if kolejka[0].czas_pozostaly >= k:
                        kwant = k
                    else:
                        kwant = kolejka[0].czas_pozostaly

            else:

                if len(kolejka) == 1:
                    kolejka[0].numer_procesu += 1

                else:

                    kolejka.append(kolejka[0])
                    kolejka.pop(0)
                    kolejka.sort(key=lambda x: (x.numer_procesu, x.moment_wejscia))
                    kolejka[0].numer_procesu += 1

                if kolejka[0].czas_pozostaly >= k:
                    kwant = k
                else:
                    kwant = kolejka[0].czas_pozostaly

        if len(kolejka) != 0:
            kolejka[0].czas_pozostaly -= 1

            for i in range(1, len(kolejka)):
                kolejka[i].czas_oczekiwania += 1

        czas_akutalny += 1
        kwant -= 1

        if czas_akutalny == 100000:
            break

    return calkowity_czas_oczekiwania / len(procesy1)



