# zadanie 2.1

import re

file = open('py1.2', 'r')
data = file.readlines()
file.close()

dict = {}
for line in data:
    matchObj = (re.match( r'^\d*. (.*) has (.*) and .*is (\d*)', line))
    if matchObj:
        name = matchObj.group(1)
        eye = matchObj.group(2)
        height = matchObj.group(3)
    else:
        print('Linie nie odczytane: ', line)

    dict[name] = {'height': int(height), 'eyes': eye}

# print(dict)


# zadanie 2.4
uniqEyeColor = {}
langPL = {'yellow': 'żółty',
          'black': 'czarny',
          'blue': 'niebieski',
          'orange': 'pomarańczowy',
          'green, yellow': 'zielono-żółty',
          'red': 'czerwony',
          'brown': 'brązowy',
          'unknown': 'niezidentyfikowany',
          'gold': 'złoty',
          'blue-gray': 'niebiesko-szary',
          'pink': 'różowy',
          'hazel': 'piwny',
          'red, blue': 'czerwono-niebieski', }

for item in dict:
    eyeColor = dict[item]['eyes']
    height = dict[item]['height']
    if eyeColor not in uniqEyeColor:
        uniqEyeColor[eyeColor] = [height]
    else:
        uniqEyeColor[eyeColor].append(height)

for i in langPL:
    if i in uniqEyeColor:
        uniqEyeColor[langPL[i]] = uniqEyeColor.pop(i)


for color in uniqEyeColor:
    everageHeight = sum(uniqEyeColor[color])  / len(uniqEyeColor[color])
    print('Średni wzrost osób z kolorem oczu ' + color + ' wynosi ' + '%.2f' % everageHeight + 'cm')





"""
# zadanie 2.3
uniqEyeColor = {}
for item in dict:
    eyeColor = dict[item]['eyes']
    height = dict[item]['height']
    if eyeColor not in uniqEyeColor:
        uniqEyeColor[eyeColor] = [height]
    else:
        uniqEyeColor[eyeColor].append(height)

# print(uniqEyeColor)

for item in uniqEyeColor:
    everageHeight = sum(uniqEyeColor[item])  / len(uniqEyeColor[item])
 #   print(everageHeight)
    print('Średni wzrost osób z kolorem oczu ' + item + ' wynosi ' + '%.2f' % everageHeight)

"""




"""
# zadanie 2.2

highPersons = open('heighPersons.txt', 'w')
lowPersons = open('lowPersons.txt', 'w')

for item in dict:
    if int(dict[item]['height']) > 200:
        highPersons.write(item + '\n')
    else:
        lowPersons.write(item + '\n')


highPersons.close()
lowPersons.close()

"""




