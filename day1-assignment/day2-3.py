# the sum of n numbers by using the while loop
num = 16

if num < 0:
   print("Enter a number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
