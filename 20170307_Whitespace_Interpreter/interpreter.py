from code_reader import *
from stack import *
from arithmetic import *
from heap import *
from input_output import *
from flow_control import *

imp_dict = {
    's': stack_flow #"Stack Manipulation"
    , 'ts': arithmetic_flow #"Arithmetic"
    , 'tt': heap_flow #"Heap Access"
    , 'tn': input_output_flow #"Input/Output"
    , 'n': flow_control_flow #Flow Control
}

def main_flow(code_reader, stack, heap = {}, inp = [], output = []):
    control_value = code_reader.next()
    if not imp_dict.has_key(control_value):
        control_value += code_reader.next()
    (imp_dict[control_value])(code_reader, stack, heap, inp, output)


def whitespace(code, inp=''):
    """  https://www.codewars.com/kata/whitespace-interpreter/train/python """
    code_validation(code)
    comment_removed = comment_remover(code)
    code_rdr = code_reader(unbleach(comment_removed))

    inp = inp.split("\n")

    output = []
    stack = []
    heap = {}

    try:
        while code_rdr:
            main_flow(code_rdr, stack, heap, inp, output)
    except StopIteration:
        pass

    return "".join([str(c) for c in output])


# to help with debugging
def unbleach(n):
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

def code_validation(code):
    if code is None or code == '':
        raise ValueError('Code not admisible')

def comment_remover(code):
    code_cleaned = ""
    for i in range(0, len(code)):
        if  code[i] in ['\t', '\n', ' '] :
            code_cleaned += code[i]
    return code_cleaned