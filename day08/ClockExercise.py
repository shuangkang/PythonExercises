from time import sleep
class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.min = minute
        self.second = second
    #时钟规则 self代表对象本身
    def run(self):
        self.second+=1
        if self.second==60:
            self.second=0
            self.min +=1
            if self.min==60:
                self.min=0
                self.hour+=1
                if self.hour==24:
                    self.hour=0;

    def show(self):
        return '%02d:%02d:%02d' % \
            (self.hour,self.min,self.second)

def main():
    clock = Clock(23,59,59);
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()