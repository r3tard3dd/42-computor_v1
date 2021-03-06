from Parser.Parser import Parser
from Utils.Utils import Utils
from Equation.Equation import Equation

test_str = "4 + 3 * X^2 + X^1 = - 5 * X^0"
term_re = r"(?P<term>[-+]?(?P<coef>\d*\.?\d*)\*?(?P<expo>X{1}\^\d+)?)"
# equation_re = "(^(\s*([+-]?)\s*\d*((\d*)(\.\d+)?\s*(\*{1}))?\s*(X(\^[012]?)?)? *[+-]?)+$)"
# equation_re= r'(^(([+-]?)\d*((\d*)(\.\d+)?[*]{1})?[^*](X(\^[012]?)?)?[^+-])+$)'
equation_re = r'(?P<term>[-+]?(?P<coef>\d*\.?\d*)\*?(?P<expo>X{1}\^\d+)?)+'

test_str = test_str.replace(' ', '')
both_sides = Utils.check_input(str_=test_str, reg=equation_re)
print(f'Both_sides: {both_sides}')
if both_sides:
    left_side = Parser.match_in_string(both_sides[0], term_re)
    # print(left_side)
#     right_side = Parser.match_in_string(both_sides[1], term_re)
#     Utils.switch_sign(right_side)
#     print(right_side)
#     equation_terms = left_side + right_side
#     print(equation_terms)
#     eq = Equation(equation_terms)
