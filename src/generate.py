from slidegen import Generator
from slidegen import DataProvider

g = Generator(DataProvider())

print('''
title: Pitching like a boss
controls: false
output: slide.html

---
''')
print(g.cover())
print(g.content())
for i in range(4):
    print(g.content())
print(g.full_image())
print('''
# Q & A
''')
