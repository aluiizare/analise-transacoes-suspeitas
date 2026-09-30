import csv

with open("transacoes.csv", "r", encoding="utf-8") as arquivo:
    transacoes = csv.DictReader(arquivo)

    for transacao in transacoes:
        print(transacao)
