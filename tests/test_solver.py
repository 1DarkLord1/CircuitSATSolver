from utils import parser
from solver import csat_solver


def test_base():
    for i in range(5):
        with open(f'simple_tests/test{i + 1}.bench') as input_file:
            lines = [line for line in input_file]

        line = ''.join(lines[0].split())
        answer = line[1:]
        output_gate, gates, num_to_name = parser.parse_bench(lines)
        solution = csat_solver.solve_curcuit_sat(gates, output_gate)

        if answer == 'UNSAT':
            assert answer == solution
        else:
            assert len(solution) > 0


def test_eda_tests():
    for i in range(2):
        with open(f'bench/test{i + 1}.bench') as input_file:
            lines = [line for line in input_file]

        output_gate, gates, num_to_name = parser.parse_bench(lines)
        solution = csat_solver.solve_curcuit_sat(gates, output_gate)

        assert len(solution) > 0
