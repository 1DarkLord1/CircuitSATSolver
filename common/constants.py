from enum import Enum

from common import clause_builders


class Operation(Enum):
    NOT = 'NOT'
    AND = 'AND'
    OR = 'OR'
    XOR = 'XOR'
    NAND = 'NAND'
    NOR = 'NOR'
    NXOR = 'NXOR'


CLAUSE_BUILDERS = {
    Operation.NOT: clause_builders.not_builder,
    Operation.AND: clause_builders.and_builder,
    Operation.OR: clause_builders.or_builder,
    Operation.XOR: clause_builders.xor_builder,
    Operation.NAND: clause_builders.nand_builder,
    Operation.NOR: clause_builders.nor_builder,
    Operation.NXOR: clause_builders.nxor_builder,
}

STR_TO_OPERATION = {
    'NOT': Operation.NOT,
    'OR': Operation.OR,
    'AND': Operation.AND,
    'XOR': Operation.XOR,
    'NAND': Operation.NAND,
    'NOR': Operation.NOR,
    'NXOR': Operation.NXOR,
}
