class test01:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    @staticmethod
    def be_positive(a,b):
        return a-b>0



    def result(a,b):
        return a+b


def main():
    a = 2
    b = 1
    if test01.be_positive(a,b):
        print(test01.result(a,b));

if __name__ == '__main__':
    main();