from timeit import timeit

# 单条语句
timeit('[i for i in range(5)]',number=100)


# 函数
def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=1000)
print(t)