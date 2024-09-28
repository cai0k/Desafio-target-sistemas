def fibonacci(n):
    x = [0, 1]
    while True:
        next_number = x[-1] + x[-2]
        if next_number > n:
            break
        x.append(next_number)
    return x

n = int(input("Digite um numero: "))
result = fibonacci(n)
if n in result:
    print(f"O numero {n} pertence a sequencia de Fibonacci")
else:
    print(f"O numero {n} nao pertence a sequencia de Fibonacci")
print(result)