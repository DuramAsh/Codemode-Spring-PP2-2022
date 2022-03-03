# all() / any()

my_list = [2, 5, 7, 134532, 12, 43, 22, 29, 31]

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# for i in my_list:
#     if is_prime(i):
#         print(i)

if any([is_prime(i) for i in my_list]):
    print('All numbers are prime')
else:
    print('Some numbers aren\'t prime')