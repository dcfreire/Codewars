use std::collections::HashSet;

fn unique<'a, I>(iter: I) -> bool where
I: Iterator<Item = &'a u8>,
{
    let mut uniq = HashSet::new();
    iter.into_iter().all(|x| uniq.insert(x) && x != &0)
}

fn validate_rows(sudoku: &[[u8; 9]; 9]) -> bool {
    let mut valid = true;
    for row in sudoku {
        valid = valid && unique(row.iter());
    }
    valid
}

fn validate_columns(sudoku: &[[u8; 9]; 9]) -> bool {
    let mut valid = true;
    for i in 0..9 {
        let column = sudoku.map(|row| row[i]);
        valid = valid && unique(column.iter());
    }
    valid
}

fn validate_blocks(sudoku: &[[u8; 9]; 9]) -> bool {
    let mut valid = true;
    for i in 0..3 {
        for j in 0..3 {
            let block = sudoku[(i*3)..(i*3)+3].iter().map(|row| &row[(j*3)..(j*3)+3]).flatten();
            valid = valid && unique(block);
        }
    }
    valid
}

fn valid_solution(sudoku: &[[u8; 9]; 9]) -> bool {
    validate_blocks(sudoku) && validate_columns(sudoku) && validate_rows(sudoku)
}


mod tests;
