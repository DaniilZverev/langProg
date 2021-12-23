# prefix = input("Введите prefix ")

# prefix = "/ + 3 10 * + 2 4 - 3 5"
# prefix = "+ + 10 20 30"
prefix = "+ 2 * 2 - 2 1"
# prefix = "+ - 13 4 55"
# prefix = "- - 2 1"
print(prefix)
prefixString = prefix.split()

operatorList = list()
numbersList = list()
resultList = list()

result = ''

def toInfix(param = ''):
    if param == 'merge':
        result = '(' + resultList[len(resultList) - 1] + ' ' + operatorList[0] + ' ' + resultList[len(resultList) - 2] + ')'
        resultList.clear()
        operatorList.pop(0)
        return resultList.append(result)
    elif param == 'last':
        result = resultList[0] + ' ' + operatorList[0] + ' ' + numbersList[0]
        operatorList.clear()
        numbersList.clear()
        resultList.clear()
        return resultList.append(result)
    else :
        if len(numbersList) == 3:
            result = '(' + numbersList[0] + ' ' + operatorList[0] + ' ' + numbersList[1] + ')'
            numbersList.pop(0)
            numbersList.pop(0)
            resultList.clear()
            operatorList.pop(0)
            return resultList.append(result)
        elif len(numbersList) >= 2 and len(operatorList) >= 1:
            result = '(' + numbersList[len(numbersList) - 2] + ' ' + operatorList[0] + ' ' + numbersList[len(numbersList) - 1] + ')'
            numbersList.pop(len(numbersList) - 1)
            numbersList.pop(len(numbersList) - 1)
            operatorList.pop(0)
            return resultList.append(result)
        else:
            result = resultList[len(resultList) - 1] + ' ' + operatorList[0] + ' ' + resultList[len(resultList) - 2]
            resultList.clear()
            operatorList.pop(0)
            return resultList.append(result)




for value in reversed(prefixString):
    if value == '/' or value == '*' or value == '-' or value == '+':
        operatorList.insert(0,value)
        if len(resultList) >= 2 and len(operatorList) >= 1:
            toInfix('merge')
        elif len(numbersList) >= 2 and len(operatorList) >= 1:
            toInfix()
    elif value.isdigit():
        numbersList.insert(0, value)
        if len(numbersList) >= 2 and len(operatorList) >= 1 and prefixString[0].isdigit() != 1:
            toInfix()
    else:
        print('Вы ввели не верное значение')

if len(numbersList) != 0 and len(operatorList) != 0:
    toInfix('last')
elif len(numbersList) == 0 and len(operatorList) != 0:
    result = operatorList[0] + ' ' + resultList[0]
    resultList.clear()
    operatorList.clear()
    resultList.append(result)

correctResult = resultList[0].split()

# if correctResult[0] == '(' and correctResult[1] == '(' and correctResult[len(correctResult) - 2] == ')' and correctResult[len(correctResult) - 1] == ')':
#     correctResult.pop(0)
#     correctResult.pop(len(correctResult) - 1)
#     print(correctResult)
# else:
print(resultList[0])