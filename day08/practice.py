class Student(object):
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, incident):
        print(self.name + '正在' + incident + ',今年' + str(self.age) + '岁,是学生')


def main():
    test = Student('唐鹏飞', 21)
    test.study('打炉石')


if __name__ == '__main__':
    main()  # 调用 main 函数以执行代码
