def add(a, b):
  sum = a + b
  return sum

def subtract(a, b):
  difference = a - b
  return difference

def multiply(a, b):
  product = a * b
  return product

def divide(a, b):
  quotient = a / b
  return quotient

# y/n
programRunning = 'yes'
operation = ''
operandA = 0
operandB = 0

while programRunning != 'no':
  operation = ''
  programRunning = input('Calculate a value?\n')
  
  if programRunning == 'no':
    break
  elif programRunning != 'yes':
    continue

  operation = input("Please select a math operation + - * /")
  print("you selected: " + operation)

  operandA = int(input("Please enter a number for operand A: "))
  operandB = int(input("Please enter a number for operand B: "))

  if operation == '+':
    print(add(operandA, operandB))

  if operation == '-':
    print(subtract(operandA, operandB))
    
  if operation == '*':
    print(multiply(operandA, operandB))

  if operation == '/':
    print(divide(operandA, operandB))