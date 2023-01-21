cont = 0
while True:
    print('Questão 1:\nO Brasil pertence a qual continente:')
    print('EUROPEU\nASIÁTICO\nAMERICANO\nAFRICANO')
    questão_1 = str(input('Qual é a sua resposta? ')).strip().upper()
    if questão_1 == 'AMERICANO':
        print('Resposta correta! Parabéns!')
        cont += 1
        break
    else:
        print('Você errou. Que pena.')
        break
while True:
    print('Questão 2:\nQual é o maior pais da América Latina?')
    print('ESTADOS UNIDOS\nARGENTINA\nBRASIL\nPARAGUAI')
    questão_2 = str(input('Qual é a sua resposta? ')).strip().upper()
    if questão_2 == 'BRASIL':
        print('Resposta correta! Parabéns!')
        cont += 1
        break
    else:
        print('Você errou. Que pena.')
        break
while True:
    print('Questão 3:\nQual destes países não pertence a América do Sul:')
    print('BASIL\nURUGUAI\nCUBA\nARGENTINA')
    questão_3 = str(input('Qual é a sua resposta? ')).strip().upper()
    if questão_3 == 'CUBA':
        print('Resposta correta!Parabéns!')
        cont += 1
        break
    else:
        print('Você errou. Que pena')
        break
print(f'Você acertou {cont} questões')
