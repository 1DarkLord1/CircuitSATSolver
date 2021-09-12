import sys

from solver import csat_solver

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Wrong number of arguments')
        exit(2)
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    csat_solver.execute_solver(input_file_name, output_file_name)
