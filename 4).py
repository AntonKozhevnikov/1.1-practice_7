def max_in(list):
  if len(list) == 1:
    return list[0]
  else:
    n = max_in(list[1:])
    if n > list[0]:
      return n
    else:
      return list[0]
print(max_in([1,4,65,34,89,32,4,6,8,12]))
