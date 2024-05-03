def repetir():
    calc_repetir = input('''
você deseja fazer outro calculo?
Se sim coloque S para Sim 
Se não deseja coloque N para NÃO
Se desejar ver todos os resultados coloque R
''')
    if calc_repetir.upper() == 'S':
        calculadora()
    elif calc_repetir.upper() == 'N':
        print('Até depois.')
    elif calc_repetir.upper() == 'R':
        abrres()
        repetir()
    else:
        repetir()
def menu1():
    menu = input('''o que voce deseja fazer na calculadora?
    1 calculos simples.
    2 Binario 
    3 octal 
    ''')
    return menu
def invalido ():
    print('comando invalido')
def arqres1(N1,N2,eq,res):
    arquivo = open('rescalculadora.txt','a')
    if eq == int:
        B = ['-','+','*','/','**','M','%','R']
        eq = B[int(eq)-1]
        if eq == '%':
            arquivo.write(f'{N2}% de {N1} = {res}'+'\n')
        elif eq.upper() == 'R':
            arquivo.write(f'raiz de {N1} = {res}'+'\n')
        else:
            arquivo.write(f'{N1} {eq} {N2} = {res}'+'\n')
    else:
        if eq == '%':
            arquivo.write(f'{N2}% de {N1} = {res}'+'\n')
        elif eq.upper() == 'R':
            arquivo.write(f'raiz de {N1} = {res}'+'\n')
        else:
            arquivo.write(f'{N1} {eq} {N2} = {res}'+'\n')
    arquivo.close()
def arqres2(N1,eq,res):
    arquivo = open('rescalculadora.txt', 'a')
    if eq == '1':
        arquivo.write(f'o numero decimal {N1} em binario é = {res}'+'\n')
    elif eq == '2':
        arquivo.write(f'O numero binario {N1} em decimal é = {res}'+"\n")
    arquivo.close()
def arqres3(N1,eq,res):
    arquivo = open('rescalculadora.txt', 'a')
    if eq == '1':
        arquivo.write(f'o numero decimal {N1} em octal é = {res}'+'\n')
    elif eq == '2':
        arquivo.write(f'O numero octal {N1} em decimal é = {res}'+"\n")
    arquivo.close()
def numeros():
    global N1, N2
    try:
        N1 = float(input('coloque o primeiro numero: '))
        N2 = float(input('coloque o sugundo numero: '))
    except ValueError:
        print('coloque apenas numeros.')
        numeros()
    return N1,N2
def numero():
    global N1
    try:
        N1 = int(input('coloque o numero: '))
    except ValueError:
        print('coloque apenas numeros sem pontuação.')
        numero()
    return N1
def abrres():
    arquivo = open('rescalculadora.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()

def soma(N1,N2):
    return N1 + N2
def sub(N1,N2):
    return N1 - N2
def mult(N1,N2):
    return N1 * N2
def div(N1,N2):
    return N1 / N2
def poten(N1,N2):
    return N1**N2
def restdiv(N1,N2):
    return N1 % N2
def porcent(N1,N2):
    return (N1*N2)/100
def raiz (N1):
    return N1**(1/2)
def binario(N1):
    b = ''
    while N1 > 0:
        b += str(int(N1) % 2)
        N1 = N1 // 2
    return b[::-1]
def binariod(N1):
    au1 = len(str(N1))
    res = 0
    while au1 > 0:
        au2 = str(N1)[-au1]
        au1 = au1 - 1
        res = int(au2)* 2 ** au1 + res
    return res

def octal(N1):
    o = ''
    while N1 > 0:
        o += str(int(N1) % 8)
        N1 = N1 // 8
    return o[::-1]
def octald(N1):
    au1 = len(str(N1))
    res = 0
    while au1 > 0:
        au2 = str(N1)[-au1]
        au1 = au1 - 1
        res = int(au2) * 8 ** au1 + res
    return res
def bem_vindo():
    print('*' * 36)
    print('**** Bem vindo a calculadora!!! ****')
    print('*' * 36)
def calculadora():
    menu = menu1()
    if menu == "1":
        eq = input('''Qual operção deseja fazer:
    1 Subitração (-)
    2 Soma (+)
    3 Multplicação (*) 
    4 Divisão (/)
    5 Potencia (**)
    6 Resto de uma divisão ou modulo (M) 
    7 Porcentagem (%)
    8 Raiz (R)
    ''')

        if eq == '1' or eq == "-":
            N1,N2 = numeros()
            res = sub(N1,N2)
            print(f'o resultado é: {N1} - {N2} = {res}')
            arqres1(N1,N2,eq,res)
        elif eq == '2' or eq == "+":
            N1, N2 = numeros()
            res = soma(N1,N2)
            print(f'o resultado é: {N1} + {N2} = {res}')
            arqres1(N1,N2,eq,res)
        elif eq == '3'or eq == "*":
            N1, N2 = numeros()
            res = mult(N1,N2)
            print(f'o resultado é: {N1} * {N2} = {res}')
            arqres1(N1,N2,eq,res)
        elif eq == '4'or eq == "/":
            N1, N2 = numeros()
            if N2 == 0:
                invalido()
            else:
                res = div(N1,N2)
                print(f'o resultado é: {N1} / {N2} = {res}')
                arqres1(N1,N2,eq,res)
        elif eq == '5'or eq == "**":
            N1, N2 = numeros()
            res =poten(N1,N2)
            print(f'o resultado é: {N1} ** {N2} = {res}')
            arqres1(N1,N2,eq,res)
        elif eq.upper() == '6'or eq == "M":
            N1, N2 = numeros()
            res = restdiv(N1,N2)
            print(f'o resultado é: {N1} M {N2} = {res}')
            arqres1(N1,N2,eq,res)
        elif eq == '7'or eq == "%":
            N1, N2 = numeros()
            res = porcent(N1,N2)
            print(f'o resultado é: {N2}% de {N1} = {res}')
            arqres1(N1,N2,eq,res)
        elif eq.upper() == '8'or eq == "R":
            N1 = numero()
            res = raiz(N1)
            print(f'o resultado é:raiz de {N1} = {res}')
            arqres1(N1,'',eq,res)
        elif eq.upper() == '9'or eq == "-":
            N1 = numero()
            if N1 == 0:
                res = 0
            else:
                res = binario(N1)
            print(f'o o numero {N1} em binario é = {res}')
            arqres1(N1, '', eq, res)
        else:
            print('operação invalida tente novamente')
    elif menu == '2':
        eq = input('''Qual operção deseja fazer:
    1 Converção decimal para binario (B)
    2 Converter binario para decimal (D)
    ''')

        if eq == "1" or eq.upper() == "B":
            N1 = numero()
            if N1 == 0:
                res = 0
            else:
                res = binario(N1)
            print(f'O numero decimal {N1} em binario é = {res}')
            arqres2(N1, eq, res)
        if eq == "2" or eq.upper() == "D":
            N1 = numero()
            if N1 == 0:
                res = 0
            else:
                res = binariod(N1)
            print (f'O numero binario {N1} em decimal é = {res}')
            arqres2(N1, eq, res)
    elif menu == '3':
        eq = input('''Qual operção deseja fazer:
    1 Converção decimal para octal
    2 Converter octal para decimal
    ''')

        if eq == '1':
            N1 = numero()
            if N1 == 0:
                res = 0
            else:
                res = octal(N1)
            print(f'O numero decimal {N1} em octal é = {res}')
            arqres3(N1, eq, res)
        elif eq == '2':
            N1 = numero()
            if N1 == 0:
                    res = 0
            else:
                res = octald(N1)
            print(f'O numero octal {N1} em decimal é = {res}')
            arqres3(N1, eq, res)


    repetir()
