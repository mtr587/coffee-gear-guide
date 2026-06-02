#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show first occurrence of product labels and their surrounding context
for i, line in enumerate(lines):
    if 'class="pick-' in line:
        # show a few lines around it
        start = max(0, i-2)
        end = min(len(lines), i+3)
        print(f'--- Around line {i+1} ---')
        for j in range(start, end):
            safe = lines[j].rstrip().encode('ascii', errors='xmlcharrefreplace').decode('ascii')
            marker = ' >>>' if j == i else ''
            print(f'  L{j+1:4d}{marker}: {safe[:100]}')
        print()
