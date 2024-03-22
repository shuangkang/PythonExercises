# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')
#
# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)
#
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')
import os
import sys
import time

li = [1, 3, 5, 7, 100]

# for index, elem in enumerate(li):
#     print(index, elem)
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)

f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间



def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

for i in fib(10):
    print(i)


def main():
    content = 'kmhssssssbbbbb.........................'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]



def get_big_two(l):
    return sorted(l, reverse=True)[:2]
print(get_big_two(li))

if __name__ == '__main__':
    main()