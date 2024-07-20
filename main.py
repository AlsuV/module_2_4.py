numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i = 0
# primes = numbers[i]   # простые числа ...Primes: [2, 3, 5, 7, 11, 13]
# not_primes = numbers[i]  # не простые числа ...Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
n = 0
for i in range(1, len(numbers)):
    for n in numbers:
        if n < 2:
            is_prime = True
            primes = numbers[i]
        else:
            not_primes = numbers[i]
            break
        continue
print('primes: ', primes)
print('not_primes: ', not_primes)