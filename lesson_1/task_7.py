# 7. По введенным пользователем длинам трех отрезков определить,можно ли составить из этих отрезков треугольник. Если да,
# определить, будет ли треугольник разносторонним, равнобедренным или равносторонним.

a = float(input('Введите значение 1-ой стороны: '))
b = float(input('Введите значение 2-ой стороны: '))
c = float(input('Введите значение 3-ей стороны: '))

if a+b > c and b+c > a and c+a > b:
    if a == b == c:
        print('Получился равносторонний треугольник.')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный.')
    else:
        print("Треугольник разносторонний")
else:
    print('Треугольника с такими сторонами не существует!')
