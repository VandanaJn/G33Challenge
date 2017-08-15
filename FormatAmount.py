import math
"""FormatAmount module has functions to format amounts"""
def format_ai(val):
    """format_ai returns truncated to three decimal places, and rounded to two decimal places"""
    return g33_round(trunc_decimals(val, 3), 2)

def format_dp(val):
    """format_dp returns truncated to three decimal places"""
    return trunc_decimals(val, 3)

def format_yld(val):
    """format_yld returns truncated to four decimal places, and rounded to three decimal places"""
    return g33_round(trunc_decimals(val, 4), 3)

def trunc_decimals(val, no_of_digits):
    """trunc_decimals returns trucates val to no_of_digits after decimal"""
    trunc_plus_1 = "{0:.{1}f}".format(val, no_of_digits+1)
    return float(trunc_plus_1[:-1])

def g33_round(number , no_of_digits):
    """g33_round returns rounded no to no_of_digits decimal places, g33_round(4.65 , 1) returns 4.7 and g33_round(4.55 , 1) returns 4.6 unlike built-in round which returns banking round"""
    if("{0:.{1}f}".format(number, no_of_digits+1)).endswith('5'):
        return math.ceil(number * 10 ** no_of_digits) / (10 ** no_of_digits)
    return round(number, no_of_digits)

    
