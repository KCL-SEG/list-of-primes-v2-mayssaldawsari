"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    prime = True
    
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

    return prime

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("must be 1 or more")

    else:
        num = 1
        while len(list) < number_of_primes:
            if isPrime(num):
                list.append(num)
            num +=1

    return list
