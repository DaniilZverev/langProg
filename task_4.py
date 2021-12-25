currentValue = ''
values = []
currentIndex = 0

def changeIndex(oper = 'null'):
    global currentIndex
    if oper == '-':
        currentIndex -= 1
    elif oper == '+':
        currentIndex += 1
    else:
        print('Error')

while 0 < 1:
    code = input()
    for operator in code.split():
        if operator == "oom":
            inputValue = int(input("ввод значения в текущую ячейку: "))
            if  currentIndex < len(values):
                values.pop(currentIndex)
            values.insert(currentIndex ,inputValue)
            currentValue = values[currentIndex]
        if operator == "moO":
            changeIndex('+')
            if currentIndex < len(values):
                currentValue = values[currentIndex]
            else:
                values.insert(currentIndex, 0)
                currentValue = values[currentIndex]
        if operator == "OOM":
            if currentIndex < len(values):
                decode = chr(int(values[currentIndex]))
                print(decode, end='')
            else:
                print('Error: Ячейка пустая')
        if operator == "mOo":
            changeIndex('-')
            if currentIndex < len(values):
                values[currentIndex]
                currentValue = values[currentIndex]
            else:
                changeIndex('+')
        if operator == "MoO":
            if len(values) == 0:
                values.insert(0, 0)
            if currentIndex < len(values):
                values[currentIndex] += 1
            else:
                print('Error: Ячейка пустая')
        elif operator == "MOo":
            if currentIndex < len(values):
                values[currentIndex] -= 1
            else:
                print('Error: Ячейка пустая')
        if operator == "Moo":
            if values[currentIndex] == 0:
                inputValue = int(input("ввод значения в текущую ячейку: "))
                values.pop(currentIndex)
                values.insert(currentIndex, inputValue)
                currentValue = values[currentIndex]
            else:
                decode = chr(int(values[currentIndex]))
                print(decode, end='')
        if operator == "OOO":
            if currentIndex < len(values):
                values[currentIndex] = 0
            else:
                print('Error: Ячейка пустая')



