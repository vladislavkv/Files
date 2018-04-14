myFile = open('text.txt', 'r')

countLines = 0
countSpaces = 0

for line in myFile:
    countLines += 1
    countSpaces += line.count(' ')

print('Кол-во пробелов в файле: ', countSpaces)
print('Кол-во строк в файле: ', countLines)

myFile.close
