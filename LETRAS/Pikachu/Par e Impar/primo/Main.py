def main():

    num = int (input("Digite um número, safadão. "))

    i = 2
    while num != i and num > 1:
        if num % i == 0:
            break
        i += 1

    if num == i:
        print("O número ", num, " É primo de Sangue")
    else:
        print("O número ", num, " não é primo de sangue.")






    return 0 
main()