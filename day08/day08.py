class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


def main():
    kmh = Student('kmh', 27)
    kmh.print_info()

if __name__ == '__main__':
    main()