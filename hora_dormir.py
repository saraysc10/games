def mediaDeHoras(prompt):
    while True:
        entrada=input(prompt)
        if ',' in entrada:
            print("Digite um valor válido (use ponto, por exemplo 8.2).")
            continue
        try:
            return float(entrada)
        except ValueError:
            print("Digite um valor válido (use ponto, por exemplo 8.2).")


mediaDiaria = mediaDeHoras("Digite quantas horas dorme durante a semana:")

mediaFinalDeSemana=mediaDeHoras("Digite quantas horas dorme no final de semana: ")

mediaTotal= ((mediaDiaria*5)+(mediaFinalDeSemana*2))/7
print(f"A média total é: {mediaTotal:.2f}")

mediaSono=""

if mediaTotal<6:
    mediaSono="Seu sono esta abaixo do ideal."
    print(mediaSono)
elif mediaTotal >= 6 and mediaTotal <= 8:
    mediaSono="Voce tem um sono adequado"
    print(mediaSono)
else:
    mediaSono="Voce dorme bastante! "
    print(mediaSono)

acorda=int(input("Digite quantas vezes o usuario acorda durante a noite: "))

sonoInterrompido=""
if acorda>=0 and acorda<=1:
    sonoInterrompido="Seu sono tende a ser pouco interrompido."
    print(sonoInterrompido)
else:
    sonoInterrompido="Seu sono está sendo muito interrompido."
    print(sonoInterrompido)

print(f"Você dorme, em média, {mediaDiaria} horas por dia na semana e {mediaFinalDeSemana} horas por dia no final de semana."
      f" Sua média de sono semanal é de {mediaTotal:.2f} horas."
      f" Classificação: {mediaSono}. Você acorda {acorda} vezes por noite, portanto {sonoInterrompido}")
