import re

"""
it has been made for parsing tasks of the specifaid site only:
https://www.math10.com/problems/addition-and-subtraction-problems-up-to-100/normal/
"""

def formula_filter(formula: str) -> str:
    "return a matched-format formula only"
    try:
        # may start with ( and digits or with digits only
        # have to contain any char in []
        # may end with digits and ) or with digits only
        # may contain any 3 chars after main group
        # can't end with =
        regex = re.compile(r'((?:\(|\d)\d* [+*/-] \d*(?:\)|\d)(?:.{3}))+')
        formula = re.search(r'.+[^=]',regex.search(formula).group().strip())
        return formula.group().strip()
    except AttributeError as e:
        print(formula, "raises", type(e))

if __name__ == '__main__':
    TEST_CASES = [
        'Add: 10 + 67 =',
        'Calculate: 99 - 85 =',
        '100 - 50 =',
        'Subtract: 76 - 30 =',
        '(40 + 51) - (41 + 32)=',
        '44 - = 25',
        'Fill in the box with the correct number:\n44 + - 30 = 44'
    ]
    for formula in TEST_CASES:
        parse = formula_filter(formula)
        print(formula, "(=)", parse)
