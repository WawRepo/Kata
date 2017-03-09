# IMP [space] - Stack Manipulation
#
# [space] (number): Push n onto the stack.
# [tab][space] (number): Duplicate the nth value from the top of the stack.
# [tab][line-feed] (number): Discard the top n values below the top of the stack from the stack. (For n<0 or n>=stack.length, remove everything but the top value.)
# [line-feed][space]: Duplicate the top value on the stack.
# [line-feed][tab]: Swap the top two value on the stack.
# [line-feed][line-feed]: Discard the top value on the stack.


def code_reader(code):
    """Code char generator"""
    for c in code:
        yield c

def read_until_terminal(code_reader):
    output_str = ''
    for c in code_reader:
        if c == 'n':
            break
        output_str += c
    return output_str


def stack_manipulation(code_reader, stack):
    control_value = code_reader.next()
    if not stack_dict.has_key(control_value):
        control_value += code_reader.next()
    (stack_dict[control_value])(code_reader, stack)


def stack_manipulation_push(code_reader, stack):
    to_push = read_until_terminal(code_reader)
    stack.append(parse_number(to_push))

def stack_manipulation_duplicate_nth(code_reader, stack):
    item_to_duplicate = len(stack) - parse_number(read_until_terminal(code_reader))
    stack[:] = stack[:item_to_duplicate] + [stack[item_to_duplicate]] + stack[item_to_duplicate:]

# IMP [space] - Stack Manipulation
#
# [space] (number): Push n onto the stack.
# [tab][space] (number): Duplicate the nth value from the top of the stack.
# [tab][line-feed] (number): Discard the top n values below the top of the stack from the stack. (For n<0 or n>=stack.length, remove everything but the top value.)
# [line-feed][space]: Duplicate the top value on the stack.
# [line-feed][tab]: Swap the top two value on the stack.
# [line-feed][line-feed]: Discard the top value on the stack.


stack_dict = {
    's': stack_manipulation_push
    , 'ts': stack_manipulation_duplicate_nth
    , 'tt': "Heap Access"
    , 'tn': "Input/Output"
    , 'n': "Flow Control"
}

def parse_number(number_wi_syntax):
    if number_wi_syntax == '':
        raise ValueError('Empty string not allowed')
    factor = 1 if number_wi_syntax[0] == 's' else -1
    return factor * int("".join([ '1' if c == 't' else '0' for c in number_wi_syntax[1:]]), 2)




imp_dict = {
    ' ': "Stack Manipulation"
    , '\t ': "Arithmetic"
    , '\t\t': "Heap Access"
    , '\t\n': "Input/Output"
    , '\n': "Flow Control"
}



def whitespace(code, inp=''):
    """  https://www.codewars.com/kata/whitespace-interpreter/train/python """
    code_validation(code)

    output = ''
    stack = []
    heap = {}
    # ...
    return output


# to help with debugging
def unbleach(n):
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

def code_validation(code):
    if code is None or code == '':
        raise ValueError('Code not admisible')