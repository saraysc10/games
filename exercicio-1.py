
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
# list=[1,2,3,4,5]
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
# a=[1,2,3,4,5]
# if 2 in a:
#     print("This value is in the list")
# else:
#     print("No value in the list")
#
# for val in a:
#     if val==2:
#         flag=True
#         break
# if flag:
#     print("This value exists in the list")
# else:
#     print("No value in this list")

"""6***"""
# list=[]
# list.append(5)
# list.append(6)
# list.append(7)
#
# list2=[8,9]
# list.extend(list2)
# print(list)
#
"""7****"""
# list.pop(1)
# list.remove(9)
# print(list)

"""8 & 9"""
# class Car:
#     def __init__(self, brand, year,metragem):
#         self.brand=brand
#         self.year=year
#         self.metragem=metragem
#     def model(self):
#         print(f"The {self.brand} is on! Ano {self.year}, Metragem:{self.metragem}")
# car1= Car("Ford", 2000, 80)
# car1.model()

"""10"""
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def introduction(self):
#         print(f"Hello, my name is {self.name}!")
#
# name1=Person("Ana",34)
# name1.introduction()

"""11"""
# class Volley:
#     def __init__(self, points, player1, player2, winner,rules):
#         self.points=points
#         self.player1=player1
#         self.player2=player2
#         self.winner=winner
#         self.rules=rules
#
#     def game(self):
#         print(f"{self.winner} is the winner with a score of {self.points}")
#
# game1= Volley('5-3', "LA", "NY", "NY", "The ball must be returned over the net in 3 hits or less")
# game1.game()

"""12"""
# class maior():
#     def __init__(self, num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def maior_numero(self):
#         if self.num1>self.num2:
#             print(f"{self.num1} eh maior que {self.num2}.")
#         else:
#             print(f"{self.num2} eh maior que {self.num1}.")
#
# num2=maior(5,7)
# num2.maior_numero()

"""13"""
# num=7
# if num%2==0:
#     print("Par")
# else:
#     print("Impar")

"""14"""
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# list2=[]
# for x in list:
#     if x%2!=0:
#         list2.append(x)
#
# print(list2)

"""15"""
# list=[]
# if list:
#     print("A lista contem elementos")
# else:
#     print("A lista esta vazia")

"""16"""
# class Livro():
#     def __init__(self,livro,ano,autor):
#         self.livro=livro
#         self.ano=ano
#         self.autor=autor
#     def definir(self):
#         print(f"O titulo do livro eh {self.livro} e o autor eh {self.autor}")
#
# livro1=Livro("A Substancia", 2024, "Ana Maria")
# livro1.definir()

"""17"""

# list=[1,2,3,4,5,6,7,3,4,2,3]
# print(sum(1 for x in list if x==3))

"""18"""
# a=[1,3,4,5,6]
# result=1
# for x in a:
#     result = result*x
# print(result)

"""19"""
# import statistics
# print(statistics.mean([1,3,4,5,6]))

# Cálculo da média
# valores=[1,2,3,4,5]
# media = sum(valores) / len(valores)
# print(f"A média é: {media}")

"""20"""
# a=3
# b=3
# if a==b:
#     print("Sao iguais")
# else:
#     print("Sao diferentes")

"""cinema"""
# import tkinter.messagebox as msgbox
# import tkinter.simpledialog as simpledialog
#
# def game():
#
#     msgbox.showinfo("Ola","Bem-vindo ao cinema!")
#
#     usuario=simpledialog.askinteger("Usuario","Qual o seu nome?")
#
#     if math.isnan(player):
#         msgbox.showwarning("Error", "Choose a number")
#     elif player>10:
#         msgbox.showwarning("Error", "Choose a number lower than 10!")
#         return
#     robot=random.randint(1,10)
#
#
#     msgbox.showinfo("Robot:", f"You chose: {player}\n Robot chose:{robot}")
#
#
#
#     if (player+robot)%2==0:
#         result="The result is Even!"
#     else:
#         result="The result is Odd!"
#
#     """Final Result"""
#     msgbox.showinfo("Result:", result)
#
#
# if __name__ == "__main__":
#     from tkinter import Tk
#     root = Tk()
#     root.withdraw()
#     game()

"""7.1- Whastapp *****"""
# list=["banana","esmalte", "maca", "carregador","meia","gato","ave","cavalo","bolsa","esmalte"]
# caracteres=0
# total_caracteres=0
# quantidade=0
# palavra_curta=list[0]
# palavra_longa=list[0]
# media=0
# for palavra in list:
#     tamanho=0
#
#
#     for letra in palavra:
#         total_caracteres=total_caracteres+1
#         tamanho +=1
#
#     quantidade=quantidade+1
#
#     comprimento2 = 0
#     for letra in palavra_curta:
#         comprimento2+=1
#
#     if tamanho<comprimento2:
#         palavra_curta=palavra
#
#     comprimento3=0
#     for letra in palavra_longa:
#         comprimento3+=1
#
#     if tamanho>comprimento3:
#         palavra_longa=palavra
#
# print(f"Comprimento de todas as palavras: {total_caracteres}")
# print(f"Comprimento media das palavras: {total_caracteres/quantidade}")
# print(f"Palavra curta: {palavra_curta}")
# print(f"Palavra longa: {palavra_longa}")

"""6***** Whatsapp"""

# list=[]
# length=int(input("Digite quantas cores o usuario deseja introduzir: "))
# print(length)
#
# for i in range(1,length+1):
#     cor=input(f"Introduza a cor {i}: ")
#     list.append(cor)
#
# print("\nCores inseridas:")
# for cor in list:
#     print(f"- {cor}")
#
# # Exibe a quantidade de cores
# print(f"\nQuantidade total de cores: {len(list)}")

"""5 - Whastapp ***"""

# cidades=[]
# for i in range(0,3):
#     cidade=input("Introduza uma cidade: ")
#     if len(cidade)>5 and "e" in cidade:
#         cidades.append(cidade)
#
# print("\n Cidades introduzidas:")
# for cidade in cidades:
#     print(f"\n -{cidade}")

"""2"""
# from datetime import datetime
# from datetime import timedelta
#
# hora_dormir=input("Digite as horas que o usuario vai dormir: ")
# dormir=datetime.strptime(hora_dormir,"%H:%M")
#
# hora_acordar=input("Digite as horas que o usuario vai acordar: ")
# acordar=datetime.strptime(hora_acordar,"%H:%M")
# acordar+=timedelta(days=1)
#
# tempo_sono=(acordar-dormir).total_seconds()/3600
#
# if tempo_sono >6:
#     print("Dormes muito")
# else:
#     print("Dormes pouco")
#
# print(f"Horas dormidas: {tempo_sono}")

"""3 Apostila Python Introducao"""
# A = "Um elefante incomoda muita gente"
# print(A[3:20])
# frase = input("Digite uma frase: ")
# frase_sem_espaços = frase.replace(' ','')
# frase_maiuscula = frase_sem_espaços.upper()
# print(frase_maiuscula)

"""4"""
# x=float(input("Digite o valor de x: "))
# y=float(input("Digite o valor de y: "))
# z = (x**2+y**2)/(x-y)**2
# print("z = ",z)

# salario = float(input("Digite o salário atual: "))
# novo_salario = salario*1.35
# print("Novo salário = R$ %.2f" %novo_salario)


"""5"""
# L = [5, 7, 2, 9, 4, 1, 3]
# print(len(L))
# print(max(L))
# print(min(L))
# print(sum(L))
# L.sort()
# print(L)
# L.reverse()
# print(L)

# L = list(range(3, 50, 3))
# print(L)

"""7"""
# lanchonete={"salgado":4.50,"lanche":6.50,"suco":3,"refrigerante":3.50,"doce":1}
# print(lanchonete)

# classe = {"Ana": 4.5,
#  "Beatriz": 6.5,
#  "Geraldo": 1.0,
#  "José": 10.0,
#  "Maria": 9.5}
#
# notas=classe.values()
#
# media=sum(notas)/len(classe.values())
# print(media)

"""9"""
# nota1 = float(input("Digite a 1ª nota do aluno: "))
# nota2 = float(input("Digite a 2ª nota do aluno: "))
# média = (nota1+nota2)/2
# print("Média = ",média)
# if média >= 6:
#  print ("Aprovado")
# elif média >=4:
#  print ("Exame")
# else:
#  print ("Reprovado")


"""10"""
# soma=0
# for x in range(3,334,3):
#     soma+=x
#
# print(soma)

# S=0
# for contador in range(1,11):
#  nota = float(input("Digite a nota "+str(contador)+": "))
#  S=S+nota
# print("Média = ",S/10)

# numero = int(input("Digite o número para a tabuada: "))
# for sequencia in range(1,11):
#  print("%2d x %2d = %3d" %(sequencia,numero,sequencia*numero))

"""Funcoes"""
# def linha(N):
#     for i in range(N):
#         print(end="_")
#     print(" ")
#
# print(linha(5))

# def imprime_lista(L):
#     contador=0
#     for valor in L:
#         contador=contador+1
#         print(contador,')', valor)
#
# print(imprime_lista([1,2,3,4,5]))

# def media_lista(L):
#     somador=0
#     for valor in L:
#         somador=somador+valor
#     return somador/len(L)
#
# print(media_lista([3,4,5]))

"""1 Whatsapp - ESP"""
# def caracteristicas(cor, esporte, cidade,animal):
#     print(f"Minha cor preferida eh: {cor},"
#           f"\nMeu esporte preferido eh: {esporte}"
#           f"\nEu nasci em {cidade},"
#           f"\nTenho animais de estimacao? {animal}")
#
# caracteristicas("amarelo","volei","SP","Sim")
# minha_cor=input("Escolha uma cor: ")
# meu_esporte=input("Escolha um esporte: ")
# minha_cidade=input("Escolha sua cidade natal: ")
# caracteristicas(minha_cor,meu_esporte,minha_cidade,"sim")

"""4 Whatsapp*****"""
# livros=["Dom Quixote","Hamlet","A Metamorfose"]
# livros.append("1984")
# livros.append("Ulisses")
# print(livros)
# livros.remove("Hamlet")
# print(livros)
# livros.insert(2,'Orgulho e preconceito')
# print(livros)
# anos=[1605,1915,1813,1949,1922]
# resultado=zip(livros,anos)
# print(list(resultado))
# for i in livros:
#     print(f"\n -{i}")
"""8"""
# numeros=[1,2,3,4,5,6,7,8,9,10]
# impar=[]
# par=[]
# for i in numeros:
#     if i%2==0:
#         par.append(i)
#     else:
#         impar.append(i)
#
# print(par)
# print(impar)

"""9 ****"""
# pratos={}
# for i in range(0,5):
#     prato=input("Insira um prato: ")
#     caloria=int(input("Insira as calores do prato acima: "))
#     pratos[prato]=caloria
#
# print(pratos)
#
# for key, value in pratos.items():
#     if value >500:
#         print(key)

"""10****"""
#
# frase= "Em rápido rapto, um rápido rato raptou três ratos sem deixar rastros."
# palavras=frase.split(" ")
# print(palavras)
#
# frequencia_palavras = {}
# for palavra in palavras:
#     if palavra in frequencia_palavras:
#         frequencia_palavras[palavra] += 1
#     else:
#         frequencia_palavras[palavra] = 1
#
# print(frequencia_palavras)

"""Cálculo de Soma e Média de uma Lista de Números
Escreva um programa em Python que solicite 
ao usuário que insira uma série de números. O programa 
deve armazenar esses números em uma lista, 
calcular a soma e a média dos números inseridos e, 
finalmente, exibir esses resultados."""
# list=[]
# for i in range(0,5):
#     num=float(input("Insira um numero: "))
#     list.append(num)
#
# soma=0
# numeros=0
# for x in list:
#     soma+=x
#     numeros+=1
#
# media=soma/numeros
# print(f"Soma: ", soma)
#
# """Como formatar:"""
# print(f"Média: {soma/numeros:.2f}")

"""Exercicio implementacao da classe matriz"""
# class Matriz:
#     def __init__(self, dados):
#         """inicializa a matriz com uma lista de listas
#         ex de datas:
#         [
#             [1,2,3],
#             [4,5,6]
#         ]"""
#
#         self.dados=dados
#         self.linhas=len(dados)
#         """Supondo que todas as linhas têm o mesmo número de colunas:"""
#         self.colunas = len(dados[0]) if self.linhas > 0 else 0
#
#         def imprime(self):
#             """Imprime a matriz de forma organizada."""
#             for linha in self.dados:
#                 print(" ".join(str(valor) for valor in linha))
#
#     def soma(self, outra):
#         """
#                 Soma a matriz com outra matriz 'outra'.
#                 Retorna uma nova instância de Matriz com o resultado.
#                 Levanta ValueError se as dimensões forem incompatíveis.
#                 """
#         if self.linhas != outra.linhas or self.colunas != outra.colunas:
#             raise ValueError ("As matrizes devem ter as mesmas dimensoes para somar.")
#         nova_dados = []
#         for i in range(self.linhas):
#             linha_soma = []
#             for j in range(self.colunas):
#                 linha_soma.append(self.dados[i][j] + outra.dados[i][j])
#                 nova_dados.append(linha_soma)
#                 return Matriz(nova_dados)
#
#     def multiplica_escalar(self,escalar):
#         """
#                 Multiplica cada elemento da matriz por um valor escalar.
#                 Retorna uma nova instância de Matriz com o resultado.
#                 """
#
#         nova_dados=[
#             [valor * escalar for valor in linha] for linha in self.dados
#         ]
#         return Matriz(nova_dados)
#
#     """
#       Multiplica cada elemento da matriz por um valor escalar.
#       Retorna uma nova instância de Matriz com o resultado.
#       """
#     """Conclusão
#     Clareza e Eficiência:
#     O método utiliza list comprehensions aninhadas para processar e
#     transformar cada elemento da matriz de forma concisa e eficiente.
#
#     Imutabilidade:
#     Em vez de modificar a matriz original, ele cria uma nova matriz,
#     o que é uma prática comum para manter a integridade dos dados.
#     Utilidade:
#     Multiplicar uma matriz por um escalar é uma operação fundamental
#     em muitas aplicações matemáticas e de processamento de dados, e esse
#     método implementa essa operação de forma elegante."""
#
#     def multiplica(self,outra):
#         """
#                 Multiplica a matriz pela matriz 'outra' seguindo a regra de multiplicação de matrizes.
#                 Retorna uma nova instância de Matriz com o resultado.
#                 Levanta ValueError se o número de colunas da primeira matriz
#                 for diferente do número de linhas da segunda.
#                 """
#
#         if self.colunas != outra.linhas:
#             raise ValueError ("Número de colunas da primeira matriz "
#                               "deve ser igual ao número de linhas da segunda.")
#
#             """Cria uma matriz de zeros com as dimensões do resultado"""
#             resultado_dados=[
#                 [0 for _ in range(outra.colunas)] for _ in range(self.linhas)
#             ]
#
#             #multiplicacao de matrizes
#             for i in range(self.linhas):
#                 for j in range (outra.colunas):
#                     soma=0
#                     for k in range(self.colunas):
#                         soma+= self.dados[i][k] * outra.dados[k][j]
#                         resultado_dados[i][j] = soma
#
#             return Matriz(resultado_dados)
#             """Resumo
# Validação Inicial: Garante que as matrizes possam ser
# multiplicadas (compatibilidade das dimensões).
#
# Criação da Estrutura do Resultado: Inicializa uma matriz de zeros com as
# dimensões adequadas para armazenar o resultado.
#
# Processo de Multiplicação: Utiliza três laços aninhados para multiplicar o
# s elementos de cada linha da primeira matriz pelas colunas
# correspondentes da segunda, acumulando os produtos.
#
# Retorno do Resultado: Retorna uma nova instância da classe
# Matriz que contém o produto das duas matrizes.
#
# Essa implementação segue o algoritmo clássico de
# multiplicação de matrizes e é uma excelente forma de praticar
# tanto o uso de loops aninhados quanto a manipulação de listas em Python dentro
# do paradigma de programação orientada a objetos."""
#
#             #codigo de exemplo para testar a classe matriz
#             if _name_ == "_main_":
#                 """definindo duas matrizes para a soma e multiplicao por escalar"""
#             dados_a = [
#                 [1,2,3],
#                 [4,5,6]
#             ]
#             dados_b=[
#                 [7,8,9],
#                 [10,11,12]
#             ]
#
#             matriz_a = Matriz(dados_a)
#             matriz_b = Matriz(dados_b)
#
#             print("Matriz A:")
#             matriz_a.imprime()
#             print("\n Matriz B:")
#             matriz_b.imprime()
#
#             #soma_das matrizes a e b
#             try:
#                 soma = matriz_a.soma(matriz_b)
#                 print("\n Soma de A e B")
#                 soma.imprime()
#             except ValueError as e:
#                 print(e)
#             # Multiplicação da matriz A por um escalar (exemplo: 3)
#             multiplicada=matriz_a.multiplica_escalar(3)
#             print("\n Matriz A multiplicada por 3:")
#             multiplicada.imprime()
#
# """if _name_ == "_main_":
#
#
# Conclusão
# Esse exemplo demonstra como:
#
# Criar e instanciar objetos da classe Matriz.
#
# Usar métodos para imprimir a matriz.
#
# Realizar a soma de duas matrizes com validação de dimensões.
#
# Multiplicar uma matriz por um escalar.
#
# O código ilustra de forma prática como combinar a
# programação orientada a objetos com operações matemáticas
# (manipulação de matrizes),
# facilitando a reutilização e a organização do código."""
#
# """# Exemplo de multiplicação de matrizes:
#     # Para multiplicar, as dimensões devem ser compatíveis.
#     # Definindo outra matriz com dimensões compatíveis:"""
#
# dados_c=[
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# matriz_c=Matriz(dados_c)
#
# try:
#      produto = matriz_a.multiplica(matriz_c)
#      print("\nProduto de A x C:")
#      produto.imprime()
# except ValueError as e:
#      print(e)

"""EXERCÍCIO PROPOSTO (1)"""
# nomeCompleto=input("Digite o nome completo: ")
# anoNascimento=int(input("Digite o ano de nascimento: "))
# temAnimaisEstimacao= bool(input("Tem animais de estimacao? Digite algum caractere se sim e nenhum caractere para nao. "))
# cidadeOndeMora=input("Qual a cidade onde mora? ")
# quantidadeIrmaos=int(input("Digite a quantidade de irmaos: "))
#
# idade=2025-anoNascimento
#
# print(f"Meu nome eh {nomeCompleto}. Nasci em {anoNascimento},"
#       f"entao tenho aproximadamente {idade} anos. Moro em "
#       f"{cidadeOndeMora}. Tenho animais de estimacao? {temAnimaisEstimacao}."
#       f"Quantidade de irmaos: {quantidadeIrmaos}.")
#
# if quantidadeIrmaos>2:
#     print("Uau! Voce tem uma familia grande!")
# else:
#     print("Sua familia deve ser bem unida!")
#
# hobbyFavorito=input("Qual o seu hobby favorito? ")
# comidaPreferida=input("Qual a sua comida preferida? ")
#
# informacoesExtras=[hobbyFavorito,comidaPreferida]
#
# print(f"Seus novos dados sao: {informacoesExtras}")

"""EXERCÍCIO PROPOSTO (2)"""
# def mediaDeHoras(prompt):
#     while True:
#         entrada=input(prompt)
#         if ',' in entrada:
#             print("Digite um valor válido (use ponto, por exemplo 8.2).")
#             continue
#         try:
#             return float(entrada)
#         except ValueError:
#             print("Digite um valor válido (use ponto, por exemplo 8.2).")
#
#
# mediaDiaria = mediaDeHoras("Digite quantas horas dorme durante a semana:")
#
# mediaFinalDeSemana=mediaDeHoras("Digite quantas horas dorme no final de semana: ")
#
# mediaTotal= ((mediaDiaria*5)+(mediaFinalDeSemana*2))/7
# print(f"A média total é: {mediaTotal:.2f}")
#
# mediaSono=""
#
# if mediaTotal<6:
#     mediaSono="Seu sono esta abaixo do ideal."
#     print(mediaSono)
# elif mediaTotal >= 6 and mediaTotal <= 8:
#     mediaSono="Voce tem um sono adequado"
#     print(mediaSono)
# else:
#     mediaSono="Voce dorme bastante! "
#     print(mediaSono)
#
# acorda=int(input("Digite quantas vezes o usuario acorda durante a noite: "))
#
# sonoInterrompido=""
# if acorda>=0 and acorda<=1:
#     sonoInterrompido="Seu sono tende a ser pouco interrompido."
#     print(sonoInterrompido)
# else:
#     sonoInterrompido="Seu sono está sendo muito interrompido."
#     print(sonoInterrompido)
#
# print(f"Você dorme, em média, {mediaDiaria} horas por dia na semana e {mediaFinalDeSemana} horas por dia no final de semana."
#       f" Sua média de sono semanal é de {mediaTotal:.2f} horas."
#       f" Classificação: {mediaSono}. Você acorda {acorda} vezes por noite, portanto {sonoInterrompido}")



"""Entre Ritmos e Telas: Explorando Dados de Bandas, Músicas e Filmes"""
# #
# bandas=['The Beatles','Queen','Nirvana']
# bandas.append("Pink Floyd")
# bandas.append("Led Zeppelin")
# print(bandas)
#
# bandas.remove("Nirvana")
# print(bandas)
#
# bandas.insert(2,'Metallica')
# print(bandas)
#
# dicionario={'The Beatles':1960,
#             'Queen':1970,
#             'Pink Floyd':1965,
#             'Led Zeppelin':1968,
#             'Metallica':1981}
#
# print(dicionario['Led Zeppelin'])
#
# dicionario["Kiss"]=1962
# dicionario["Rolling Stones"]=1970
#
# print(dicionario)
#
# # Definindo uma classe chamada 'Pessoa'
# class pessoa():
#     """Método construtor que inicializa os atributos nome e idade"""
#     def __init__(self, nome,idade,profissao,cidade):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao
#         self.cidade=cidade
#
#     # Método para apresentar a pessoa
#     def apresentar(self):
#         return (f"Ola, meu nome eh {self.nome} e tenho {self.idade} anos."
#                 f"Sou {self.profissao} e moro em {self.cidade}.")
#
# # Criando um objeto da classe Pessoa
# pessoa1=pessoa("joao",30,"artesao","Rio de Janeiro")
# # Utilizando o método 'apresentar' do objeto
# print(pessoa1.apresentar())
#
# mensagem=pessoa1.apresentar()
# print("Estou chamando o Joao de novo.",mensagem)