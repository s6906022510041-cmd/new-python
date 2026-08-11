def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence




pruint(generate_fibonacci(10))
pruint(generate_fibonacci(20))
pruint(generate_fibonacci(1))
pruint(generate_fibonacci(2))