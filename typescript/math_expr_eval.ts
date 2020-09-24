
function in_to_postfix(expression: string): string {
    //Tokenize input
    let arr = [...expression.matchAll(/\(|\)|[\d.]+|\*|\-|\+|\//g)].map((x) => x[0]);
    let stack: Array<string>;
    let precedence = { "*": 2, "/": 2, "+": 1, "-": 1 };
    let postexpr: string;
    for (let token of arr) {
        if (token === "(") {
            stack.push(token);
        }
        if (token.match(/\d+/g)) {
            postexpr += token;
        }
        if (token === ")") {
            while (cur !== "(") {
                var cur = stack.pop();
                postexpr += cur;
            }
        }
        if (["*", "+", "-", "/"].includes(token)) {
            while (true) {
                if (precedence[stack[stack.length -1]])
            }
        }
    }
    return "";
}
export function calc(expression: string): number {
    // evaluate `expression` and return result
    return 0;
}


in_to_postfix("(2 / (2 + 3.33) * 4) - -6")