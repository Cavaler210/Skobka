inp = input()
spisok = []

for i in inp:

    if i == '(':
        spisok.append(i)
    elif i == ')':
        free = spisok.pop()
        if free == '(' and i ==')':
            continue
        else:
            break



    if i == '{':
        spisok.append(i)
    elif i == '}':
        free = spisok.pop()
        if free == '{' and i == '}':
            continue
        else:
            break

    if i == '[':
        spisok.append(i)
    elif i == ']':
        free = spisok.pop()
        if free == '[' and i == ']':
            continue
        else:
            break



if len(spisok) == 0:
    print('YES')
else:
    print('no')

print(spisok)
