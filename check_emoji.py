with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in [211, 221, 231, 253, 263, 273]:
    line = lines[i]
    escaped = line.rstrip().encode("ascii", errors="xmlcharrefreplace").decode("ascii")
    print(f"Line {i+1}: {escaped}")
