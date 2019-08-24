import re


def top_3_words(text):
    print(text)

    text = text.lower()
    words = re.findall(r'[^\W_]+(?:[\'][^\W_]+)*', text)
    wc = {}
    for w in words:
        if w in wc.keys():
            wc[w] += 1
        else:
            wc[w] = 1
    return [i[0] for i in sorted(wc.items(), key=lambda x: x[1], reverse=True)[:3]]


top_3_words("BfAS. tEK'?;::tDDxK;/,;KemKMa?/ !PcbwptKRoz.zeZgEIZl_?;::KemKMa. __:tDDxK;PcbwptKRoz/;/;_tDDxK,: zeZgEIZl? tEK'!- PcbwptKRoz:-tEK'?PcbwptKRoz!:,; tEK';PcbwptKRoz,?/:_BfAS?!_?.tDDxK:._/tDDxK;/KemKMa!_:-;BfAS,;!PcbwptKRoz/;zeZgEIZl  ;?_KemKMa!,BfAS,:KemKMa-tEK'/KemKMa?.;--PcbwptKRoz!/-PcbwptKRoz?PcbwptKRoz/zeZgEIZl-!:/_PcbwptKRoz:.;!BfAS/ KemKMa-..tEK',KemKMa!.,PcbwptKRoz:;:/ KemKMa;_KemKMa;tEK'//!;zeZgEIZl?/.;zeZgEIZl  KemKMa-/tDDxK;:/:-PcbwptKRoz_BfAS !_tEK'!,.,-KemKMa?-,;KemKMa./::KemKMa?_PcbwptKRoz_ tEK' ,KemKMa/-tDDxK:?-:tEK'::;KemKMa tEK' . !.tEK'!BfAS!!/!tEK';tDDxK,_:tEK'?  :PcbwptKRoz!.::tDDxK?tEK'?zeZgEIZl--!?:BfAS -:tDDxK::tEK'!! PcbwptKRoz-!.?KemKMa.tEK':,,KemKMa:- tDDxK_-KemKMa:,;:PcbwptKRoz:?!!tEK'?/;/")
