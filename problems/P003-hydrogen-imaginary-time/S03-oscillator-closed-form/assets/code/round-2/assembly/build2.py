# build.py -- assemble answer-2.md from template2.md, inserting code and outputs verbatim.
import re, pathlib
t = pathlib.Path('template2.md').read_text()

def code(m):
    return pathlib.Path(m.group(1)).read_text().rstrip('\n')

def out(m):
    body = pathlib.Path(m.group(1)).read_text().rstrip('\n')
    return "```\n" + body + "\n```"

def raw(m):
    return pathlib.Path(m.group(1)).read_text().rstrip('\n')

t = re.sub(r'\{\{CODE:([^}]+)\}\}', code, t)
t = re.sub(r'\{\{OUT:([^}]+)\}\}', out, t)
t = re.sub(r'\{\{RAW:([^}]+)\}\}', raw, t)
assert '{{' not in t
pathlib.Path('answer-2.md').write_text(t)
print("written", len(t), "chars")
