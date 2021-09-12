import typing


def and_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [-sink, source[0]],
        [-sink, source[1]],
        [sink, -source[0], -source[1]],
    ]


def or_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [-sink, source[0], source[1]],
        [sink, -source[0]],
        [sink, -source[1]],
    ]


def xor_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [-sink, -source[0], -source[1]],
        [-sink, source[0], source[1]],
        [sink, -source[0], source[1]],
        [sink, source[0], -source[1]]
    ]


def nand_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [sink, source[0]],
        [sink, source[1]],
        [-sink, -source[0], -source[1]],
    ]


def nor_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [-sink, -source[0]],
        [-sink, -source[1]],
        [sink, source[0], source[1]],
    ]


def nxor_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [-sink, source[0]],
        [sink, -source[0]],
        [-source[0], source[1]],
        [source[0], -source[1]],
    ]


def not_builder(
        sink: int,
        source: typing.List[int]
) -> typing.List:
    return [
        [-sink, -source[0]],
        [sink, source[0]]
    ]
