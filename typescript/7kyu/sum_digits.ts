export function sumDigits(number: number): number {
    return Math.abs(number).toString().split('').map(x=>+x).reduce(function(a, b){return a + b})
}
console.log(sumDigits(15))