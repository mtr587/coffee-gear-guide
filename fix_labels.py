#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for .pick-recommended (Barista's Pick - premium label)
css_add = '\n.pick-recommended{font-size:.76rem;color:#fff;background:var(--star);padding:6px 10px;border-radius:6px;margin-bottom:10px;border-left:none;line-height:1.4;font-weight:700}'

# Insert after .pick-overall CSS rule
css_pattern = r'(\.pick-overall\{[^}]+\})'
content = re.sub(css_pattern, r'\1' + css_add, content)

# 2. Fellow Stagg EKG ($170+) -> Barista's Pick (premium recommendation)
# Find by ASIN B0DWFPXN48
idx = content.find('B0DWFPXN48')
if idx > 0:
    before = content[:idx]
    last_guide = before.rfind('pick-guide')
    if last_guide > 0:
        div_end = before.index('</div>', last_guide)
        full_tag = before[last_guide:div_end+6]
        # Find what's inside
        inner = before[last_guide:div_end+6]
        content = content.replace(inner, 'pick-recommended">\U0001F525 Barista\u2019s Pick', 1)
        print('Stagg -> Barista\'s Pick')
else:
    print('ERROR: Stagg ASIN not found')

# 3. AeroPress ($35, 4.8*, 90K reviews) is the real Great Value
idx = content.find('B0BYKKS1NV')
if idx > 0:
    before = content[:idx]
    last_overall = before.rfind('pick-overall')
    if last_overall > 0:
        # Find the full tag
        tag_start = before.rfind('pick-overall', 0, last_overall)
        div_end = before.index('</div>', tag_start)
        full_tag = before[tag_start:div_end+6]
        content = content.replace(full_tag, 'pick-guide">\u2705 Great Value', 1)
        print('AeroPress -> Great Value')
    else:
        print('ERROR: AeroPress overall pick not found')
else:
    print('ERROR: AeroPress ASIN not found')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
