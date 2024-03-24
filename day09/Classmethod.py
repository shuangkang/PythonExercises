from time import time, localtime, sleep


class bell(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d时%02d分%02d秒' % \
               (self._hour, self._minute, self._second)


def main():
    bell1 = bell.now()
    while True:
        print(bell1.show())
        sleep(1)
        bell.run(bell1)


if __name__ == '__main__':
    main()