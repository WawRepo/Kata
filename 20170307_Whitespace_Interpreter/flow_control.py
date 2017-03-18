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

def flow_control_exit(code_reader, stack, heap, input, output):
    for c in code_reader:
        pass

flow_control_dict = {
  'nn': flow_control_exit
}

def flow_control_flow(code_reader, stack, heap, input, output):
    control_value = code_reader.next()
    if not flow_control_dict.has_key(control_value):
        control_value += code_reader.next()
    (flow_control_dict[control_value])(code_reader, stack, heap, input, output)
