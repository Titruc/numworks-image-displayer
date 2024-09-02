with open("compresse.txt") as r:
    content = r.read()

result = ''
for n in content:
    if n != ' ':
        result+=n
with open('coucou.txt', 'w') as f:
    f.write(result)