def fibonacci(n):
    sequence=[0,1]
    if n<=5:
        return n
    for _ in range(2, n+1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[n]

print(fibonacci(10))