#Molecule to atoms
#https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python
def parse_molecule (formula):
    import re

    with_one = full_molecule_count(formula)
    splited  = re.split('(\d+)',with_one)
    print splited
    is_letter = True
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
    print dict
    return dict


def full_molecule_count(molecule):
    molecule_ = molecule + "_"
    return "".join([ c + '1' if c.isalpha() and not ( molecule_[i+1].isdigit() or molecule_[i+1].islower() ) else c
                     for i, c in enumerate(molecule)])