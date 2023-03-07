import URL_requests as url


# Cores
cor_preto = "#3b3b3b"  # Preto
cor_branco = "#ffffff"  # Branco
cor_azul = "#38576b"  # Azul
cor_cinza = "#ECEFF1"  # Cinza
cor_laranja = "#FFAB40"  # Laranja


def BuscarCotas():
    url.dolar_reais_hoje()
    url.BTC_Real()
    Bitcoin = url.BTCCota
    Dolar = url.dollar_hoje
