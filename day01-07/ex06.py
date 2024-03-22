def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# for i in range(20):
#     print(i + 1, ':', fibonacci(i))


def yinzi(n):
    lst= []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    return sum(lst)


for i in range(1000):
    if yinzi(i) == i:
        print(i)

import test
test.bar()

def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100