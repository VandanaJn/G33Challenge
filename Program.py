"""Entry program for G33 Challenge"""
from FormatAmount import format_ai, format_dp, format_yld
PROMPT_1 = "ENTER TYPE OF NUMBER AS SINGLE CHAR 'A' | 'D' | 'Y' | ANY OTHER CHAR TO QUIT: "

def format_amt(n_type, val):
    """format_amt formats val per their n_type"""
    if n_type == 'A':
        return "ACCRUED INTEREST: {0}".format(format_ai(val))
    if n_type == 'D':
        return "DOLLAR PRICE: {0}".format(format_dp(val))
    if n_type == 'Y':
        return "YIELD: {0}".format(format_yld(val))
    return val

def amt_prompt(n_type):
    """amt_prompt returns prompt 'for' 'type' of amount"""
    if n_type == 'A':
        return "ENTER ACCRUED INTEREST: "
    if n_type == 'D':
        return "ENTER DOLLAR PRICE: "
    if n_type == 'Y':
        return "ENTER YIELD: "
    return "ENTER NUMBER: "

def run_program():
    """run_program is an entry point for the Program"""
    types = ['A', 'D', 'Y']
    while True:
        num_type = input(PROMPT_1)
        if num_type not in types:
            break
        val = float(input(amt_prompt(num_type)))
        print(format_amt(num_type, val))

if __name__ == '__main__':
    run_program()
