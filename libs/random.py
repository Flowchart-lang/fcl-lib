# libs/random.py

import sys
import random

def random_command(interpreter, args):
    """
    Implements the RANDOM command.
    Example usage: RANDOM result_var = min_value, max_value
    """
    try:
        # Split the arguments into the destination variable and the range
        dest_var, expr = args.split("=", 1)
        dest_var = dest_var.strip()
        expr = expr.strip()
        
        # Split the expression into min and max values
        min_str, max_str = expr.split(",", 1)
        min_val = interpreter._get_value(min_str.strip())
        max_val = interpreter._get_value(max_str.strip())
        
        # Check if the values are integers
        if isinstance(min_val, int) and isinstance(max_val, int):
            # Generate a random integer and store it in the destination variable
            interpreter.variables[dest_var] = random.randint(min_val, max_val)
        else:
            print(f"Error: RANDOM command requires two numbers for the range. Received: {min_val} and {max_val}.")
            sys.exit(1)
            
    except ValueError:
        print(f"Error: Invalid RANDOM statement: '{args}'. Expected 'VAR = MIN, MAX'.")
        sys.exit(1)

# Dictionary that maps FCL command names to Python functions.
# The interpreter will find and use this dictionary to extend its command set.
commands = {
    "RANDOM": random_command,
}
