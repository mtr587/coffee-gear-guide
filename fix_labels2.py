#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add .pick-recommended CSS (already added by fix_labels.py, let's just keep the existing lines)
# CSS was already successfully inserted

# 2. Fellow Stagg: line 316  <div class="pick-guide">✅ Great Value</div>
stagg_old = '<div class="pick-guide">\u2705 Great Value</div>\n<a class="btn" href="https://www.amazon.com/dp/B0DWFPXN48?tag=jamesma06-20" target="_blank" rel="nofollow sponsored">Check Price on Amazon</a>\n</div>\n</div>\n</div>\n</div>\n\n<!-- ===== MUGS & GLASSWARE ===== -->'
stagg_new = '<div class="pick-recommended">\U0001F525 Barista\u2019s Pick</div>\n<a class="btn" href="https://www.amazon.com/dp/B0DWFPXN48?tag=jamesma06-20" target="_blank" rel="nofollow sponsored">Check Price on Amazon</a>\n</div>\n</div>\n</div>\n</div>\n\n<!-- ===== MUGS & GLASSWARE ===== -->'

if stagg_old in content:
    content = content.replace(stagg_old, stagg_new, 1)
    print('Stagg: replaced')
else:
    print('Stagg: NOT FOUND - checking encoding')
    # Try char by char
    idx = content.find('B0DWFPXN48')
    if idx > 0:
        print(f'  Found at position {idx}')
        snippet = content[idx-200:idx]
        # Find pick-guide in snippet
        pg_idx = snippet.rfind('pick-guide')
        if pg_idx > 0:
            context = snippet[pg_idx-10:pg_idx+80]
            print(f'  Context: {context.encode("ascii", errors="replace").decode("ascii")}')

# 3. AeroPress: line 307  <div class="pick-overall">🏆 Overall Pick</div>
aeropress_old = '<div class="pick-overall">\U0001F3C6 Overall Pick</div>'
aeropress_new = '<div class="pick-guide">\u2705 Great Value</div>'

if aeropress_old in content:
    content = content.replace(aeropress_old, aeropress_new, 1)
    print('AeroPress: replaced')
else:
    print('AeroPress: NOT FOUND')
    # Debug: show what characters are around
    idx = content.find('B0BYKKS1NV')
    if idx > 0:
        before = content[idx-200:idx]
        print(f'  Last 200 chars before ASIN: {before[-100:].encode("ascii", errors="replace").decode("ascii")}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
