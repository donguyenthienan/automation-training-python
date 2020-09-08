'''
In the program below, we've used an if...else statement in combination with a while loop to calculate the sum of natural numbers up to num.
'''

# Sum of natural numbers up to num

num = 16

if num < 0:
  print("Enter a positive number")
else:
  sum = 0
  # use while loop to iterate until zero
  while (num > 0):
    sum += num
    num -= 1
  print("The sum is", sum)
