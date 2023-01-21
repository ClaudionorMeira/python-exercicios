print('-%' * 30)
print(f'{"TABELA DE JUROS SIMPLES":>40}')
print('-%' * 30)
salário = float(input('Salário: '))
capital = float(input('Valor proposto: '))
taxa = float(input('Taxa de juros: '))
tempo = int(input('Nº Parcelas: '))
juros = capital * taxa * tempo
total = capital + juros
limite = salário * 0.3
valor = juros / tempo
if limite > valor:
    print('Seu financiamento foi aprovado!')
    print(f'Valor do financiamento: R${capital:.2f}\nPeríodo: {tempo} meses.')
    print(f'Valor das parcelas: R${valor:.2f}\nValor total dos juros: R${juros:.2f}')
    print(f'Valor total do financiamento: R${total}')
else:
    print('Infelizmente seu financiamento não foi aprovado.')
