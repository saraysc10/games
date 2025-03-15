
print('Hello World')
"""num1=int(input("Digite o primeiro numero:"))
num2=int(input("Digite o segundo numero: "))
num3=int(input("Digite o terceiro numero:"))
divisao=(num1+num2)/num3
print("A divisao eh", divisao)"""

"""num4=int(input("Digite um numero:"))
if num4%2==0:print("O numero eh par")
else: print("O numero eh impar")"""

"""nota1=float(input("Digite a primeira nota:"))
nota2=float(input("Digite a segunda nota:"))
nota3=float(input("Digite a terceira nota:"))

media=(nota1+nota2+nota3)/3
print(f"A media eh:", f"{media:.2f}")"""

"""idade=19
print("Minha idade eh ", idade)

if idade<18:
    print("Menor")
else:
    print("Maior")"""

"""nota =6
if(nota>=7):
    print("Aprovado")
elif(nota<7 and nota>5):
    print("Recuperacao")
else:
    print("Reprovado")

    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

        if nota >= 7 and nota <= 10:
            print("Aprovado")
        elif nota >= 5 and nota < 7:
            print("Recuperação")
        elif nota >= 0 and nota < 5:
            print("Reprovado")
        else:
            print("Nota inválida")"""

"""num1=30
num2=5
print(max(num1,num2))"""

# nome="Maria"
# print("Ola, ", nome)
#
# if nome=="Maria":
#     print("Ola, ",nome,"! Bem vinda novamente!")

# numero=int(input("Digite um numero"))
#
# if numero>0:
#     print("Numero positivo")
# else:
#     print("Numero negativo")
#
# cor="laranja"
# if cor=="vermelho":
#     print("Pare")
# elif cor=='laranja':
#     print('Atencao')
# else:
#     print("Siga")

# temp=28
# if temp>30:
#     print("Muito quente!")
# else:
#     print("Temperatura agradavel")

# fruta='banana'
# if fruta=='maca':
#     print("Voce escolheu maca")
# else:
#     print("Voce escolheu outra fruta")

# num=int(input("Escolha um numero: "))
# if num%2==1:
#     print("Numero impar")
# else:
#     print("Numero par")

"""8"""
# senha="123456"
# if input("Digite uma senha:")==senha and senha.isdigit() and len(senha)==6:
#     print('Senha Correta')
# else:
#     print('Senha incorreta. A senha deve conter seis digitos numericos.Tente novamente')

"""8b"""
# temp=22
# if temp<15:
#     print("Frio")
# else:
#     print("Clima bom")

"""10b"""
# a=5
# b=10
# if a==b:
#     print("Iguais")
# elif a>b:
#     print("a eh maior que b")
# elif b>a:
#     print("b eh maior que a")
# else:
#     print("Condicao inesperada")

# valor1=input("Digite um valor: ")
# valor2=input("Digite um valor: ")
# if valor1.isdigit() and valor2.isdigit():
#     if(valor1==valor2):
#         print("Iguais")
#     elif(valor1>valor2):
#         print("a eh maior que b")
#     else:
#         print("a eh menor que b")
# else:
#     print("Valores invalidos")

"""11"""
# usuario=input("Digite o usuario: ")
# if usuario=='admin':
#     print("Acesso autorizado")
# else:
#     print("Acesso negado")

"""11b"""
# num=8
# if num%2==0:
#     print("Numero par")
# else:
#     print("Numero impar")

"""12"""
# altura=1.75
# idade=20
# if altura>1.80 and idade<25:
#     print("Pessoa alta e jovem")
# elif altura>1.80 or idade<25:
#     print("Pessoa alta ou jovem")
# else:
#     print("Pessoa com altura media ou baixa e com 25 anos ou mais")

"""13"""
# cidade="Sao Paulo"
# estado="SP"
# if cidade.lower()=="rio" or cidade.lower()=="rio de janeiro":
#     print("Voce mora no Rio")
# elif cidade.lower()=='sao paulo' and estado.upper()=="SP":
#     print("Voce mora em Sao Paulo")
# else:
#     print("Voce mora em outra cidade ou Estado")

"""13"""
# dia = "Segunda"
# if dia.lower()=="sabado" or dia.lower()=="domingo":
#     print("Fim de semana!")
# else:
#     print("Dia de semana")

"""14"""
# x=3
# y="3"
# if type(x)==type(y):
#     print("Mesmos valores e tipos!")
# else:
#     print("Valores ou tipos diferentes")

"""15"""
# saldo=950
# if saldo>1000:
#     print('Saldo alto')
# elif saldo>500 and saldo<1000:
#     print("Saldo medio")
# else:
#     print("Saldo baixo")

"""16"""
# linguagem=" Python "
# if linguagem.strip()=="Python":
#     print("Linguagem correta!")
# else:
#     print("Tente novamente")

"""17"""
# hora="21"
# if int(hora)>=18:
#     print("Boa noite")
# else:
#     print("Bom dia")

"""18"""
# cor=" Azul "
# if cor.strip().lower()=='azul':
#     print("Cor correta")
# else:
#     print("Cor incorreta")

"""19"""
# idade=input('Insira sua idade: ')
# if idade.isdigit() and int(idade)>60:
#     print("Terceira idade")
# else:
#     print("Adulta ou jovem")

"""20"""
# nome=" Ana "
# if nome.strip()=='Ana':
#     print("Oi,", nome.strip(),"!")
# else:
#     print("Nome diferente de Ana")

"""21"""
# def verifica_numero():
#     numero=input("Digite um numero valido: ")
#     if numero.replace("-","").isdigit():
#         if int(numero)>0:
#             return print("positivo")
#         elif int(numero)<0:
#             return print("negativo")
#         else:
#             return print("zero")
#     else:
#         return print("invalido")
#
# verifica_numero()

"""22"""
# def soma_numeros():
#     num1=input("Digite um numero: ")
#     num2=input("Digite um numero: ")
#     if num1.isdigit() and num2.isdigit():
#         return print(int(num1)+int(num2))
#     else:
#         return print("valor invalido")
#
# soma_numeros()

# def soma_numeros2():
#     num1=float(input("Digite um numero: "))
#     num2=float(input("Digite um numero: "))
#     num1_round=round(num1,1)
#     num2_round=round(num2,1)
#
#     return print(num1_round+num2_round)
#
# soma_numeros2()
# **************
# def soma_numeros2():
#     num1 = float(input("Digite um número: "))
#     num2 = float(input("Digite um número: "))
#
#     num1_round = round(num1, 1)
#     num2_round = round(num2, 1)
#
#     print("Resultado:{:.1f}".format(num1_round + num2_round))

# soma_numeros2()

"""23"""
# def cumprimentar():
#     nome=input("Digite seu nome: ")
#     return print("Ola,", nome.strip().capitalize())
#
# cumprimentar()

"""24"""
# def verifica_paridade():
#     valor=input("Insira um valor: ")
#     if valor.isdigit():
#         if int(valor)%2==0:
#             return print("Par")
#         else:
#             return print("Impar")
#     else:
#         return print("Invalido")

# verifica_paridade()

"""25"""
# def area_retangulo():
#     largura=input("Insira largura: ")
#     altura=input("Insira altura: ")
#     if largura.isdigit() and altura.isdigit():
#         return print(int(largura) * int(altura))
#     else:
#         return print("dimensoes invalidas")
#
# area_retangulo()

"""Dicas para solução e comandos mais importantes"""
# list=[1,2,3]
# list.append(4)
# print(list)

"""2"""
# list=[1,2,3]
# print(sum(list))

"""3"""
# list=[1,2,3]
# print(max(list))

"""4*******"""
# list=[-1,1,2,3]
# print(sum(1 for x in list if x < 0))

"""5"""
a=[1,2,3,4,5]
if 2 in a:
    print("This value is in the list")
else:
    print("No value in the list")

for val in a:
    if val==2:
        flag=True
        break
if flag:
    print("This value exists in the list")
else:
    print("No value in this list")