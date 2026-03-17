def fibonacci(n):
    if n <= 1:
        return n
    sequence = [0, 1]
    for _ in range(2, n+1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[n]

print(fibonacci(2))