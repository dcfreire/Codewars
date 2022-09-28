#![allow(dead_code)]

use crate::Param::*;
use std::cmp::Ordering;
use std::collections::HashMap;

#[derive(Debug, Clone)]

enum Param {
    Register(String),
    Constant(i64),
}

impl From<&&str> for Param {
    fn from(x: &&str) -> Self {
        match x.parse::<i64>() {
            Ok(val) => Constant(val),
            Err(_) => Register(x.to_string()),
        }
    }
}
#[derive(Debug, Clone)]

enum Message {
    Register(String),
    Text(String),
}

impl From<&&str> for Message {
    fn from(x: &&str) -> Self {
        if x.chars().nth(0) == Some('\'') {
            Self::Text(x[1..x.len() - 1].to_string())
        } else {
            Self::Register(x.to_string())
        }
    }
}

#[derive(Debug, Clone)]
enum JumpCmp {
    Jmp(String),
    Jne(String),
    Je(String),
    Jge(String),
    Jg(String),
    Jle(String),
    Jl(String),
}

#[derive(Debug, Clone)]
enum Instruction {
    Jnz(Param, Param),
    Cmp(Param, Param),
    Mov(String, Param),
    Add(String, Param),
    Sub(String, Param),
    Mul(String, Param),
    Div(String, Param),
    Msg(Vec<Message>),
    Inc(String),
    Dec(String),
    Label(String),
    Jmp(String),
    JCmp(JumpCmp),
    Call(String),
    Comment,
    Ret,
    End,
    None,
}

fn split_instruction(ins: &str) -> Vec<&str> {
    let mut ret = Vec::new();
    match ins.split(' ').map(str::trim).collect::<Vec<_>>().as_slice() {
        ["msg", ..] => {
            ret.push("msg");
            let mut in_quote = false;
            let mut s = 3;
            for (idx, c) in ins[3..].chars().enumerate() {
                if c == '\'' {
                    in_quote = !in_quote;
                }
                if !in_quote && c == ',' {
                    ret.push(&ins[s..idx + 3].trim());
                    s = idx + 4;
                }
            }
            ret.push(&ins[s..].trim());
        }
        other => {
            let cmdlen = other[0].len();
            ret.push(other[0]);
            let contents = ins[cmdlen..]
                .split(',')
                .map(str::trim)
                .filter(|x| x.len() > 0);
            ret.append(&mut contents.collect::<Vec<_>>())
        }
    }
    ret
}

impl From<&str> for Instruction {
    fn from(ins: &str) -> Self {
        match split_instruction(ins).as_slice() {
            ["jnz", x, y] => Self::Jnz(Param::from(x), Param::from(y)),
            ["cmp", x, y] => Self::Cmp(Param::from(x), Param::from(y)),
            ["mov", x, y] => Self::Mov(x.to_string(), Param::from(y)),
            ["add", x, y] => Self::Add(x.to_string(), Param::from(y)),
            ["sub", x, y] => Self::Sub(x.to_string(), Param::from(y)),
            ["mul", x, y] => Self::Mul(x.to_string(), Param::from(y)),
            ["div", x, y] => Self::Div(x.to_string(), Param::from(y)),
            ["msg", tail @ ..] => Self::Msg(tail.iter().map(Message::from).collect()),
            ["inc", x] => Self::Inc(x.to_string()),
            ["dec", x] => Self::Dec(x.to_string()),
            ["jmp", x] => Self::Jmp(x.to_string()),
            ["jne", x] => Self::JCmp(JumpCmp::Jne(x.to_string())),
            ["je", x] => Self::JCmp(JumpCmp::Je(x.to_string())),
            ["jge", x] => Self::JCmp(JumpCmp::Jge(x.to_string())),
            ["jg", x] => Self::JCmp(JumpCmp::Jg(x.to_string())),
            ["jle", x] => Self::JCmp(JumpCmp::Jle(x.to_string())),
            ["jl", x] => Self::JCmp(JumpCmp::Jl(x.to_string())),
            ["call", x] => Self::Call(x.to_string()),
            ["ret"] => Self::Ret,
            ["end"] => Self::End,
            other => {
                if other.len() > 0 {
                    if other[0].chars().last() == Some(':') {
                        Self::Label(other[0][..other[0].len() - 1].to_string())
                    } else if other[0].starts_with(';') {
                        Self::Comment
                    } else {
                        Self::None
                    }
                } else {
                    Self::None
                }
            }
        }
    }
}

impl<T> Index<Ptr> for Vec<T> {
    type Output = T;
    fn index(&self, index: Ptr) -> &Self::Output {
        &self[index.ptr]
    }
}

#[derive(PartialEq, PartialOrd, Copy, Clone, Debug)]
struct Ptr {
    ptr: usize,
}

impl Into<usize> for Ptr {
    fn into(self) -> usize {
        self.ptr
    }
}

impl PartialEq<usize> for Ptr {
    fn eq(&self, other: &usize) -> bool {
        self.ptr == *other
    }
}

impl PartialOrd<usize> for Ptr {
    fn partial_cmp(&self, other: &usize) -> Option<std::cmp::Ordering> {
        self.ptr.partial_cmp(&other)
    }
}

use std::ops::{AddAssign, Index};
impl AddAssign<i64> for Ptr {
    fn add_assign(&mut self, rhs: i64) {
        if rhs < 0 {
            self.ptr -= rhs.abs() as usize
        } else {
            self.ptr += rhs as usize
        }
    }
}

struct AssemblerInterpreter {
    registers: HashMap<String, i64>,
    instructions: Vec<Instruction>,
    labels: HashMap<String, Ptr>,
    ptr: Ptr,
    prev_cmp: Option<Ordering>,
    call_stack: Vec<Ptr>,
    output: Vec<String>,
}

impl AssemblerInterpreter {
    fn set_labels(&mut self) {
        for (idx, ins) in self.instructions.iter().enumerate() {
            match ins {
                Instruction::Label(lbl) => {
                    self.labels.insert(lbl.clone(), Ptr { ptr: idx });
                }
                _ => continue,
            }
        }
    }

    fn new(ins: Vec<&str>) -> Self {
        let instructions = ins.into_iter().map(Instruction::from).collect::<Vec<_>>();
        Self {
            registers: HashMap::new(),
            instructions,
            labels: HashMap::new(),
            ptr: Ptr { ptr: 0 },
            prev_cmp: None,
            call_stack: Vec::new(),
            output: vec!["".to_string()],
        }
    }

    fn next(&mut self) {
        self.ptr += 1;
    }

    fn skip(&mut self, jump: i64) {
        self.ptr += jump;
    }

    fn goto(&mut self, pos: Ptr) {
        self.ptr = pos
    }

    fn mov(&mut self, x: String, y: Param) {
        self.ptr += 1;
        let num = self.get_param(y);
        self.registers.insert(x, num);
    }

    fn inc(&mut self, x: String) {
        match self.registers.get(&x) {
            Some(value) => {
                self.registers.insert(x, value + 1);
            }
            None => (),
        }
        self.next()
    }

    fn dec(&mut self, x: String) {
        match self.registers.get(&x) {
            Some(value) => {
                self.registers.insert(x, value - 1);
            }
            None => (),
        }
        self.next()
    }

    fn get_param(&self, x: Param) -> i64 {
        match x {
            Register(reg) => *self.registers.get(&reg).unwrap(),
            Constant(con) => con,
        }
    }

    fn jnz(&mut self, x: Param, y: Param) {
        let jump = self.get_param(x);
        if jump != 0 {
            let num = self.get_param(y);
            self.skip(num)
        } else {
            self.next()
        }
    }

    fn add(&mut self, x: String, y: Param) {
        let val = self.get_param(y);
        if let Some(num) = self.registers.get(&x) {
            self.registers.insert(x, *num + val);
        }
        self.next()
    }

    fn sub(&mut self, x: String, y: Param) {
        let val = self.get_param(y);
        if let Some(num) = self.registers.get(&x) {
            self.registers.insert(x, *num - val);
        }
        self.next()
    }

    fn mul(&mut self, x: String, y: Param) {
        let val = self.get_param(y);
        if let Some(num) = self.registers.get(&x) {
            self.registers.insert(x, *num * val);
        }
        self.next()
    }

    fn div(&mut self, x: String, y: Param) {
        let val = self.get_param(y);
        if let Some(num) = self.registers.get(&x) {
            self.registers.insert(x, *num / val);
        }
        self.next()
    }

    fn jmp(&mut self, lbl: String) {
        if let Some(pos) = self.labels.get(&lbl) {
            self.goto(*pos);
        }
        self.next()
    }

    fn cmp(&mut self, x: Param, y: Param) {
        let x_val = self.get_param(x);
        let y_val = self.get_param(y);
        self.prev_cmp = Some(x_val.cmp(&y_val));
        self.next()
    }

    fn jcmp(&mut self, ins: JumpCmp) {
        use JumpCmp::*;
        use Ordering::*;
        if let Some(cmp) = self.prev_cmp {
            match (cmp, ins) {
                (Equal, Je(lbl))
                | (Greater | Equal, Jge(lbl))
                | (Greater, Jg(lbl))
                | (Less | Equal, Jle(lbl))
                | (Less, Jl(lbl))
                | (Less | Greater, Jne(lbl)) => self.jmp(lbl),
                _ => self.next(),
            }
        }
    }

    fn call(&mut self, lbl: String) {
        self.call_stack.push(self.ptr);
        self.jmp(lbl);
    }

    fn ret(&mut self) {
        if let Some(pos) = self.call_stack.pop(){
            self.goto(pos)
        }
        self.next()
    }

    fn msg(&mut self, messages: Vec<Message>) {
        for m in messages {
            match m {
                Message::Register(reg) => self
                    .output
                    .push(self.registers.get(&reg).unwrap().to_string()),
                Message::Text(text) => self.output.push(text),
            }
        }
        self.next()
    }

    fn tokenize(input: &str) -> Vec<&str> {
        let mut ret = Vec::new();
        for mut line in input.split('\n').map(str::trim) {
            if let Some(idx) = line.find(';') {
                line = &line[..idx]
            }
            ret.push(line.trim())
        }
        ret.into_iter()
            .filter(|x| x.len() > 0)
            .collect::<Vec<&str>>()
    }
    fn run(&mut self) -> Result<(), ()> {
        let mut end = false;
        self.set_labels();

        while self.ptr < self.instructions.len() {
            let instruction = self.instructions[self.ptr].clone();
            match instruction {
                Instruction::Jnz(x, y) => self.jnz(x, y),
                Instruction::Cmp(x, y) => self.cmp(x, y),
                Instruction::Mov(x, y) => self.mov(x, y),
                Instruction::Add(x, y) => self.add(x, y),
                Instruction::Sub(x, y) => self.sub(x, y),
                Instruction::Mul(x, y) => self.mul(x, y),
                Instruction::Div(x, y) => self.div(x, y),
                Instruction::Msg(vec) => self.msg(vec),
                Instruction::Inc(x) => self.inc(x),
                Instruction::Dec(x) => self.dec(x),
                Instruction::Jmp(lbl) => self.jmp(lbl),
                Instruction::JCmp(cmp) => self.jcmp(cmp),
                Instruction::Call(lbl) => self.call(lbl),
                Instruction::Ret => self.ret(),
                Instruction::End => {
                    end = true;
                    break;
                }
                _ => self.next(),
            }
        }
        if end {
            Ok(())
        } else {
            Err(())
        }
    }

    pub fn interpret(input: &str) -> Option<String> {
        let lines = AssemblerInterpreter::tokenize(input);
        let mut interpreter = AssemblerInterpreter::new(lines);
        match interpreter.run() {
            Ok(()) => Some(interpreter.output.concat().to_string()),
            Err(()) => None
        }
    }
}

mod tests;
