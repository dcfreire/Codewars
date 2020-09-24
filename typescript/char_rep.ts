//Does this still count as a one liner? lel
export function longestRepetition(text: string): [string, number] {
    return (text + '~').split('').reduce((acc, v) => {let s: string = acc[1][0] as string;let seq: string = acc[0] as string;if (!s.length && v === '~') { return ['', ['', 0]]}if (!s.length) {return [acc[0] + v, [v, 1]];}switch (seq.charAt(0)) {case v: {return [acc[0] + v, [s, acc[1][1]]];}default: {return seq.length > acc[1][1] ? [v, [seq.charAt(0), seq.length]] : [v, [s, acc[1][1]]];}}}, ['', ['', 0]])[1] as [string, number];
}
