def is_even(n : int) -> bool:
    # if n & 1 == 0:
    if n % 2 == 0:
        return True
    else:
        return False
        
print(is_even(int(input())))