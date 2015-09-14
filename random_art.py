import random
from math import *

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr1 = lambda x, y: (x * x * y * y)/10
    # expr2 = lambda x, y: (x - y)**2
    # expr3 = lambda x, y: (x * y)**9
    # expr4 = lambda x, y: (x * y)**random.random
    # expr5 = lambda x, y: (x * y)**(x * y)
    # expr6 = lambda x, y: (x**y)
    # return random.choice([expr1, expr2, expr3, expr4, expr5, expr6])


    expr1 = lambda x, y: (cos(x) - sin(y)) * random.random()
    expr2 = lambda x, y: (sin(x) - sin(y)) * random.random()
    expr3 = lambda x, y: (cos(x) - cos(y)) * random.random()
    expr4 = lambda x, y: (sin(x) + cos(y)) * random.random()
    expr5 = lambda x, y: sin(pi * (sin(x*y))) * random.random
    expr6 = lambda x, y: tan(x*y) - sin(y) * random.random()
    expr7 = lambda x, y: (x * y) * random.random()
    expr8 = lambda x, y: sin(pi * (sin(x*y)))
    expr9 = lambda x, y: tan(pi)+sin(x)+tan(y)*tan(x*y) * random.random()
    return random.choice([expr1, expr2, expr3, expr4, expr5, expr6, expr7, expr8, expr9])






def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
