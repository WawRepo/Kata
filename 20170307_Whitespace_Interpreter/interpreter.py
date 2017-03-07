
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