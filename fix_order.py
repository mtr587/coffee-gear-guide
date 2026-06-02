#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix 1: Line 222 (Nespresso Vertuo) - missing closing div tag
# Line 223 currently: <div class="pick-guide">&#9989; Great Value
line_idx = 222  # 0-indexed
lines[line_idx] = '    <div class="pick-guide">\u2705 Great Value</div>\n'

# Fix 2: Line 212 is actually Breville (not Cafelat)
# Line 212: #1 Best Seller -> should be Overall Pick
# Breville is the 2nd card in Espresso Machines
lines[211] = '    <div class="pick-overall">\U0001F3C6 Overall Pick</div>\n'

# Fix 3: Line 232 (Nespresso) - currently Barista's Pick -> should be Great Value
lines[231] = '    <div class="pick-guide">\u2705 Great Value</div>\n'

# Verify
for i in [211, 212, 221, 222, 231, 232]:
    safe = lines[i].rstrip().encode('ascii', errors='xmlcharrefreplace').decode('ascii')
    print(f'Line {i+1:3d}: {safe}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done')
