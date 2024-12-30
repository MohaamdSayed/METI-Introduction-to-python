range_end = int(input("enter the range end: "))

numbers = [True] * range_end
numbers[0] = False
numbers[1] = False

for i in range(2, range_end):
  if (numbers[i]):
    print(i)
    for j in range(2, range_end):
      num = j * i
      if (num >= range_end):
        break
      else:
        numbers[num] = False
