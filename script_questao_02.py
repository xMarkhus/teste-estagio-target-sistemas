# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def sequencia_fibonacci(numero):
    if numero <= 0:
        return []
    
    sequencia = []
    a, b = 0, 1
    while len(sequencia) < numero:
        sequencia.append(a)
        a, b = b, a + b
    
    return sequencia


def pertence_a_sequencia_fibonacci(numero):
    if numero < 0:
        return False
    
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b

    return a == numero


def main():
    while True:
        entrada = input('Digite um número inteiro positivo ou "S" para sair: ').strip()
        
        if entrada.lower() == 's':
            print('Saindo do programa.')
            break
        
        try:
            numero = int(entrada)
            
            if numero <= 0:
                print('Por favor, digite um número inteiro positivo.')
            else:
                print(f'Sequência de Fibonacci com {numero} termos: {sequencia_fibonacci(numero)}')

                if pertence_a_sequencia_fibonacci(numero):
                    print(f'O número {numero} pertence à sequência de Fibonacci.')
                else:
                    print(f'O número {numero} não pertence à sequência de Fibonacci.')
        
        except ValueError:
            print('Digite um número inteiro válido.')

if __name__ == '__main__':
    main()
