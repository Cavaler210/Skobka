# print("Введите скобочную последовательность из '(' и ')' ")

def skobka(inp):
    x = 0
    for i in inp:
        if i == '(':
            x += 1

        elif i == ')':
            x -= 1
            if x == - 1:
                break

    if x == 0:
        answer = True
    elif x != 0:
        answer = False
    return answer
#print(skobka())
