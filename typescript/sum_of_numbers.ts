export function getSum(a: number, b: number): number{
  return Array<number>(Math.abs(a - b) + 1).fill(0).reduce((acc, _value, i)=>{return a < b ? acc + a + i : acc + b + i }, 0)
}
