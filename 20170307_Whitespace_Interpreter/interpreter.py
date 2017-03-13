from code_reader import *
from stack import *
from arithmetic import *
from heap import *
from input_output import *

imp_dict = {
    's': stack_flow #"Stack Manipulation"
    , 'ts': arithmetic_flow #"Arithmetic"
    , 'tt': heap_flow #"Heap Access"
    , 'tn': input_output_flow #"Input/Output"
    , 'n': "Flow Control"
}

def main_flow(code_reader, stack, heap = {}, inp = [], output = []):
    control_value = code_reader.next()
    if not stack_dict.has_key(control_value):
        control_value += code_reader.next()
    (imp_dict[control_value])(code_reader, stack, heap, inp, output)


def whitespace(code, inp=''):
    """  https://www.codewars.com/kata/whitespace-interpreter/train/python """
    code_validation(code)
    code_rdr = code_reader(unbleach(code))

    inp = list (inp)

    output = []
    stack = []
    heap = {}

    while code_rdr:
        main_flow(code_rdr, stack, heap, inp, output)

    return "".join(output)


# to help with debugging
def unbleach(n):
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

def code_validation(code):
    if code is None or code == '':
        raise ValueError('Code not admisible')