import numpy as np
import SLLStack
import ArrayStack
import ChainedHashTable
import DLList
import operator
import re

import BinaryTree


def _make_tokens(expr: str) -> list:
    variables = [x for x in re.split('\W+', expr) if x.isalnum()]
    ee = re.split('\w+', expr)
    tokens = []
    while len(variables) > 0 and len(ee) > 0:
        if len(ee[0]) < 2:
            tokens.append(ee[0])
        else:
            for c in ee[0]:
                tokens.append(c)
        del ee[0]
        tokens.append(variables[0])
        del variables[0]

    while len(ee) > 0:
        if len(ee[0]) < 2:
            tokens.append(ee[0])
        else:
            for c in ee[0]:
                tokens.append(c)
        del ee[0]
    return tokens


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        parens = ArrayStack.ArrayStack()
        for c in s:
            if c == "(":
                parens.push(c)
            if c == ")":
                if parens.size() > 0:
                    parens.pop()
                else:
                    return False
        return parens.size() == 0

    def print_expression(self, expr: str):
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]
        e = re.split('\w+', expr)
        for i in range(len(variables)):
            var = variables[i]
            val = self.dict.find(var)
            if val is not None:
                variables[i] = str(val)
        exp2 = ""
        while len(variables) > 0 and len(e) > 0:
            exp2 += e[0] + variables[0]
            del variables[0]
            del e[0]

        while len(e) > 0:
            exp2 += e[0]
            del e[0]
        print(exp2)
        return exp2

    def evaluate(self, expr: str):
        parse_tree = self._build_parse_tree(expr)
        return self._evaluate(parse_tree.r)

    def _evaluate(self, u: BinaryTree.BinaryTree.Node):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left is not None and u.right is not None:
            return op[u.v](self._evaluate(u.left), self._evaluate(u.right))
        elif u.left is None and u.right is None:
            if u.k is None:
                raise ValueError(f"Missing operand after {u.parent.k}.")
            elif u.v is not None:
                return u.v
            else:
                raise ValueError(f"Missing value for variable '{u.k}'")
        else:
            raise ValueError(f"Missing an operand and/or operator before {u.left.v}.")

    def _build_parse_tree(self, expr: str) -> str:
        if not self.matched_expression(expr):
            raise ValueError("Expression contains unmatched parenthesis.")
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node()
        current = t.r
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]
        tokens = _make_tokens(expr)
        for token in tokens:
            if token == '(':
                current.insert_left(BinaryTree.BinaryTree.Node())
                current = current.left
            elif token in ['+', '-', '*', '/']:
                current.set_key(token)
                current.set_val(token)
                current.insert_right(BinaryTree.BinaryTree.Node())
                current = current.right
            elif token == ')':
                current = current.parent
            elif token in variables:
                current.set_key(token)
                current.set_val(self.dict.find(token))
                current = current.parent
            else:
                raise ValueError(f"{token} is an invalid token in the expression")
        return t


