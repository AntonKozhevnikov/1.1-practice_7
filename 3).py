a = int(input("Введите число: "))
n = int(input("Введите степень: "))
def power(a, n):
  if n == 0:
    return 1
  if n % 2 == 0:
    return power(a, n/2)*power(a,n/2)
  else:
    return power(a, n-1)*a
print("Результат: ", power(a, n))
