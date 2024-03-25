from abc import ABCMeta, abstractmethod
import random
class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')
    def __init__(self,name,hp):
        self._name = name
        self._hp = hp


    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp


    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, enemy):
        pass



class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp, mp):
        super().__init__(name,hp)
        self._mp = mp

    # 普通攻击
    @abstractmethod
    def attack(self, enemy):
        enemy.hp -= random.randint(10, 30)

    # 大招
    def huge_attack(self,enemy):
        if enemy.mp > 50:
            enemy.mp -= 50
            injury = enemy.hp * 3 // 4
            injury = injury if injury > 50 else 0
            enemy.hp -= injury
            return True
        else:
           self.attack(enemy)
           return False


class Monster(Fighter):
    __slots__ = ('_name', '_hp', )

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

