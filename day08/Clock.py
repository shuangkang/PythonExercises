import time


class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        while True:
            time.sleep(1)
            self.sec += 1
            if self.sec == 60:
                self.min += 1
                self.sec = 0
                if self.min == 60:
                    self.hour += 1
                    self.min = 0
                    if self.hour == 24:
                        self.hour = 0
            print("%02d:%02d:%02d" % (self.hour, self.min, self.sec))


def main():
    clock = Clock(23, 59, 55)
    clock.run()


if __name__ == "__main__":
    main()
