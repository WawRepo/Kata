def code_reader(code):
    """Code char generator"""
    for c in code:
        yield c

# def code_reader(code):
#     length = len(code)
#     i = 0
#     while i < length:
#         val = (yield i)
#         if val != 'position':
#             yield code[i]
#             i += 1
# a = code_reader("foobar")
#
# print a.next()
# print a.send('position')
# print a.next()
# print a.send('position')
# print a.send('position')
# print a.next()
# print a.send('position')

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