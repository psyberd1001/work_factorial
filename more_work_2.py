n = int(input('Введите число для вычисления факториала: '))
def factorial(number):
    if number == 1:
        return 1
    factorial_n_minus_1 = factorial(number = number - 1)
    return number * factorial_n_minus_1


def factorial_while(number1):
    number_while = 1
    while number1 > 1:
        number_while = number_while * number1
        number1 -= 1
    return number_while

def factorial_for(number2):
    number_for = 1
    for i in range(1, number2 + 1):
        number_for = number_for * i
    return number_for

print(factorial(n))
print(factorial_while(n))
print(factorial_for(n))


