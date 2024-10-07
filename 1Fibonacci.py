"""1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

Implemente em python utilizando as melhores praticas do mercado e em ingles"""
def sequencia_fibonacci(n):
    """Gera a sequência de Fibonacci até o número n."""
    sequencia = []
    a = 0
    b = 1
    
    while a <= n:
        sequencia.append(a)
        temp = a
        a = b
        b = temp + b
    
    return sequencia

def esta_na_fibonacci(num):
    fib_sequencia = sequencia_fibonacci(num)
    return num in fib_sequencia

def main():
    entrada_usuario = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
    
    if esta_na_fibonacci(entrada_usuario):
        print(f"O número {entrada_usuario} está na sequência de Fibonacci.")
    else:
        print(f"O número {entrada_usuario} NÃO está na sequência de Fibonacci.")

main()


