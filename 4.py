from math import e, pi, cos, sin, sqrt, log


def template_for_task_1(x):
    for n in range(10, 15):
        summ = 0
        for k in range(1, n + 1):
            summ += cos(x * k)
        result = pow(e, x) + summ
        print(f'For_task_1 {x=} {n=} {result=}')


def template_for_task_2(x):
    for n in range(10, 15):
        summ = 0
        for k in range(1, n + 1):
            summ += pow(sin((k - 1) / (k + 1)), 2) + pow(e, sqrt(x / k))
        result = pi / (pow(x, 1 / 3) + 3 / (x + 5)) * summ
        print(f'For_task_2 {x=} {n=} {result=}')


def template_for_task_3(x):
    for n in range(10, 15):
        summ = 0
        for k in range(1, n + 1):
            summ += (1 + (k + 1) / n) / (pow(e, k) * sqrt(pow(x, k - 1)) + log(x))
        result = sqrt(pow(sin(x / n), 3)) * summ
        print(f'For_task_3 {x=} {n=} {result=}')


def template_for_task_4(x):
    for n in range(10, 15):
        summ = 0
        for k in range(1, n + 1):
            summ += sqrt((pow(pow(x, k + 1), 1 / k)) + (pow(pow(e, k - 2 / 3), 1 / k)) / (1 + log(x)))
        result = (sin((pi * n) / (x + 3))) * summ
        print(f'For_task_4 {x=} {n=} {result=}')

def template_for_task_5(x):
    for n in range(10, 15):
        summ = 0
        for k in range(1, n + 1):
            summ += pow(abs(x+k), 2) * cos(k + pow(sin(x), 1/5) / (k * x))
        result = 1 / 45 * sqrt(pow(3, x + n)) * summ
        print(f'For_task_5 {x=} {n=} {result=}')

def template_for_task(x=0.6, step=0.25):
    while x <= 1.1:
        template_for_task_1(x)
        template_for_task_2(x)
        template_for_task_3(x)
        template_for_task_4(x)
        template_for_task_5(x)
        x += step


template_for_task()
