#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 307 (0-indexed 306) currently has: pick-overall with the trophy emoji
# Replace it with Great Value
line307 = lines[306]
print(f'Before (line 307): {line307[:80].encode("ascii", errors="xmlcharrefreplace").decode("ascii")}')

# Replace the content between > and <
lines[306] = '    <div class="pick-guide">\u2705 Great Value</div>\n'

print(f'After (line 307): {lines[306][:80].encode("ascii", errors="xmlcharrefreplace").decode("ascii")}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done')
