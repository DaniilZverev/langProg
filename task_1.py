#                Task 1
#
# firstNumber = int(input('Введите первое число - '))
# secondNumber = int(input('Введите второе число -'))
# operator = input('Введите оператор - ')
# result = 0
#
# if operator:
#     if operator == '+':
#         result = (firstNumber + secondNumber)
#     elif operator == '-':
#         result = (firstNumber - secondNumber)
#     elif operator == '*':
#         result = (firstNumber * secondNumber)
#     elif operator == '/':
#         if (secondNumber != 0):
#             result = (firstNumber / secondNumber)
#         else:
#             print('Делить на 0 нельзя')
#     else:
#         print('Введен не верный оператор')
#
# print(result)


#                Task 2
# word = input('Введите слово на англ языке - ')
# vowels = 0
# consonants = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Гласных %i\nСогласных %i" % (vowels, consonants))


#                Task 3
# list = open("words.txt", "r").read().split()
# wm = ""
# lm = 0
# for w in list:
#     l = len(w)
#     if l > lm:
#        wm = w
#        lm = l
#        print(lm)
# print("Самое длинное слово:")
# print(wm)




