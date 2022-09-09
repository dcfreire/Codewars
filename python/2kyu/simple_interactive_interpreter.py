import re

def in_to_postfix(arr):
    stack = []
    precedence = {"*": 2, "/": 2, "+": 1, "-": 1, "%": 2}
    postexpr = []
    for token in arr:
        if token == "(":
            stack.append(token)
        if re.match(r"-?[\d.]+", token):
            postexpr.append(token)
        if token == ")":
            cur = stack.pop()
            while cur != "(":
                postexpr.append(cur)
                cur = stack.pop()
        if token in ["*", "+", "-", "/", "%"]:
            while True:
                if precedence.get(stack[-1] if stack else "", 0) >= precedence.get(token):
                    postexpr.append(stack.pop())
                else:
                    stack.append(token)
                    break
    while stack:
        postexpr += stack.pop()
    return postexpr


def eval_post(expression):
    stack = []

    funcs = {
        "*": lambda x, y: y * x,
        "/": lambda x, y: y / x,
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "%": lambda x, y: y % x,
    }
    for token in expression:
        if token in ["*", "+", "-", "/", "%"]:
            stack.append(funcs[token](float(stack.pop()), float(stack.pop())))
        else:
            stack.append(token)
    if len(stack) > 1:
        raise Exception
    return [float(x) for x in stack][0]


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile(r"\s*([-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def calc(self, expression):
        a = [self.vars.get(t, t) for t in expression]
        if list(filter(re.compile(r"[a-zA-Z]").match, a)):
            raise Exception
        a = in_to_postfix(a)
        b = eval_post(a)

        return int(b) if b.is_integer() else b

    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        tokens = tokenize(expression)
        if not tokens:
            return ""
        if "=" in tokens:
            self.vars[tokens[0]] = str(self.calc(tokens[2:]))
            return int(self.vars[tokens[0]])
        else:
            return self.calc(tokens)
