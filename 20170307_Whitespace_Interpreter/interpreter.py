

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