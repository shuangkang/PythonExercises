class Man(object):
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    @property
    def getname(self):
        return self.name

    @property
    def getage(self):
        return self.age

    @property
    def getaddress(self):
        return self.getaddress

    def eat(self):
        if self.address == '杭州':
            print('%s正在吃崔强.' % self.name)
        else:
            print('%s正在吃奥利给.' % self.name)

def main():
    man = Man('唐鹏飞',22,'地球人')
    man.eat()
    man.address = '杭州'
    man.eat();

if __name__ == '__main__':
    main()