"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

import sys


text = sys.stdin.read().lower()
for c in text:
    if c in (',.;:!/?()-—–»«'):
        text = text.replace(c, '')
res = {}
for i in text.split():
    res[i] = res.get(i, 0) + 1
for word in sorted(res.items(), key=lambda x: -x[1])[:10]:
    print(word[0], end=' ')
