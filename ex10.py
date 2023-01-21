salário = float(input('Salário: '))
limite = salário * 0.3
capital = float(input('Valor do financiamento: '))
taxa = float(input('Taxa de juros: '))
tempo = int(input('Período: '))
montante = capital * (1 + taxa)**tempo
juros = montante - capital
parcela = juros / tempo
if limite > parcela:
    print('Parabéns, seu financiamento foi aprovado!')
    print(f'Valor financiado: R${capital:.2f}\nPeríodo: {tempo} meses\nParcelas: R${parcela:.2f}\n'
          f'Valor final: R${montante:.2f} ')
else:
    print('Infelizmente seu financiamento não foi aprovado.')
print('FIM')
