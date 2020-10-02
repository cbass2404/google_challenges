"""
random ids
prime numbers in single string
number picked is starting index + 5 digits
starting index n of lambda string of primes
value of n is between 0 and 10000
"""


def solution(n):
    hat = []

    def prime_numbers():
        for num in range(2, 20500):
            if all(num % i != 0 for i in range(2, num)):
                hat.append(num)

    prime_numbers()
    hat = ''.join(map(str, hat))

    while n <= 10000:
        return hat[n: n+5]
    n += 1


print(solution(0))
print(solution(3))
