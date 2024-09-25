def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {num} NÃO pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(is_fibonacci(numero))

