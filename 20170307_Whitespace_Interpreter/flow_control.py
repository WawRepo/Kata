from code_reader import *

# IMP [line-feed] - Flow Control
#
# [space][space] (label): Mark a location in the program with label n.
# [space][tab] (label): Call a subroutine with the location specified by label n.
# [space][line-feed] (label): Jump unconditionally to the position specified by label n.
# [tab][space] (label): Pop a value off the stack and jump to the label specified by n if the value is zero.
# [tab][tab] (label): Pop a value off the stack and jump to the label specified by n if the value is less than zero.
# [tab][line-feed]: Exit a subroutine and return control to the location from which the subroutine was called.
# [line-feed][line-feed]: Exit the program.

def flow_control_exit(code_reader, stack, heap, input, output, labels, return_address):
    # for c in code_reader:
    #     pass
    code_reader.close()

def flow_control_mark_label(code_reader, stack, heap, input, output, labels, return_address):
    label = read_until_terminal(code_reader)
    position = code_reader.position()
    if labels.has_key(label):
        raise KeyError("Label already exist")
    labels[label] = position

def flow_control_call_subroutine(code_reader, stack, heap, input, output, labels, return_address):
    label = read_until_terminal(code_reader)
    return_address.append(code_reader.position())
    code_reader.move(labels[label])

def flow_control_jump_unconditionally(code_reader, stack, heap, input, output, labels, return_address):
    label = read_until_terminal(code_reader)
    code_reader.move(labels[label])

# def flow_control_jump_unconditionally(code_reader, stack, heap, input, output, labels, return_address):
#     label = read_until_terminal(code_reader)
#     if labels.has_key(label):
#         code_reader.move(labels[label])

def flow_control_jump_if_zero_stack(code_reader, stack, heap, input, output, labels, return_address):
    label = read_until_terminal(code_reader)
    if stack.pop() == 0:
        code_reader.move(labels[label])

def flow_control_jump_if_less_zero_stack(code_reader, stack, heap, input, output, labels, return_address):
    label = read_until_terminal(code_reader)
    if stack.pop() < 0:
        code_reader.move(labels[label])

def flow_control_exit_subroutine(code_reader, stack, heap, input, output, labels, return_address):
    position = return_address.pop()
    code_reader.move(position)
#
# def flow_control_flow(code_reader, stack, heap, input, output, labels, return_address):
#     control_value = code_reader.next()
#     if not flow_control_dict.has_key(control_value):
#         control_value += code_reader.next()
#     (flow_control_dict[control_value])(code_reader, stack, heap, input, output, labels, return_address)
