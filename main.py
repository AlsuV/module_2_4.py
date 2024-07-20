numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = list[numbers]   # простые числа ...Primes: [2, 3, 5, 7, 11, 13]
not_primes = list[numbers]  # не простые числа ...Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
i = 0
n = 0

for i in range(len(numbers)):
    for n in numbers:
        if n < 2:
            is_prime = True
            print('primes: ', list[numbers])
            continue
        else:
            print(not_primes)
        break