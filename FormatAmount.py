"""FormatAmount module has functions to format amounts"""
def format_ai(val):
    """format_ai returns truncated to three decimal places, and rounded to two decimal places"""
    return "{0:.2f}".format(trunc_decimals(val, 3))

def format_dp(val):
    """format_dp returns truncated to three decimal places"""
    return "{0:.3f}".format(trunc_decimals(val, 3))

def format_yld(val):
    """format_yld returns truncated to four decimal places, and rounded to three decimal places"""
    temp = trunc_decimals(val, 4)
    return round(temp, 3)

def trunc_decimals(val, no_of_digits):
    """trunc_decimals trucates val to no_of_digits after decimal and returns it"""
    trunc_plus_1 = "{0:.{1}f}".format(val, no_of_digits+1)
    return float(trunc_plus_1[:-1])
