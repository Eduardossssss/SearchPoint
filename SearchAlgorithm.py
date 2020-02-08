from SearchPoint import SearchPoint


def search_algorythm(position, x, y):
    lx = 0      # левая граница по оси x (начинается с нуля, так как это указано в условии задачи)
    rx = w      # правая граница по оси x
    uy = h      # верхняя граница по оси y
    dy = 0      # нижняя граница по оси y (начинается с нуля, так как это указано в условии задачи)

    while position:
        if 'R' in position:
            lx = x                  # если искомая точка находится правее стартовой точки, то сдвигаем левую границу
            x = int((lx+rx)/2)      # берем новую координату x посередине между левой и правой границей
        if 'L' in position:
            rx = x                  # если искомая точка находится левее стартовой точки, то сдвигаем правую границу
            x = int((lx+rx)/2)
        if 'U' in position:
            dy = y                  # если искомая точка находится выше стартовой точки, то сдвигаем нижнюю границу
            y = int((uy+dy)/2)      # берем новую координату y посередине между верхней и нижней границей
        if 'D' in position:
            uy = y                  # если искомая точка находится ниже стартовой точки, то сдвигаем верхнюю границу
            y = int((uy+dy)/2)
        print(x, y)
        position = SP.where_is_point(x, y)
    return print('Искомая точка: {} {}'.format(x, y))

def main():
    search_algorythm(SP.where_is_point(x, y), x, y)


if __name__ == '__main__':
    while True:
        try:
            w = int(input('Введите ширину координатной плоскости: '))
            if w < 0:
                print('Вы ввели значение ширины меньшее нуля. '
                      'Пожалуйста, введите число от 0.')
                continue
        except ValueError:
            print('Вы ввели не число. Пожалуйста, введите число.')
            continue
        while True:
            try:
                h = int(input('Введите высоту координатной плоскости: '))
                if h < 0:
                    print('Вы ввели значение высоты меньшее нуля. '
                          'Пожалуйста, введите число от 0.')
                    continue
            except ValueError:
                print('Вы ввели не число. Пожалуйста, введите число.')
                continue
            break
        while True:
            try:
                x = int(input('Введите координату x для стартовой точки: '))
                if not 0 <= x <= w:
                    print('Координата x стартовой точки выходит за пределы допустимого диапазона. '
                          'Пожалуйста, введите число от 0 до {}.'.format(w))
                    continue
            except ValueError:
                print('Вы ввели не число. Пожалуйста, введите число.')
                continue
            while True:
                try:
                    y = int(input('Введите координату y для стартовой точки: '))
                    if not 0 <= y <= h:
                        print('Координата y стартовой точки выходит за пределы допустимого диапазона. '
                                'Пожалуйста, введите число от 0 до {}.'.format(h))
                        continue
                    else:
                        break
                except ValueError:
                    print('Вы ввели не число. Пожалуйста, введите число.')
            break
        break

    SP = SearchPoint(w, h)
    print('Выходные данные: ')
    main()