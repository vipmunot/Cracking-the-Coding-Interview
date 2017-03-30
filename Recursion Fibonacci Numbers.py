memory = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in memory.keys():
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]
n = int(input())
print(fibonacci(n))
