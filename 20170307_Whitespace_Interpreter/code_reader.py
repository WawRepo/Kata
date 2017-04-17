# def code_reader(code):
#     """Code char generator"""
#     for c in code:
#         if c == 't' or c == 'n' or c =='s':
#             yield c



class code_reader:
    """
    CodeReader class will provide 3 main functions:
    next() works as generator defined on string 
    position() gives a position of char that next() is going to return
    move(i) move cursor to position i
    """

    def __init__(self, code):
        self._code = code
        self._position = 0

    def __iter__(self):
        return self

    def next(self):
        pos = self._position
        if pos >= len(self._code):
            raise StopIteration
        self._position += 1
        return self._code[pos]

    def position(self):
        return self._position

    def move(self, i):
        if i < 0 or i >= len(self._code) :
            raise IndexError("Index out of bounds")
        self._position = i


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
    if len(number_wi_syntax) == 1:
        return 0
    factor = 1 if number_wi_syntax[0] == 's' else -1
    return factor * int("".join([ '1' if c == 't' else '0' for c in number_wi_syntax[1:]]), 2)