def f(n):
    return 7**(n + 2) + 8**(2 * n + 1)


m = 57
bad = [n for n in range(1, 101) if f(n) % m != 0]
print("Контрприкладів не знайдено" if not bad else bad)
