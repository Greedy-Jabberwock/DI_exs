border = '\n-------------------\n'
# with open('names.txt', 'r+') as f:
#     print(f.read(), end=border)
#     f.seek(0)
#     print(f.readline(5), end=border)
#     f.seek(0)
#     print(f.read(5), end=border)
#     f.seek(0)
#     all_lines = [x.split()[0] for x in f.readlines()]
#     print(all_lines, end=border)
#     names_set = set(all_lines)
#     for name in names_set:
#         print(f'{name} counts {all_lines.count(name)} times.', end=border)
#     f.write('\nVitalii')

with open('names.txt', 'a+') as f:
    f.seek(0)
    lines = f.readlines()
    for index, line in enumerate(lines):
        if line.strip() == 'Luke':
            lines[index] = 'Luke Skywalker\n'
    with open('names.txt', 'w') as fw:
        fw.seek(0)
        fw.writelines(lines)
