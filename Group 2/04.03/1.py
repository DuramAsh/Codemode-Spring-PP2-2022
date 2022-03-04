# def is_prime(n):
# 	if n == 0 or n == 1:
# 		return False
# 	for i in range(2, int(n ** 0.5) + 1):
# 		if n % i == 0:
# 			return False
# 	return True

# def okay(n):
#     return n >= 100

# l1 = [2, 4, 67, 512, 29, 31, 55, 123]
# print(all([is_prime(i) for i in l1]))
# print(any([is_prime(i) for i in l1]))

# print(*filter(is_prime, l1))


# import re
# pattern = r'\d{3,5}'
# re.search(pattern, '347289301')
# R1 = re.compile(pattern)
# R1.search('81739240918')

# class Person:
#     name = '123'
#     surname = '256'

# print(dir(Person))

# print(divmod(10, 3))

# for i in range(len(l1))
# for i in l1

# for i in range(len(l1)):
#     print(i, l1[i])

# for ind, el in enumerate(l1):
#     print(ind, el)

# print(eval('(5+67)*2+4/22'))

# with open('script.py', 'r') as f:
#     x = f.read()

# exec(x)

# s = '12345'
# s[0] = '2'

# import s

# def main():
#     print('OK1')

# if __name__ == '__main__':
# 	main()

# def maxx(**kwargs):
#     return 5

# print(maxx({1: 2}, {3: 4}))

# class Person:
#     def __init__(self, age) -> None:
#         self.__age = age

#     def get_age(self):
#         return self.__age


# P1 = Person(25)
# print(P1.get_age())

# l1 = [1, 2, 3, 4, 5]
# l2 = [11, 22, 33, 44, 55, 66, 77]
# z = zip(l1, l2)

# for i in z:
#     print(i)