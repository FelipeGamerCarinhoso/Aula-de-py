from Sub import sub
from Mult import mult
from Div import div
def main():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))

    if operacao == '+':
            resultado = somar(numero1, numero2)
    elif operacao == '-':
            resultado = subtrair(numero1, numero2)
    elif operacao == '*':
            resultado = multiplicar(numero1, numero2)
    elif operacao == '/':
            resultado = dividir(numero1, numero2)
    else:
            print("Tente novamente.")
   continue
    
print(" Resultado: {resultado}")

def soma(num1, num2):

    return num1 + num2

main()