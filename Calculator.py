
from logo_Calculator import logo

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  if b != 0:
    return a / b
  else:
    return "You can't divide with 0"

choice_op = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div 
}

def calculator():
  print(logo)
  
  first_numbers = float(input("What's the first number? : "))
  for symbol in choice_op:
    print(symbol)
    should_continue = True

    while should_continue:
      symbol_op = input("Pick an operation from the line above: ")
      second_number = float(input("What's the next number? : "))
      calculation_f = choice_op[symbol_op]
      answer = calculation_f(first_numbers, second_number)
      print(f"{first_numbers} {symbol_op} {second_number} = {answer}")

      if input(f"Type 'y' to continue calculating with {answer}, or type 'n to start a new calculation: ") == 'y':
        first_numbers = answer
      else:
        should_continue = False
        clear()
        calculator()

calculator()