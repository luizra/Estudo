#gerador de cpf
''''''
#gerando 9 numeros aleiatorios
listacpf = []
for x in range (9):
    cpf = rd.randint(0,9)
    listacpf.append(cpf)

#fazendo um contador
contador = len(listacpf)
NumeroMultiplicador = 11
ListaResult = []
zera = 0

#"for" contador para multipicar somar e encontrar o resultado do numero validador
for caractere in range(19):
    NumeroMultiplicador -= 1
    resultado = NumeroMultiplicador * listacpf[zera]
    ListaResult.append(resultado)
    zera += 1
    if NumeroMultiplicador == 2:
        NumeroMultiplicador = 12
        zera = 0

#"if" para encontrar o primeiro numero validador. Usando o comando SUM para somar todos os caraccteres da lista.
        if len(listacpf) == 9:
            soma = sum(ListaResult)
            validador1 = 11 - (soma%11)
            if validador1 > 9:
                validador1 = 0
            ListaResult = []
            listacpf.append(validador1)

#"elif" para encontrar o segundo numero validador. Usando o comando SUM para somar todos os caraccteres da lista.
        elif len(listacpf) == 10:
            soma1 = sum(ListaResult)
            validador2 = 11 - (soma1 % 11)
            if validador2 > 9:
                validador2 = 0
            listacpf.append(validador2)
#Convertendo o "listacpf" para "stringer" e adicionando "." e "-"
CPFValidado = ''
for x in range(len(listacpf)):
    if x == 3 or x == 6:
        CPFValidado += '.'
    if x == 9:
        CPFValidado += '-'
    CPFValidado += str(listacpf[x])

print(CPFValidado)
