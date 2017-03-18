from code_reader import *

# IMP [tab][tab] - Heap Access
#
# [space]: Pop a and b, then store a at heap address b.
# [tab]: Pop a and then push the value at heap address a onto the stack.

def stack_to_heap(code_reader, stack, heap ):
    if len(stack) > 1:
        key, value = stack.pop(), stack.pop()
        heap[key] = value

def heap_to_stack(code_reader, stack, heap ):
    if len(stack) > 0 and len(heap) > 0:
        address = stack.pop()
        stack.append(heap[address])


heap_dict = {
    's': stack_to_heap
    ,'t': heap_to_stack

}

def heap_flow(code_reader, stack, heap):
    control_value = code_reader.next()
    if not heap_dict.has_key(control_value):
        control_value += code_reader.next()
    (heap_dict[control_value])(code_reader, stack, heap)
