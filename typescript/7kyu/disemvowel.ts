export class Kata {
    static disemvowel(str: string) {
        return str.split('').map((c) => { return (['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'].indexOf(c) > -1 ? '' : c)}).join('');
    }
}
  