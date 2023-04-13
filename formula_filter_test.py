import re

"""
it has been made for parsing tasks of the specifaid site only:
https://www.math10.com/problems/addition-and-subtraction-problems-up-to-100/normal/
"""


def formula_filter(formula: str) -> str:
    try:
        # it may start with ( and digits or with digits only
        # it may consist any character
        # and it has to end with =
        regex = re.compile(r'(\(|\d).+(=)$')
        # decline =
        formula = re.search(r'.+[^=]', regex.search(formula).group()).group().strip()
        return formula

    except AttributeError as e:
        print(formula, "raises", type(e))
        return ''


if __name__ == '__main__':
    """
    need to test:
    (a) 1|2|3-digit numbers in different scenarios of
    (b) addition|subtractin|multiplication|division
    (c) inside of () [or without them]
    (d) in more complex scenarios when consists more than 1 simple case
    (e) with incoming description [or without]
    (f) wrong incoming case
    """
    TEST_CASES = [
        'Add: 1 + 7 =',         # case: e_a(1)b(+)a(1)
        'Add: 1 + 17 =',        # case: e_a(1)b(+)a(2)
        'Add: 10 + 7 =',        # case: e_a(2)b(+)a(1)
        'Add: 10 + 17 =',       # case: e_a(2)b(+)a(2)
        'Add: (1 + 7) =',       # case: e_c_a(1)b(+)a(1)
        'Add: (1 + 17) =',      # case: e_c_a(1)b(+)a(2)
        'Add: (10 + 7) =',      # case: e_c_a(2)b(+)a(1)
        'Add: (10 + 17) =',     # case: e_c_a(2)b(+)a(2)
        '1 * 7 =',              # case: a(1)b(*)a(1)
        '1 - 17 =',             # case: a(1)b(-)a(2)
        '10 + 7 =',             # case: a(2)b(+)a(1)
        '10 / 17 =',            # case: a(2)b(/)a(1)
        '(1 * 7) =',            # case: c_a(1)b(*)a(1)
        '(1 - 17) =',           # case: c_a(1)b(-)a(2)
        '(10 + 7) =',           # case: c_a(2)b(+)a(1)
        '(10 / 17) =',          # case: e_a(2)b(/)a(2)
        'Calculate: 99 - 85 =', # case: e_a(2)b(-)a(2)
        'Subtract: 76 - 30 =',  # case: e_a(2)b(-)a(2)
        'Subtract: 85 - 4 =',   # case: e_a(2)b(-)a(1)
        'Subtract: 5 - 40 =',   # case: e_a(1)b(-)a(2)
        '5 - 4 =',              # case  a(1)b(-)a(1)
        '(5 - 4)=',             # case  c_a(1)b(-)a(1)
        '(40 + 51) - (3 - 2)=', # case: d_c_a(2)b(+)a(2)_a(1)b(-)a(1)
        '1000 - 500 =',         # case: a(4)b(-)a(3)
        '100-(24+36)-30=',      # case: d
        '44 - = 25',            # case: f
        'Fill in the box with the correct number: \n44 + - 30 = 44',                          # case: f
        'John had 100 chocolate egg toys. He gave 60 to Sissy. How many toys did John have? ' # case: f
    ]
    for formula in TEST_CASES:
        parse = formula_filter(formula)
        print(formula, "(=)", parse)
