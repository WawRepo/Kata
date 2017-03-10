from interpreter import *

# IMP [space] - Stack Manipulation
#
# [space] (number): Push n onto the stack.
# [tab][space] (number): Duplicate the nth value from the top of the stack.
# [tab][line-feed] (number): Discard the top n values below the top of the stack from the stack. (For n<0 or n>=stack.length, remove everything but the top value.)
# [line-feed][space]: Duplicate the top value on the stack.
# [line-feed][tab]: Swap the top two value on the stack.
# [line-feed][line-feed]: Discard the top value on the stack.


def stack_manipulation(code_reader, stack):
    control_value = code_reader.next()
    if not stack_dict.has_key(control_value):
        control_value += code_reader.next()
    (stack_dict[control_value])(code_reader, stack)


def stack_manipulation_push(code_reader, stack):
    to_push = read_until_terminal(code_reader)
    stack.append(parse_number(to_push))


def stack_manipulation_duplicate_nth(code_reader, stack):
    item_to_duplicate = len(stack) - 1 - parse_number(read_until_terminal(code_reader))
    if item_to_duplicate < 0 or item_to_duplicate >= len(stack):
        return
    stack[:] = stack[:item_to_duplicate] + [stack[item_to_duplicate]] + stack[item_to_duplicate:]


def stack_manipulation_discard_n(code_reader, stack):
    items_to_discard = len(stack) - 2 - parse_number(read_until_terminal(code_reader))
    if items_to_discard < 0 or items_to_discard >= len(stack) - 1:
        stack[:] = [stack[-1]]
    else:
        stack[:] = stack[:items_to_discard] + [stack[-1]]


def stack_manipulation_duplicate_top(code_reader, stack):
    stack.append(stack[-1])


def stack_manipulation_swap(code_reader, stack):
    if len(stack) >= 2:
        stack[-1], stack[-2] = stack[-2], stack[-1]


def stack_manipulation_discard_top(code_reader, stack):
    if len(stack) > 0:
        stack.pop()


stack_dict = {
    's': stack_manipulation_push
    , 'ts': stack_manipulation_duplicate_nth
    , 'tn': stack_manipulation_discard_n
    , 'ns': stack_manipulation_duplicate_top
    , 'nt': stack_manipulation_swap
    , 'nn': stack_manipulation_discard_top
}