#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

blocks = content.split('<div class="category-block">')
for i, block in enumerate(blocks):
    if i == 0:
        continue
    cat_match = re.search(r'<h3>(.*?)</h3>', block)
    cat = cat_match.group(1) if cat_match else '?'
    
    products = re.findall(r'<h4>(.*?)<span class="price-range">', block)
    labels = re.findall(r'<div class="(pick-best|pick-overall|pick-guide)">(.*?)</div>', block)
    
    print(f"\n--- {cat} ---")
    for p, (cls, label) in zip(products, labels):
        # remove HTML entities
        p_clean = p.replace('&amp;', '&').replace('&nbsp;', ' ')[:45]
        print(f"  {p_clean:45s} | {cls:15s} | {label.encode('ascii', errors='xmlcharrefreplace').decode('ascii')}")
