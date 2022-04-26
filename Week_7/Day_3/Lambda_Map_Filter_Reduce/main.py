names = ['John', 'Hillary', 'Spencer', 'Ruth', 'Jo']

to_hello = map((lambda x: f"Hello, {x}"),
               (filter(lambda i: len(i) <= 4, names)))

for x in to_hello:
    print(x)
