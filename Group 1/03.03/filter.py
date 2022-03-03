
my_list = [2, 5, 7, 134532, 12, 43, 22, 29, 31]

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(*filter(is_prime, my_list))
print(*filter(lambda x: x >= 10, my_list))
# print(f'hafdhl {name} asdjklf')