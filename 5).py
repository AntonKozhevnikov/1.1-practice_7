x = int(input('Выберете номер члена ряда Фибаначчи: '))
def fib(n):
    if n <= 2:
        return 1
    else:
        return (fib(n-2) + fib(n-1))
print('Пожалуйста: ', fib(x))

#не понял как сделать с последовательность нуля 
