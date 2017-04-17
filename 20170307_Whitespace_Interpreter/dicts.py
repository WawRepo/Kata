import input_output
import arithmetic
import stack
import heap
import flow_control

input_output_dict = {
    'ss': input_output.stack_output_char
    , 'st': input_output.stack_output_int
    , 'ts': input_output.input_char_heap
    , 'tt': input_output.input_int_heap
}

arithmetic_dict = {
    'ss': arithmetic.arithmetic_add
    ,'st': arithmetic.arithmetic_substract
    ,'sn': arithmetic.arithmetic_multiply
    ,'ts': arithmetic.arithmetic_divide
    ,'tt': arithmetic.arithmetic_modulo
}

stack_dict = {
    's': stack.stack_manipulation_push
    , 'ts': stack.stack_manipulation_duplicate_nth
    , 'tn': stack.stack_manipulation_discard_n
    , 'ns': stack.stack_manipulation_duplicate_top
    , 'nt': stack.stack_manipulation_swap
    , 'nn': stack.stack_manipulation_discard_top
}

heap_dict = {
    's': heap.stack_to_heap
    ,'t': heap.heap_to_stack
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