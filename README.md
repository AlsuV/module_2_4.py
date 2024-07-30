numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []   # простые числа ...Primes: [2, 3, 5, 7, 11, 13]
not_primes = []  # не простые числа ...Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for divisor in range(2, i):
        if i % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not_primes: ', not_primes)
