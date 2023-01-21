cont = 0
melhor_média = 0
pior_média = 0
melhor_aluno = ''
print('¨' * 35)
print(f'{"ANO LETIVO 2022":^35}')
print('¨' * 35)
print(f'{"MÉDIA FINAL":^35}')
print('¨' * 35)
for est in range(1, 4):
    aluno = str(input('ALUNO: ')).strip().upper()
    série = int(input('SÉRIE: '))
    turma = str(input('TURMA: ')).upper()[0]
    matéria = str(input('DISCIPLINA: ')).strip().upper()[:3]
    nota_1 = float(input('PROVA_1: '))
    nota_2 = float(input('PROVA_2: '))
    nota_3 = float(input('PROVA_3: '))
    média = (nota_1 + nota_2 + nota_3) / 3
    cont += 1

    if média >= 7:
        print(f'ALUNO: {aluno}\nSérie: {série}ª\nTurma: {turma}')
        print(f'DISCIPLINA: {matéria}')
        print(f'MÉDIA FINAL: {média:.1f}')
        print('SITUAÇÃO DO ALUNO: APROVADO!')
    elif 5 <= média <= 6.9:
        print(f'ALUNO: {aluno}')
        print(f'DISCIPLINA: {matéria}')
        print(f'MÉDIA FINAL: {média:.1f}')
        print('SITUAÇÃO DO ALUNO: RECUPERAÇÃO')
    else:
        print(f'ALUNO: {aluno}')
        print(f'DISCIPLINA: {matéria}')
        print(f'MÉDIA FINAL: {média:.1f}')
        print('SITUAÇÃO DO ALUNO: REPROVADO')
    if est == 1:
        melhor_média = média
        pior_média = média
        melhor_aluno = aluno
    else:
        if média > melhor_média:
            melhor_média = média
            melhor_aluno = aluno
        if média < pior_média:
            pior_média = média
print('¨' * 35)
print(f'{"DESEMPENHO DE NOTAS":^35}')
print('¨' * 35)
print(f'Média mais alta: {melhor_média:.1f}')
print(f'Melhor aluno(a): {melhor_aluno}')
print(f'Média mais baixa: {pior_média:.1f}')
print('¨' * 35)
print('FIM')
print('¨' * 35)
