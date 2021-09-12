import typing
from common import constants


class Gate:
    def __init__(
        self,
        num: int,
        op: constants.Operation,
        inputs: typing.List[int]
    ):
        self.number = num
        self.operation = op
        self.inputs = inputs
