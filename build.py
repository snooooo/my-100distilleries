import json
import os

dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir, 'data_raw.json'), 'r') as f:
    data = f.read().strip()

with open(os.path.join(dir, 'template.html'), 'r') as f:
    html = f.read()

html = html.replace('__DATA_PLACEHOLDER__', data)

with open(os.path.join(dir, 'index.html'), 'w') as f:
    f.write(html)

print(f'Built index.html ({len(html)} bytes)')
