# Hézio

import re

txt = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."

# Todos que começam com a tem três caracteres quaisquer no meio e depois r
x = re.findall("a...r", txt)
print(x)