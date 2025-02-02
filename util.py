def is_armstrong(number):
  sum = 0
  digits = [int(digit) for digit in str(number)]
  for digit in digits:
    # get the cube of the digit
    sum += (digit ** 3)
  return True if sum == number else False

def digit_sum(number):
  sum = 0
  digits = [int(digit) for digit in str(number)]
  for digit in digits:
    # get the sum of the digit
    sum += digit
  return sum

def is_prime(number):
  if number == 0 or number == 1:
    return False
  elif number > 1:
    for i in range(2, number):
      if number % i == 0:
        return False
    return True

def is_perfect(number):
  sum = 0
  for i in range(1, number):
    if number % i == 0:
      sum += i
  if sum == number:
    return True
  return False
