import typing

from common import entities
from common import constants


def parse_input_output_gates(line: str) -> str:
    pos_l = line.find('(') + 1
    pos_r = line.find(')')
    gate_name = line[pos_l:pos_r]
    return gate_name


def store_gate(
    name_to_num: typing.Dict,
    gate_name: str,
    num: int
) -> int:
    num += 1
    name_to_num[gate_name] = num
    return num


def parse_input_nodes(args):
    nodes = args.split(',')
    return [''.join(node.split()) for node in nodes]


def parse_inner_gates(line: str):
    pos_equal = line.find('=')
    pos_l = line.find('(') + 1
    pos_r = line.find(')')

    in_names = parse_input_nodes(line[pos_l:pos_r])
    out_name = line[:pos_equal]
    op_name = line[pos_equal + 1:pos_l - 1]
    return out_name, in_names, op_name


def create_gates(
    name_to_num: typing.Dict,
    out_num: int,
    in_names: typing.List,
    op_name: str
):
    ctr = out_num
    gates = []
    last_num = name_to_num[in_names[0]]
    if len(in_names) == 1:
        gates.append(entities.Gate(
                out_num,
                constants.STR_TO_OPERATION[op_name],
                [last_num]
            )
        )
        return gates

    sz = len(in_names)
    for i, name in enumerate(in_names):
        if i == 0:
            continue
        num = name_to_num[name]
        if i < sz - 1:
            ctr += 1
        gates.append(
            entities.Gate(
                ctr if i < sz - 1 else out_num,
                constants.STR_TO_OPERATION[op_name],
                [last_num, num]
            )
        )
        last_num = num

    return ctr, gates


def parse_bench(lines: [str]) -> typing.Tuple:
    output_gate = None
    gates = []
    name_to_num = {}
    num_to_name = {}
    ctr = 0
    for raw_line in lines:
        line = ''.join(raw_line.split())
        if line == '':
            continue
        if line[:5] == 'INPUT':
            name = parse_input_output_gates(line)
            ctr = store_gate(name_to_num, name, ctr)
            num_to_name[ctr] = name
        elif line[:6] == 'OUTPUT':
            output_gate = parse_input_output_gates(line)
        elif line[0] != '#':
            out_name, in_names, op_name = parse_inner_gates(line)
            ctr = store_gate(name_to_num, out_name, ctr)
            ctr, new_gates = create_gates(
                name_to_num, ctr, in_names, op_name
            )
            gates.extend(new_gates)

    return name_to_num[output_gate], gates, num_to_name
