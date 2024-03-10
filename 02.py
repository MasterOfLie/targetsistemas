#  2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 
# IMPORTANTE:  
# 	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 

def sequencia_fibonacci(n):
    fibonnacci = [0, 1]
    while fibonnacci[-1] < n:
        fibonnacci.append(fibonnacci[-1] + fibonnacci[-2])
    return fibonnacci

def verificar_fibonnacci(n):
    fibonnacci = sequencia_fibonacci(n)
    if n in fibonnacci:
        return True
    else:
        return False

numero = int(input("Digite um número: "))

if verificar_fibonnacci(numero):
    print(f"O número {numero} esta na sequência de Fibonacci.")
else:
    print(f"O número {numero} não esta na sequência de Fibonacci.")