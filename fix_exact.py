#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# === FIXES ===

# Cafelat Robot: remove L213 duplicate label (stray pick-best)
lines[212] = ''  # blank out the duplicate line

# Breville (line 223): Great Value -> Overall Pick  
lines[222] = '    <div class="pick-overall">\U0001F3C6 Overall Pick</div>\n'

# Nespresso (line 233): remove Barista's Pick (stray from earlier replacement)
lines[232] = ''  # blank out

# Fellow Opus (line 265): Great Value -> Overall Pick
lines[264] = '    <div class="pick-overall">\U0001F3C6 Overall Pick</div>\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done')
