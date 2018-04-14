myFile = open('test.virus', 'a', encoding = 'utf-8')

lastName = input('Введите фамилию: ')
firstName = input('Введите имя: ')
middleName = input('Введите отчество: ')

fio = lastName + ' ' + firstName + ' ' + middleName + '\n'

myFile.write(fio)
myFile.close()
