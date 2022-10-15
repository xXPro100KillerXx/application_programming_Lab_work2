alph = {}
alphr = {}
alph1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for i in range(0, len(alph1)):
    alph[alph1[i]] = i + 1
    alphr[i + 1] = alph1[i]

print(alph)
print(alphr)

try:  # предотвращение ошибки пользователя, если он введет не цифру
    try:  # предотвращение ошибки пользователя, если он введет не слово
        num = int(input('выберете операцию: зашифровка - 1, расшифровка - 2: '))
        a = 0
        resolt = ''
        tloser = ''
        if num == 1:    #шифрование
            x = str(input(('Введите пердложение, которое нужно зашифровать: ')))
            step = int(input('Введите шаг(число) шифрования: '))

            while step > 33:    #вычисление нужного шага, если шаг больше 33
                step -= 33
            k = step

            for i in range(0, len(x)):
                if x[i] == ' ':
                    resolt += ' '
                else:
                    m = alph[x[i]]
                    if m + k <= 33:
                        resolt += alphr[m + k]
                    else:
                        resolt += alphr[(m + k) - 33]
            print(resolt)

        elif num == 2:  #расшифровка
            x = str(input(('Введите пердложение, которое нужно расшифровать: ')))
            step = int(input('Введите шаг(число) расшифровки: '))

            while step > 33:
                step -= 33
            k = step

            for i in range(0, len(x)):
                if x[i] == ' ':
                    tloser += ' '
                else:
                    m = alph[x[i]]
                    if m - k > 0:
                        tloser += alphr[m - k]
                    else:
                        tloser += alphr[(m - k) + 33]
            print(tloser)
        else:   #если пользователь введет не ту цифру
            print('Введите нужную цифру')
            a = 1

    except KeyError:
        a = 1
        print('Ошибка, Вы ввели не слово')
except ValueError:
    a = 1
    print('Ошибка, Вы ввели не цифру')

while a == 1:
    try:
        try:
            num = int(input('выберете операцию: зашифровка - 1, расшифровка - 2: '))
            a = 0
            resolt = ''
            tloser = ''
            if num == 1:
                x = str(input(('Введите пердложение, которое нужно зашифровать: ')))
                step = int(input('Введите шаг(число) шифрования: '))

                while step > 33:
                    step -= 33
                k = step

                for i in range(0, len(x)):
                    if x[i] == ' ':
                        resolt += ' '
                    else:
                        m = alph[x[i]]
                        if m + k <= 33:
                            resolt += alphr[m + k]
                        else:
                            resolt += alphr[(m + k) - 33]
                print(resolt)

            elif num == 2:
                x = str(input(('Введите пердложение, которое нужно расшифровать: ')))
                step = int(input('Введите шаг(число) расшифровки: '))

                while step > 33:
                    step -= 33
                k = step

                for i in range(0, len(x)):
                    if x[i] == ' ':
                        tloser += ' '
                    else:
                        m = alph[x[i]]
                        if m - k > 0:
                            tloser += alphr[m - k]
                        else:
                            tloser += alphr[(m - k) + 33]
                print(tloser)

        except KeyError:
            a = 1
            print('Ошибка, Вы ввели не слово')
    except ValueError:
        a = 1
        print('Ошибка, Вы ввели не цифру')
