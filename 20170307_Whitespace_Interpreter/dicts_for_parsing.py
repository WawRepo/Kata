import code_reader
import flow_control

def do_nothing(code_reader, stack = [], heap = {}, inp = [], output = [], labels = {}, return_address= []):
    pass

def parse_label_only(code_reader, stack = [], heap = {}, inp = [], output = [], labels = {}, return_address= []):
    code_reader.read_until_terminal(code_reader)


input_output_dict = {
    'ss': do_nothing
    , 'st': do_nothing
    , 'ts': do_nothing
    , 'tt': do_nothing
}

arithmetic_dict = {
    'ss': do_nothing
    ,'st': do_nothing
    ,'sn': do_nothing
    ,'ts': do_nothing
    ,'tt': do_nothing
}

stack_dict = {
    's': parse_label_only
    , 'ts': parse_label_only
    , 'tn': parse_label_only
    , 'ns': do_nothing
    , 'nt': do_nothing
    , 'nn': do_nothing
}

heap_dict = {
    's': do_nothing
    ,'t': do_nothing
}

flow_control_dict = {
  'nn': flow_control.flow_control_exit
    , 'ss': flow_control.flow_control_mark_label
    , 'st': parse_label_only
    , 'sn': parse_label_only
    , 'ts': parse_label_only
    , 'tt': parse_label_only
    , 'tn': do_nothing
 }