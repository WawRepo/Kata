from interpreter import *

# IMP [tab][tab] - Heap Access
#
# [space]: Pop a and b, then store a at heap address b.
# [tab]: Pop a and then push the value at heap address a onto the stack.

# def stack_to_heap(code_reader, stack, heap):
#     if len(stack) > 1:
#         stack.append(stack.pop() + stack.pop())
#
# heap_dict = {
#     's': stack_to_heap
#     ,'t': heap_to_stack
#
# }

def some_function():
    for i,x in enumerate("zsd"):
        val = (yield x)
        if val == 'len':
            yield i

a = some_function()

print a.next()
print a.send('len')
# print a.next()
print a.send('len')
print a.send('len')
print a.send('len')
#
#
# for i in a:
#     print i, a.send('len')
#

