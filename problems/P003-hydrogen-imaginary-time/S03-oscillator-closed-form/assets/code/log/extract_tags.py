# extract_tags.py -- list every provenance tag in final.md outside fenced code, with the
# section it sits in, the nearest equation number on the same or preceding lines, and a snippet.
# Run: python3 -I extract_tags.py S03/final/final.md
import re, sys
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
sec = ''; infence = False; lasteq = ''
for n, l in enumerate(lines, 1):
    if l.startswith('```'):
        infence = not infence; continue
    if infence: continue
    if l.startswith('#'): sec = l.lstrip('#').strip()[:40]
    m = re.findall(r'\\tag\{([^}]+)\}', l)
    if m: lasteq = m[-1]
    for t in re.finditer(r'`\[(D|S|V|R|A\d?|N|\?)\]`', l):
        snip = re.sub(r'\s+', ' ', l[t.end():t.end()+90]).strip()
        print(f"{n}\t{sec}\t{lasteq}\t{t.group(1)}\t{snip}")
