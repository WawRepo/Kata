from collections import Mapping

import code_reader
import stack as st
import arithmetic
import heap as hp
import input_output
import flow_control

# imp_dict = {
#     's': stack_flow #"Stack Manipulation"
#     , 'ts': arithmetic_flow #"Arithmetic"
#     , 'tt': heap_flow #"Heap Access"
#     , 'tn': input_output_flow #"Input/Output"
#     , 'n': flow_control_flow #Flow Control
# }
#
# def main_flow(code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
#     control_value = code_reader.next()
#     if not imp_dict.has_key(control_value):
#         control_value += code_reader.next()
#     (imp_dict[control_value])(code_reader, stack, heap, inp, output, labels, return_address)




def flow(dict, code_reader, stack, heap = {}, inp = [], output = [], labels = {}, return_address= []):
    control_value = code_reader.next()
    if not dict.has_key(control_value):
        control_value += code_reader.next()
    if isinstance(dict[control_value], Mapping):
        flow(dict[control_value], code_reader, stack, heap, inp, output, labels, return_address)
    else:
        (dict[control_value])(code_reader, stack, heap, inp, output, labels, return_address)



def get_labels(code):
    def do_nothing(code_reader, stack=[], heap={}, inp=[], output=[], labels={}, return_address=[]):
        pass

    def parse_label_only(code_rdr, stack=[], heap={}, inp=[], output=[], labels={}, return_address=[]):
        code_reader.read_until_terminal(code_rdr)

    input_output_dict = {
        'ss': do_nothing
        , 'st': do_nothing
        , 'ts': do_nothing
        , 'tt': do_nothing
    }

    arithmetic_dict = {
        'ss': do_nothing
        , 'st': do_nothing
        , 'sn': do_nothing
        , 'ts': do_nothing
        , 'tt': do_nothing
    }

    stack_dict = {
        's': parse_label_only
        , 'ts': parse_label_only
        , 'tn': parse_label_only
        , 'ns': do_nothing
        , 'nt': do_nothing
        , 'nn': do_nothing
    }

    heap_dict = {
        's': do_nothing
        , 't': do_nothing
    }

    flow_control_dict = {
        'nn': flow_control.flow_control_exit
        , 'ss': flow_control.flow_control_mark_label
        , 'st': parse_label_only
        , 'sn': parse_label_only
        , 'ts': parse_label_only
        , 'tt': parse_label_only
        , 'tn': do_nothing
    }

    imp_dict = {
        's': stack_dict  # "Stack Manipulation"
        , 'ts': arithmetic_dict  # "Arithmetic"
        , 'tt': heap_dict  # "Heap Access"
        , 'tn': input_output_dict  # "Input/Output"
        , 'n': flow_control_dict  # Flow Control
    }

    code_rdr = code_reader.code_reader(code)
    inp = []
    output = []
    stack = []
    heap = {}
    labels = {}
    return_address = []

    try:
        while code_rdr:
            # main_flow(code_rdr, stack, heap, inp, output, labels, return_address)
            flow(imp_dict,code_rdr, stack, heap, inp, output, labels, return_address)
    except StopIteration:
        pass

    return labels


def whitespace(code, inp=''):
    """  https://www.codewars.com/kata/whitespace-interpreter/train/python """
    code_validation(code)
    comment_removed = comment_remover(code)
    code_rdr = code_reader.code_reader(unbleach(comment_removed))
    #code_rdr = CodeReader(unbleach(comment_removed))

    labels = get_labels(unbleach(comment_removed))

    inp = inp.split("\n")

    output = []
    stack = []
    heap = {}
    return_address = []

    input_output_dict = {
        'ss': input_output.stack_output_char
        , 'st': input_output.stack_output_int
        , 'ts': input_output.input_char_heap
        , 'tt': input_output.input_int_heap
    }

    arithmetic_dict = {
        'ss': arithmetic.arithmetic_add
        , 'st': arithmetic.arithmetic_substract
        , 'sn': arithmetic.arithmetic_multiply
        , 'ts': arithmetic.arithmetic_divide
        , 'tt': arithmetic.arithmetic_modulo
    }

    stack_dict = {
        's': st.stack_manipulation_push
        , 'ts': st.stack_manipulation_duplicate_nth
        , 'tn': st.stack_manipulation_discard_n
        , 'ns': st.stack_manipulation_duplicate_top
        , 'nt': st.stack_manipulation_swap
        , 'nn': st.stack_manipulation_discard_top
    }

    heap_dict = {
        's': hp.stack_to_heap
        , 't': hp.heap_to_stack
    }

    flow_control_dict = {
        'nn': flow_control.flow_control_exit
        , 'ss': flow_control.flow_control_mark_label
        , 'st': flow_control.flow_control_call_subroutine
        , 'sn': flow_control.flow_control_jump_unconditionally
        , 'ts': flow_control.flow_control_jump_if_zero_stack
        , 'tt': flow_control.flow_control_jump_if_less_zero_stack
        , 'tn': flow_control.flow_control_exit_subroutine
    }

    imp_dict = {
        's': stack_dict  # "Stack Manipulation"
        , 'ts': arithmetic_dict  # "Arithmetic"
        , 'tt': heap_dict  # "Heap Access"
        , 'tn': input_output_dict  # "Input/Output"
        , 'n': flow_control_dict  # Flow Control
    }

    try:
        while code_rdr:
            # main_flow(code_rdr, stack, heap, inp, output, labels, return_address)
            flow(imp_dict,code_rdr, stack, heap, inp, output, labels, return_address)
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