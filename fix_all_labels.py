#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1a: Cafelat Robot — remove duplicate label (L213)
# Currently L212: <div class="pick-overall"> (wrong, should be pick-best)
# L213: <div class="pick-best"> (from cafelat)
# L212 was set by fix_order, need to revert
old = '<h4>Cafelat Robot Espresso Maker<span class="price-range">$$$</span></h4>\n<div class="stars">'
new = '<h4>Cafelat Robot Espresso Maker<span class="price-range">$$$</span></h4>\n<div class="pick-best">#1 Best Seller</div>\n<div class="stars">'
content = content.replace(old, new, 1)

# Now remove the duplicate pick-best that follows
# Pattern: pick-overall\n<pick-best>  -> pick-best only
content = content.replace(
    '<div class="pick-overall">\U0001F3C6 Overall Pick</div>\n<div class="pick-best">#1 Best Seller</div>',
    '<div class="pick-best">#1 Best Seller</div>',
    1
)

# Fix 2: Breville Barista Express -> Overall Pick
content = content.replace(
    '<h4>Breville Barista Express Impress<span class="price-range">$$$$</span></h4>\n<div class="pick-guide">\u2705 Great Value</div>',
    '<h4>Breville Barista Express Impress<span class="price-range">$$$$</span></h4>\n<div class="pick-overall">\U0001F3C6 Overall Pick</div>',
    1
)

# Fix 3: Fellow Opus -> Overall Pick
content = content.replace(
    '<h4>Fellow Opus Conical Burr Grinder<span class="price-range">$$$</span></h4>\n<div class="pick-guide">\u2705 Great Value</div>',
    '<h4>Fellow Opus Conical Burr Grinder<span class="price-range">$$$</span></h4>\n<div class="pick-overall">\U0001F3C6 Overall Pick</div>',
    1
)

# Fix 4: Remove Barista's Pick from Nespresso line (should be Great Value only)
# L232-233: pick-guide\npick-recommended -> pick-guide only
content = content.replace(
    '<h4>Nespresso Vertuo Next Deluxe<span class="price-range">$$</span></h4>\n<div class="pick-guide">\u2705 Great Value</div>\n<div class="pick-recommended">\U0001F525 Barista\u2019s Pick',
    '<h4>Nespresso Vertuo Next Deluxe<span class="price-range">$$</span></h4>\n<div class="pick-guide">\u2705 Great Value</div>',
    1
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
