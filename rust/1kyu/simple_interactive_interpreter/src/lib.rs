use regex::Regex;
use std::collections::VecDeque;
use std::collections::{HashMap, HashSet};
use std::iter::FromIterator;

fn tokenize(expression: &str) -> Vec<String> {
    Regex::new(r"\s*(=>|[-+*/%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
        .unwrap()
        .find_iter(expression)
        .map(|m| m.as_str().trim().to_string())
        .collect::<Vec<String>>()
}

fn in_to_postfix(expression: Vec<&String>) -> Vec<String> {
    let mut stack = Vec::new();
    let mut postexpr = Vec::new();
    let precedence = HashMap::from([
        ("=".to_string(), 3),
        ("*".to_string(), 2),
        ("/".to_string(), 2),
        ("%".to_string(), 2),
        ("+".to_string(), 1),
        ("-".to_string(), 1),
    ]);
    let num_re = Regex::new(r"-?[\d.]+|[A-Za-z_][A-Za-z0-9_]*").unwrap();

    for token in expression {
        if token == "(" {
            stack.push(token);
        } else if token == ")" {
            let mut cur = stack.pop().unwrap();
            while cur != "(" {
                postexpr.push(cur.clone());
                cur = stack.pop().unwrap();
            }
        } else if num_re.is_match(&token) {
            postexpr.push(token.clone());
        } else if precedence.contains_key(token) {
            loop {
                let last = match stack.last() {
                    Some(s) => (*s).clone(),
                    None => "".to_string(),
                };
                if precedence.get(&last).map_or(&0, |s| s) >= precedence.get(token).unwrap() {
                    postexpr.push(stack.pop().unwrap().clone());
                } else {
                    stack.push(token);
                    break;
                }
            }
        }
    }
    while let Some(s) = stack.pop() {
        postexpr.push(s.clone());
    }
    postexpr
}

struct Interpreter {
    vars: HashMap<String, String>,
    funcs: HashMap<String, (Vec<String>, Vec<String>)>,
}

impl Interpreter {
    fn eval_post(&mut self, expression: &Vec<String>) -> Result<f32, String> {
        let mut stack: Vec<String> = Vec::new();
        let mut ops: HashMap<String, fn(f32, f32) -> f32> = HashMap::new();
        ops.insert("*".to_string(), |x, y| y * x);
        ops.insert("/".to_string(), |x, y| y / x);
        ops.insert("%".to_string(), |x, y| y % x);
        ops.insert("+".to_string(), |x, y| y + x);
        ops.insert("-".to_string(), |x, y| y - x);
        ops.insert("=".to_string(), |_, y| y);

        for token in expression {
            if ops.contains_key(token) {
                let op = ops.get(token).unwrap();
                if token == "=" {
                    let x = stack.pop().unwrap();
                    let y = stack.pop().unwrap();
                    self.insert_variable(&y, &[x.to_string()])?;
                    stack.push(x);
                } else {
                    let x = match stack.pop().unwrap().parse() {
                        Ok(val) => val,
                        Err(_) => return Err("No such variable".to_string())
                    };
                    let y = match stack.pop().unwrap().parse() {
                        Ok(val) => val,
                        Err(_) => return Err("No such variable".to_string())
                    };
                    stack.push(op(x, y).to_string());
                }
            } else {
                stack.push(token.clone());
            }
        }
        match stack.len() {
            1 => match stack[0].parse() {
                Ok(s) => Ok(s),
                Err(_) => Err("Invalid Expression".to_string())
            },
            _ => Err("Invalid Expression".to_string()),
        }
    }

    fn eval_expr(&mut self, input: &[String]) -> Result<f32, String> {
        let var_re = Regex::new(r"[A-Za-z_][A-Za-z0-9_]*").unwrap();
        let parsed_input: Result<Vec<_>, _> = input
            .iter()
            .map(|s| match var_re.is_match(s) {
                true => Ok(self.vars.get(s).map_or(s, |x| x)),
                false => Ok(s),
            })
            .collect();

        match parsed_input {
            Ok(expression) => self.eval_post(&in_to_postfix(expression)),
            Err(e) => Err(e),
        }
    }

    fn eval_func(&mut self, input: &[String]) -> Result<f32, String> {
        let var_re = Regex::new(r"[A-Za-z_][A-Za-z0-9_]*").unwrap();
        let mut stack = Vec::from(input);
        let mut var_queue = VecDeque::new();
        while let Some(value) = stack.pop() {
            if let Some(expr) = self.funcs.get(&value) {
                if expr.0.len() > var_queue.len() {
                    return Err(format!(
                        "Wrong number of arguments, expected {:}, got {:}",
                        expr.0.len(),
                        var_queue.len()
                    ));
                }

                let mut selected = Vec::new();

                for _ in 0..expr.0.len() {
                    selected.push(var_queue.pop_front().unwrap());
                }

                let vars: HashMap<&String, &String> =
                    HashMap::from_iter(expr.0.iter().zip(selected.iter()));

                let parsed_input: Vec<_> = expr
                    .1
                    .iter()
                    .map(|s| match var_re.is_match(s) {
                        true => vars.get(s).unwrap(),
                        false => s,
                    })
                    .collect();

                let res = self.eval_post(&in_to_postfix(parsed_input))?;
                stack.push(res.to_string());
                continue;
            }

            var_queue.push_front(value);
        }
        match var_queue.len() {
            1 => Ok(var_queue[0].parse().unwrap()),
            _ => Err("Wrong number of arguments".to_string()),
        }
    }

    fn calc(&mut self, input: &[String]) -> Result<f32, String> {
        if self.funcs.contains_key(&input[0]) {
            return self.eval_func(input);
        }
        return self.eval_expr(input);
    }

    fn new() -> Interpreter {
        Self {
            vars: HashMap::new(),
            funcs: HashMap::new(),
        }
    }

    fn insert_variable(&mut self, name: &String, expr: &[String]) -> Result<Option<f32>, String> {
        if self.funcs.contains_key(name) {
            return Err("ERROR: There is already a function named '{name}' declared".to_string());
        }
        let var_re = Regex::new(r"[A-Za-z_][A-Za-z0-9_]*").unwrap();
        if !var_re.is_match(name) {
            return Err("Invalid identifier".to_string());
        }
        match self.calc(expr) {
            Ok(r) => {
                self.vars.insert(name.clone(), r.to_string());
                return Ok(Some(r));
            }
            Err(e) => return Err(e),
        };
    }

    fn insert_function(
        &mut self,
        name: &String,
        vars: &[String],
        expr: &[String],
    ) -> Result<Option<f32>, String> {
        if self.vars.contains_key(name) {
            return Err("ERROR: There is already a variable named '{name}' declared".to_string());
        }

        let var_re = Regex::new(r"[A-Za-z_][A-Za-z0-9_]*").unwrap();

        if !var_re.is_match(name) {
            return Err("Invalid identifier".to_string());
        }

        let mut uniq = HashSet::new();
        if !vars.iter().all(|x| uniq.insert(x)) {
            return Err("Duplicate arguments".to_string());
        }

        for token in expr {
            if var_re.is_match(token) && !vars.contains(token) {
                return Err("ERROR: Unknown identifier '{token}'".to_string());
            }
        }
        self.funcs
            .insert(name.clone(), (vars.to_vec(), expr.to_vec()));
        Ok(None)
    }

    fn input(&mut self, input: &str) -> Result<Option<f32>, String> {
        let tokens = tokenize(input);

        if tokens.len() == 0 {
            return Ok(None);
        } else if tokens.contains(&"=".to_string()) {

            return self.insert_variable(&tokens[0], &tokens[2..]);
        } else if let Some(idx) = tokens.iter().position(|t| t == "=>") {
            if tokens[0] != "fn" {
                return Err("Function is declared within an expression".to_string());
            }

            return self.insert_function(&tokens[1], &tokens[2..idx], &tokens[idx..]);
        }
        Ok(Some(self.calc(&tokens)?))
    }
}
