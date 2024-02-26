import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='Add2Numbers')

# Add an argument
parser.add_argument('number1', type=int, help='First number to add')
parser.add_argument('number2', type=int, help='Second number to add')
parser.add_argument('--scale', type=int, default=1)

args = parser.parse_args()

result = (args.number1 + args.number2) * args.scale

print(f"The result is: {result}")


