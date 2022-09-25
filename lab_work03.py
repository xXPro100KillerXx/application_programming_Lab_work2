alph = {}
alphr = {}
alph1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for i in range(0, len(alph1)):
    alph[alph1[i]] = i + 1
    alphr[i + 1] = alph1[i]

print(alph)
print(alphr)


x = str(input(('Введите слово, которое нужно зашифровать: ')))
step = int(input('Введите шаг(число) шифрования: '))
resolt = ''
tloser = ''

for i in range(0, len(x)):
    if x[i] == ' ':
        resolt += ' '
    else:
        m = alph[x[i]]
        if m + step <= 33:
            resolt += alphr[m + step]
        else:
            resolt += alphr[(m + step) - 33]



for i in range(0, len(resolt)):
    if x[i] == ' ':
        tloser += ' '
    else:
        m = alph[resolt[i]]
        if m - step > 0:
            tloser += alphr[m - step]
        else:
            tloser += alphr[(m - step) + 33]

print(resolt)
print(tloser)
