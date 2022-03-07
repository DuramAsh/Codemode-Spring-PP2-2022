def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

my_list = [5,4,6,7,8,1,22,42,43,97]
primes = filter(isPrime, my_list)
print(*primes)