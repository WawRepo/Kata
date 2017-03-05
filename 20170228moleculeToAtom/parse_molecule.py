#Molecule to atoms
#https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python
import re
def parse_molecule (formula):
    with_one = reduce_parenhesis(full_molecule_count(formula))
    splited = re.split('(\d+)',with_one)
    i = 0
    dict = {}
    while i < len(splited) - 1:
        is_next_letter = splited[i].isalpha()
        if is_next_letter:
            if dict.has_key(splited[i]):
                dict[splited[i]] += int(splited[i+1])
            else:
                dict[splited[i]] = int(splited[i+1])
            i += 2
        else:
            if dict.has_key(splited[i]):
                dict[splited[i]] += 1
            else:
                dict[splited[i]] = 1
            i += 1
    return dict



def full_molecule_count(molecule):
    molecule_ = molecule + "_"
    return "".join([ c + '1'
                     if (c.isalpha() and not ( molecule_[i+1].isdigit() or molecule_[i+1].islower() ) )
                     or ( (c == ")" or c == "]" or c == "}" ) and not  molecule_[i+1].isdigit() )
                     else c
                     for i, c in enumerate(molecule)])

def reduce_parenhesis(molecule):
    brackets = identify_brackets(molecule)
    if len(brackets) == 0:
        return molecule
    else:
        return reduce_parenhesis(reduce_parenhesis_for_bracket(molecule, [brackets[0]]))

def identify_brackets(molecule):
    import math
    start = [i+.1 for i, x in enumerate(molecule) if x == "(" or x == "[" or x == "{"]
    end = [i+.2 for i, x in enumerate(molecule) if x == ")" or x == "]" or x == "}"]
    brackets = sorted(start + end)
    result = []
    while len(brackets) > 0 :
        for i, x in enumerate(brackets):
            if abs(math.modf(brackets[i] + brackets[i+1])[0] - .3) < .000001:
                result.append((int(brackets[i]) , int(brackets[i+1])))
                del brackets[i + 1]
                del brackets[i]
                break
    return result


def reduce_parenhesis_for_bracket(molecule, bracket):
    mul = molecule[bracket[0][1] + 1]
    if mul.isdigit():
        splited = re.split('(\d+)', molecule[bracket[0][0] + 1:bracket[0][1]])
        multiply = [ str(int(x)*int(mul)) if x.isdigit() else x for x in splited]
        return molecule[0:bracket[0][0]] + "".join( multiply) + molecule[bracket[0][1] + 2 :]
