import random

def main():
    notas =[0] * 4
    i = 0
    while i < 4:
        notas[i] = random.uniform(0,10)
        i += 1
    média = sum(notas) / len(notas)
    print("Média", notas)
    print("Média", média)
    if média >= 6:
        print("passou de Ano! Miseravel.")
    else:
        print("BURRO MISERÁVEL!!!")
        return 0
main()