a = int(input('Введите число: '))
def print_till_zero(n):
    print (n)
    if n == 2:
        return n-1 
    return(print_till_zero(n - 1))
print(print_till_zero(a))
