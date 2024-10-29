r = 0
n = 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

while True:
    n = int(input('Введи целое число: '))
    if n == 0:
        break
    m = sum_digits(n)
    if m > r:
        r = m
        q = n
print(f'Число с максимальной суммой цифр {q} Сумма цифр этого числа {r}')