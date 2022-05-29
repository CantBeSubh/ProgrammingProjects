import math
def is_square(n):
    d,f=divmod(n**0.5,1)
    return True if f==0 else False    

print(is_square(23))

print(divmod(23.5,1))