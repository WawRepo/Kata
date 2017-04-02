from code_reader import *
# IMP [tab][line-feed] - Input/Output
#
# [space][space]: Pop a value off the stack and output it as a character.
# [space][tab]: Pop a value off the stack and output it as a number.
# [tab][space]: Read a character from input, a, Pop a value off the stack, b, then store the ASCII value of a at heap address b.
# [tab][tab]: Read a number from input, a, Pop a value off the stack, b, then store a at heap address b.


def stack_output_char(code_reader, stack, heap, input, output):
    # if len(stack) > 0:
    to_convert = stack.pop()
    output.append(str(unichr(to_convert)))

def stack_output_int(code_reader, stack, heap, input, output):
    #if len(stack) > 0:
    to_add = stack.pop()
    output.append(to_add)

def input_char_heap(code_reader, stack, heap, inp, output):
    # if len(inp) > 0:
    value = ord(inp[0][0])
    key = stack.pop()
    heap[key] = value
    inp[0] = inp[0][1:]


def input_int_heap(code_reader, stack, heap, inp, output):
    #if len(inp) > 0:
    value =  inp.pop(0)
    key = stack.pop()
    heap[key] = value

input_output_dict = {
    'ss': stack_output_char
    , 'st': stack_output_int
    , 'ts': input_char_heap
    , 'tt': input_int_heap
}


def input_output_flow(code_reader, stack, heap, input, output):
    control_value = code_reader.next()
    if not input_output_dict.has_key(control_value):
        control_value += code_reader.next()
    (input_output_dict[control_value])(code_reader, stack, heap, input, output)
