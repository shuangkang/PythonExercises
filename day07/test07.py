s1 = '郭恩腾'
s2 = '是一个'
#可以起到换行的作用
s3 = s1+s2+"""
勾八
"""
print(s1,s2,s3,end='')

s1 = 'hello' * 3
print(s1)
#跳过两个下标
print(s1[2:])
#跳过两个下标获取到第五个
print(s1[2:5])
#获取字符数
print((len)(s1))
#首字母大写
print(s1.capitalize())
#每个首字母大写
print(s1.title())
#全部大写
print(s1.upper())
#查找字符下标
print(s1.find("h"))
#是否以该字符开头
print(s1.startswith("he"))

# print(s1.rjust(50,'   '))
#是否以数字构成
print(s1.isdigit())
#是否以字符构成
print(s1.isalpha())
#获得去掉左右空格之后的拷贝
s3 = "  勾八  "
print(s3.strip())

#使用字符串的方式
a,b = 1,4
c = print('{0}*{1} = {2}'.format(a,b,a*b))
#使用语法糖简化
c = print(f'{a}*{b} = {a*b}');

#list 列表
list2 = [1,2,3,23,23,2]
print(list2)

list4 = ["唐鹏飞"]*3
print(list4)

#可以倒序下标获取数组
print(list2[-2])
#遍历数据
for e in list2:
    print(e);

#获取元素索引和值
for index,e in enumerate(list2):
    print(index,e)

#添加
list2.append("1")
#删除
list2.remove("1")

list2.clear()
#切片操作
list2 = [1,2,3,4,5,6]
list3 = list2[1:4]
print(list3)
#反转
list4 = list2[::-1]
print(list4)
#排序
list2 = sorted(list4)
print(list2)
#按照字符长度排序
list2 = ['123123','1','23']
list3 = sorted(list2,key=len)
print(list3)

list2.sort(reverse=True)
print(list2)
#使用循环生成列表
f = [x for x in range(1,10)]
print(f)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

t = ('实打实','请问',True,12312)

for e in t:
    print(e)

#元祖转数组
person = list(t)
print(person)
tuple(person)
#转回list
print(type(person))

num = set(range(1,0))
print(num)
num.discard(5)

scores = {'nima':23,'sda':23}

a = dict(ont=1,we=2,sd=1)
#更新
scores['nima'] = 12
print(scores)
scores.pop('nima',23)
print(scores)