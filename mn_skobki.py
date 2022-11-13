


def skob(inp):
    spisok = [] #задаем пустой список

    psp = True  # наша последовательность верная

    for i in inp:
        if i in '({[':
            spisok.append(i)
        elif i in ')}]':
            if not spisok:  # из пустого списка нельзя убрать скобку
                psp = False
                break
            free = spisok.pop()
            if free == '(' and i == ')': # если совпадает скобка в стеке и элемент, то они вылетают
                continue
            if free == '[' and i == ']':
                continue
            if free == '{' and i == '}':
                continue
            psp = False
            break
    if psp and len(spisok) == 0:
        answer = True
    else:
        answer = False
    return answer
#print(skob())

