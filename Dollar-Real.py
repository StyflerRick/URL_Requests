import URL_requests as URL

URL.dolar_reais_hoje()

while True:
    valor = input('Quantos reais deseja converter em dolar?')
    try:
        valor = float(valor)
        print('Com R${:.2f} dá para comprar ${:.2f}'.format(
            valor, round(valor/URL.dollar_hoje, 2)))
        break
    except ValueError:
        print('O Valor inserido não é permitido. Somente números e ponto')
    except TypeError:
        print('O Valor inserido não é permitido. Somente números e ponto')
