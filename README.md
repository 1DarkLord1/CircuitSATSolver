# CurcuitSATSolver

#### Солвер основан на sat-солвере pycosat, поэтому необходимо установить эту библиотеку:
``` pip install pycosat ```

#### Тестирование осуществляется с помощью библиотеки pytest:
``` pip install pytest ```

#### Запуск тестов (осуществляется из корня):
``` pytest test_solver.py ```

#### Точка входа программы main.py (запускать из корня):
``` python3 main.py <input_file_name> <output_file_name> ```

### ВНИМАНИЕ!!! Входные данные должны быть в формате BENCH! 
#### Поддерживаемые типы операций: AND, OR, XOR, NAND, NOR, NXOR, NOT.
