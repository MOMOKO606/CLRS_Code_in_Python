from functools import reduce
"""
A Pythonic with closure code of Horner's rule for computing the polynomial equation.
Input @para: a single number x.
Output: function para_of which requires the two coefficients  as its put.
"""
def poly_equa(x):

    """
    Input @para: two coefficients a2 and a1.
    Output: the result of the equation a1 + a2 * x.
    """
    def para_of(a2, a1):
        return a1 + a2 * x

    #  When you return a function, don't write () after the function name.
    return para_of

polynomial_equation = poly_equa(2)  # Set x = 2.
print(reduce(polynomial_equation, [3,2,1,0]))