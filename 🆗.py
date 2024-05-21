"Anyone here?"
# Anyone here?
a = [0, ]
f = lambda x: round(((x + 1) * 5) / 4)
for j in range(5):
    for i in a:
        try: a.append(f(f(i) - j))
        except: a.append(0)
print(a)
