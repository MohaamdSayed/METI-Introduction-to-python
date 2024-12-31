def fact(num: int) -> int:
  if (num == 0 or num == 1):
    return 1
  else:
    return num * fact(num - 1)

print(fact(5))