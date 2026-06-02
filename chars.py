#!/usr/bin/env python3
import unicodedata

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

counts = {}
for i, ch in enumerate(text):
    cp = ord(ch)
    if cp > 127:
        if cp not in counts:
            name = unicodedata.name(ch, '?')
            counts[cp] = {'char': ch, 'name': name, 'count': 0, 'sample_pos': i}
        counts[cp]['count'] += 1

for cp in sorted(counts.keys()):
    info = counts[cp]
    ctx = text[max(0, info['sample_pos']-15):info['sample_pos']+20]
    encoded = ctx.encode('ascii', errors='xmlcharrefreplace').decode('ascii')
    print(f'U+{cp:04X} ({info["name"]}): {info["count"]}x')
    print(f'  Context: ...{encoded}...')
    print()
