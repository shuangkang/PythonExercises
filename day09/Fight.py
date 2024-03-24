from abc import ABCMeta, abstractmethod
from random import randint

class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0

    @property
    def alive(self):
        return self.hp > 0

    @abstractmethod
    def attack(self, other):
        pass

class Player(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):  # 添加attack方法的实现
        damage = randint(10, 20)
        other.hp -= damage
        print('%s对%s造成了%s伤害' % (self.name, other.name, damage))

    def grab_the_milk_dragon_gripper(self, other):
        damage = randint(15, 25)
        other.hp -= damage
        print('%s使用了抓奶龙爪手对%s造成了%s伤害,,%s的生命剩余%s' % (self.name, other.name, damage,other.name,other.hp))

    def cnm(self):
        heal = randint(10, 20)
        self.hp += heal
        print('%s大喝一声cnm给自己回复了%s点生命' % (self.name, heal))

    def crotchless(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            print('%s使用了必杀技!掏裆对%s造成了%s伤害,%s的生命剩余%s' % (self.name, other.name, injury,other.name,other.hp))
            return True
        else:
            self.attack(other)
            print('%s对%s使用的掏裆失败了' % (self.name, other.name))
            return False

def main():
    p1 = Player('唐鹏飞', 200, 100)
    p2 = Player('郭恩腾', 200, 100)
    while p1.alive and p2.alive:
        skill = randint(1, 20)
        if skill <= 4:
            p1.attack(p2)
            if not p2.alive:
                print("p2G了")
                break
        elif skill == 5:
            p1.cnm()
        elif skill == 6:
            p1.crotchless(p2)
            if not p2.alive:
                print("p2G了")
                break
        elif 6 < skill <= 10:
            p1.grab_the_milk_dragon_gripper(p2)
            if not p2.alive:
                print("p2G了")
                break
        elif 10 < skill <= 14:
            p2.attack(p1)
            if not p1.alive:
                print("p1G了")
                break
        elif skill == 15:
            p2.cnm()
        elif skill == 16:
            p2.crotchless(p1)
            if not p1.alive:
                print("p1G了")
                break
        else:
            p2.grab_the_milk_dragon_gripper(p1)
            if not p1.alive:
                print("p1G了")
                break

if __name__ == '__main__':
    main()
