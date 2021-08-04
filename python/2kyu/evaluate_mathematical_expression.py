
import re
import math

def in_to_postfix(expression):
    # Tokenize input
    if re.search(r'[^\d]\s*-\(', expression):
        expression = re.sub(r'-\(', '~(', expression)
    arr = re.findall(r'\(|\)|\-?[\d.]+|\*|\-|\+|\/|~', expression)
    stack = []
    precedence = {"*": 2, "/": 2, "+": 1, "-": 1, "~":3}
    postexpr = []
    for token in arr:
        if token == "(":
            stack.append(token)
        if re.match(r'-?[\d.]+', token):
            postexpr.append(token)
        if token == ")":
            cur = stack.pop()
            while cur != "(":
                postexpr.append(cur)
                cur = stack.pop()
        if token in ["*", "+", "-", "/", "~"]:
            while True:
                if precedence.get(stack[-1] if stack else '', 0) >= precedence.get(token):
                    postexpr.append(stack.pop())
                else:
                    stack.append(token)
                    break
    while stack:
        postexpr += stack.pop()
    return postexpr


def eval_post(expression):
    stack = []

    funcs = {"*": lambda x, y: y * x,
             "/": lambda x, y: y / x,
             "+": lambda x, y: y + x,
             "-": lambda x, y: y - x,
             "~": lambda x: -1 * x
             }
    for token in expression:
        if token in ["*", "+", "-", "/", "~"]:
            if len(stack) == 1 and token == "-":
                stack.append(-1 * float(stack.pop()))
                continue
            if token == "~":
                stack.append(funcs[token](float(stack.pop())))
                continue
            stack.append(funcs[token](float(stack.pop()), float(stack.pop())))
        else:
            stack.append(token)
    return math.fsum([float(x) for x in stack])

def calc(expression):
    a = in_to_postfix(expression)
    b = eval_post(a)
    return int(b) if b.is_integer() else b