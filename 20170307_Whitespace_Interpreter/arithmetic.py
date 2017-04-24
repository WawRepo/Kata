from code_reader import *

# IMP [tab][space] - Arithmetic
# [space][space]: Pop a and b, then push b+a.
# [space][tab]: Pop a and b, then push b-a.
# [space][line-feed]: Pop a and b, then push b*a.
# [tab][space]: Pop a and b, then push b/a*. If a is zero, throw an error.
# *Note that the result is defined as the floor of the quotient.
# [tab][tab]: Pop a and b, then push b%a*. If a is zero, throw an error.
# *Note that the result is defined as the remainder after division and sign (+/-) of the divisor (a).


def arithmetic_add(code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
    #if len(stack) > 1:
    stack.append(stack.pop() + stack.pop())


def arithmetic_substract(code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
    #if len(stack) > 1:
    stack.append( - stack.pop() + stack.pop())


def arithmetic_multiply(code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
    #if len(stack) > 1:
    stack.append(stack.pop() * stack.pop())


def arithmetic_divide(code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
    #if len(stack) > 1:
    a, b = stack.pop(), stack.pop()
    stack.append(b / a)

def arithmetic_modulo(code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
    #if len(stack) > 1:
    a, b = stack.pop(), stack.pop()
    stack.append(b % a)


def arithmetic_flow(code_reader, stack, heap=[], inp=[], output=[]):
    control_value = code_reader.next()
    if not aritmetic_dict.has_key(control_value):
        control_value += code_reader.next()
    (aritmetic_dict[control_value])(code_reader, stack)


aritmetic_dict = {
    'ss': arithmetic_add
    ,'st': arithmetic_substract
    ,'sn': arithmetic_multiply
    ,'ts': arithmetic_divide
    ,'tt': arithmetic_modulo
}