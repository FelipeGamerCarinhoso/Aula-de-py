def main():
    altura = float ( input("Digite a sua altura: "))
    idade = int ( input("Digite a sua idade aqui: "))
    isCasado =  input("Eae Bonitão: ")
    sexo = input("Digite seu sexo: ")
    nome = input("Digite seu nome: ")
    peso = float( input ("Digite seu peso: "))
    cpf = input("Seu cpf: ")

    print("O ", nome ,"mede ", altura, "m de altura, tem ", idade, "anos de idade" )
    print("É do sexo", sexo,"pesa,", peso, "e seu cpf", cpf)

    if isCasado == "S" or isCasado == "s":
        print("O ", nome, "É casado")
    elif isCasado == "sou" or isCasado =="sou":
        print("Ele é casado")
    else:
        print("O ", nome, "não é casado :")
    return 0
main()

