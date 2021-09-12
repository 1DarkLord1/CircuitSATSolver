import typing
import pycosat

from utils import parser

from common import entities
from common import constants


def gate_to_clause(gate: entities.Gate) -> typing.List[int]:
    return constants.CLAUSE_BUILDERS[gate.operation](
        gate.number,
        gate.inputs
    )


def solve_curcuit_sat(
        gates: typing.List[entities.Gate],
        out_gate: int
):
    clauses = []
    for gate in gates:
        clauses.extend(gate_to_clause(gate))
    clauses.append([out_gate])
    return pycosat.solve(clauses)


def execute_solver(input_file_name, output_file_name):
    with open(input_file_name, 'r') as input_file:
        lines = [line for line in input_file]

    output_gate, gates, num_to_name = parser.parse_bench(lines)
    solution = solve_curcuit_sat(gates, output_gate)

    if solution in ['UNKNOWN', 'UNSAT']:
        with open(output_file_name, 'w') as output_file:
            output_file.write(solution)
            exit(0)

    output_sol = [
        '{0} = {1}'.format(
            num_to_name[abs(v)],
            0 if v < 0 else 1
        )
        for v in solution if abs(v) in num_to_name
    ]

    with open(output_file_name, 'w') as output_file:
        output_file.write(str(output_sol).replace("'", ''))
