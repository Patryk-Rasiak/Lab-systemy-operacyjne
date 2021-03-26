class Proces:

    def __init__(self, numer_procesu, moment_wejscia, dlugosc_fazy, czas_pozostaly, czas_oczekiwania):
        self.numer_procesu = numer_procesu
        self.moment_wejscia = moment_wejscia
        self.dlugosc_fazy = dlugosc_fazy
        self.czas_pozostaly = czas_pozostaly
        self.czas_oczekiwania = czas_oczekiwania

    def __str__(self):
        return f"Numer procesu: {self.numer_procesu}, " \
               f"moment wejścia: {self.moment_wejscia}, " \
               f"długość fazy: {self.dlugosc_fazy}, " \
               f"pozostały czas: {self.czas_pozostaly}, " \
               f"czas oczekiwania: {self.czas_oczekiwania}"
