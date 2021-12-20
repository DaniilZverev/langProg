# prefix = input("Введите prefix ")

prefix = "+ - 13 4 55"
print(prefix)
prefixList = prefix.split()

operList = list()
result = ""

for i in prefixList:
    if(i.isdigit()):
        result += i + ' '
        if(len(operList)):
            result += operList[0] + ' '
            operList.pop(0)
    elif (i == "+"):
        operList.append(i)
    elif(i == "-"):
        operList.append(i)
    elif (i == "*"):
        operList.append(i)

print(result)