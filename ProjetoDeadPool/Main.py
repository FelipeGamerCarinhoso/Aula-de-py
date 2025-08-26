import random 
def main():
    numAle = random.randint(1 , 75)

    num = 0

    tentativas = 0 
    while num != numAle:
       num = int (input("Digite um número: "))

        if num > numAle:
          print("O numero é menor")