#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('<div class="pick-overall">\u00bf\u00bf Overall Pick</div>', '<div class="pick-overall">\U0001F3C6 Overall Pick</div>')
content = content.replace('<div class="pick-guide">\u00bf Great Value</div>', '<div class="pick-guide">\u2705 Great Value</div>')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
