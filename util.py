async def is_armstrong(number):
  if number < 0:
    return False

  total = 0
  index = len(str(number))
  digits = [int(digit) for digit in str(number)]
  for digit in digits:
    # get the cube of the digit
    total += (digit ** index)
  return True if total == number else False

async def digit_sum(number):
  if number < 0:
    number = -number

  total = 0
  digits = [int(digit) for digit in str(number)]
  for digit in digits:
    # get the total of the digit
    total += digit
  return total

async def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

async def is_perfect(number):
  if number < 1:
    return False
  total = 0
  for i in range(1, number):
    if number % i == 0:
      total += i
  if total == number:
    return True
  return False

async def get_num_prop(number):
  num_prop = []
  if number % 2 == 0:
    num_prop.append('even')
  else:
    num_prop.append('odd')

  if is_armstrong(number):
    num_prop.insert(0, 'armstrong')

  return num_prop
