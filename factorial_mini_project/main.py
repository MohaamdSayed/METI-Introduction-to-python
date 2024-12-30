num = int(input("Enter the number you want to find the factorial of: "))
if(num == 0 ):
  print(1)
  exit()
for i in range(1, num):
  num *= i

print(num)