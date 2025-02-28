def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b    

def multiplicacao(a, b):            
    return a * b

def divisao(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    return a ** 0.5

def media(a, b):
    return (a + b) / 2

def media_3(a, b, c):
    return (a + b + c) / 3

def media_4(a, b, c, d):
    return (a + b + c + d) / 4

def media_5(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def media_6(a, b, c, d, e, f):
    return (a + b + c + d + e + f) / 6

print("Selecione o número da operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz Quadrada")
print("7 - Média de 2 números")
print("8 - Média de 3 números")
print("9 - Média de 4 números")
print("10 - Média de 5 números")
print("11 - Média de 6 números")

escolha = input("Digite sua opção (1/2/3/4/5/6/7/8/9/10/11): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(num1, "+", num2, "=", soma(num1, num2))
elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
elif escolha == '5':
    print(num1, "elevado a", num2, "=", potencia(num1, num2))
elif escolha == '6':
    print("A raiz quadrada de", num1, "=", raiz(num1))
elif escolha == '7':
    print("A média de", num1, "e", num2, "=", media(num1, num2))
elif escolha == '8':
    num3 = float(input("Digite o terceiro número: "))
    print("A média de", num1, ",", num2, "e", num3, "=", media_3(num1, num2, num3))
elif escolha == '9':
    num3 = float(input("Digite o terceiro número: "))   
    num4 = float(input("Digite o quarto número: "))
    print("A média de", num1, ",", num2, ",", num3, "e", num4, "=", media_4(num1, num2, num3, num4))
elif escolha == '10':
    num3 = float(input("Digite o terceiro número: "))   
    num4 = float(input("Digite o quarto número: "))
    num5 = float(input("Digite o quinto número: "))
    print("A média de", num1, ",", num2, ",", num3, ",", num4, "e", num5, "=", media_5(num1, num2, num3, num4, num5))
elif escolha == '11':
    num3 = float(input("Digite o terceiro número: "))   
    num4 = float(input("Digite o quarto número: "))
    num5 = float(input("Digite o quinto número: "))
    num6 = float(input("Digite o sexto número: "))
    print("A média de", num1, ",", num2, ",", num3, ",", num4, ",", num5, "e", num6, "=", media_6(num1, num2, num3, num4, num5, num6))
else:  
    print("Opção inválida")