use crate::Param::*;
use std::collections::HashMap;

enum Param {
    Register(String),
    Constant(i64),
}

impl From<&&str> for Param {
    fn from(x: &&str) -> Self {
        match x.parse::<i64>() {
            Ok(val) => {
                Constant(val)
            }
            Err(_) => {
                Register(x.to_string())
            }
        }
    }
}

enum Instruction {
    Mov(String, Param),
    Inc(String),
    Dec(String),
    Jnz(Param, Param),
    None
}

impl From<&str> for Instruction {
    fn from(ins: &str) -> Self {
        match ins.split(' ').collect::<Vec<&str>>().as_slice() {
            ["mov", x, y] => Self::Mov(x.to_string(), Param::from(y)),
            ["inc", x] => Self::Inc(x.to_string()),
            ["dec", x] => Self::Dec(x.to_string()),
            ["jnz", x, y] => Self::Jnz(Param::from(x), Param::from(y)),
            _ => Self::None,
        }
    }
}

#[derive(PartialEq, PartialOrd)]
struct Ptr {
    ptr: usize
}

impl Into<usize> for Ptr {
    fn into(self) -> usize {
        self.ptr
    }
}



use std::ops::AddAssign;
impl AddAssign<i64> for Ptr {
    fn add_assign(&mut self, rhs: i64) {
        if rhs < 0 {
            self.ptr -= rhs.abs() as usize
        } else {
            self.ptr += rhs as usize
        }
    }
}


struct Assembler<'a> {
    registers: HashMap<String, i64>,
    instructions: Vec<&'a str>,
    ptr: Ptr,
}

impl<'a> Assembler<'a> {
    fn new(instructions: Vec<&'a str>) -> Self {
        Self {
            registers: HashMap::new(),
            instructions,
            ptr: Ptr{ptr: 0},
        }
    }

    fn mov(&mut self, x: String, y: Param) {
        self.ptr += 1;
        match y {
            Register(reg) => {
                let val = self.registers.get(&reg).unwrap();
                self.registers.insert(x, *val)
            }
            Constant(con) => self.registers.insert(x, con),
        };
    }

    fn inc(&mut self, x: String) {
        self.ptr += 1;
        match self.registers.get(&x) {
            Some(value) => {
                self.registers.insert(x, value + 1);
            }
            None => (),
        }
    }

    fn dec(&mut self, x: String) {
        self.ptr += 1;
        match self.registers.get(&x) {
            Some(value) => {
                self.registers.insert(x, value - 1);
            }
            None => (),
        }
    }

    fn get_param(&mut self, x: Param) -> i64 {
        match x {
            Register(reg) => *self.registers.get(&reg).unwrap(),
            Constant(con) => con
        }
    }

    fn jnz(&mut self, x: Param, y: Param) {
        let jump = self.get_param(x);
        if jump != 0 {
            let num = self.get_param(y);
            self.ptr += num;

        } else {
            self.ptr += 1;
        }
    }

    fn run(&mut self) {
        while self.ptr.ptr < self.instructions.len() {
            let instruction = self.instructions[self.ptr.ptr];
            match Instruction::from(instruction) {
                Instruction::Mov(x, y) => self.mov(x, y),
                Instruction::Inc(x) => self.inc(x),
                Instruction::Dec(x) => self.dec(x),
                Instruction::Jnz(x, y) => self.jnz(x, y),
                Instruction::None => (),
            }
        }
    }
}

fn simple_assembler(program: Vec<&str>) -> HashMap<String, i64> {
    let mut ass = Assembler::new(program);
    ass.run();
    ass.registers
}

mod tests;
