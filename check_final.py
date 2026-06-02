#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('All product label lines:')
for i, line in enumerate(lines, 1):
    line_s = line.strip()
    if line_s.startswith('<div class="pick-'):
        safe = line_s.encode('ascii', errors='xmlcharrefreplace').decode('ascii')
        print(f'  Line {i:3d}: {safe}')
