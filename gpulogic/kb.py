from abc import ABC
from typing import Iterable, Optional, Union, List, Any


class Term(ABC):
    def __init__(self, idx: int):
        self.idx = idx

    def __eq__(self, other):
        return type(self) == type(other) and self.idx == other.idx

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.idx)})"

    def __hash__(self):
        return hash(repr(self))


class Constant(Term):
    pass


class Variable(Term):
    pass


class Atom(object):
    args: list[Term]

    def __init__(self, idx: int, args: Optional[list[Term]] = None):
        self.idx = idx
        self.args = args if args is not None else []

    def __eq__(self, other):
        return type(self) == type(other) and self.idx == other.idx and self.args == other.args

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.idx)}, {repr(self.args)})"

    def __hash__(self):
        return hash(repr(self))


class Rule(object):
    head: list[Atom]
    tail: list[Atom]

    def __init__(self, head: Union[Atom, list[Atom]], tail: Optional[list[Atom]] = None):
        self.head = head if isinstance(head, list) else [head]
        self.tail = tail if tail is not None else []

    def __eq__(self, other):
        return type(self) == type(other) and self.head == other.head and self.tail == other.tail

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.head)}, {repr(self.tail)})"

    def __hash__(self):
        return hash(repr(self))


class KnowledgeBase(object):
    def __init__(self, rules: Iterable[Rule]):
        self.rules = set(rules)

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.rules)})"
