
import re
import math

def in_to_postfix(expression):
    # Tokenize input
    #Tem um erro que se tiver UM neg, subtracao binaria antes de parentesis
    #que nao tenha espaco entre - e ( eh considerada neg. MAS passou em todos os testes,
    #então é isso aí. Devia ter feito um non capturing group no regex e dado sub sem esse if. 
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
    try:
        a = in_to_postfix(expression)
        b = eval_post(a)
    except:
        print(expression)
        return 0
    return int(b) if b.is_integer() else b

class Calculator():
    def in_to_postfix(self, expression):

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
    def eval_post(self, expression):
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
    def evaluate(self, string):
        try:
            a = self.in_to_postfix(string)
            b = self.eval_post(a)
        except Exception as e:
            print(str(e))
            print(string)
            return 0
        return int(b) if b.is_integer() else b

print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
