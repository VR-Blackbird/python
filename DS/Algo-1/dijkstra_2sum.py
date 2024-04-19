# Dijkstra 2 Sum problem for Infix operators
from DS.ll.singly import LinkedList
import operator
import pdb

"""
Algorithm:
1. Value -> Push to thye value stack
2. Operator -> Push to Operator stack
3. Left paranthesis -> Ignore
4. Right paranthesis -> pop operator and two values in value stack; push the result of applying operator to those values
    onto operand stack
5. Repeat steps 1 to 5
"""
infix_op_string = "(1 + (( 22 + 3 ) * ( 4 * 5)))"
parse_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def parse_infix_operator(operators: str) -> int:
    values_stack = LinkedList()
    operator_stack = LinkedList()
    operators = operators.replace(" ", "")

    number = ""
    for idx, operator in enumerate(operators):
        if operator == "(":
            pass
        elif operator.isnumeric():
            number += operator
            if not operators[idx + 1].isnumeric():
                values_stack.append(int(number))
                number = ""
        elif operator == ")":
            value2 = values_stack.pop()
            value1 = values_stack.pop()
            operator_used = parse_dict.get(operator_stack.pop())

            result = operator_used(value1, value2)
            values_stack.append(result)
        else:
            operator_stack.append(operator)
    return values_stack.pop()


if __name__ == "__main__":
    sums = parse_infix_operator(infix_op_string)
    print(sums)
