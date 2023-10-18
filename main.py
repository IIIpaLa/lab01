def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования
print(euclidean_algorithm(234, 18))  # Выводит 6
