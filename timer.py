import Tkinter
import threading
from time import sleep


class Timer(object):

    def __init__(self, hour, minute, second, window_handle):
        self.current_time = [hour, minute, second]
        self.wh = window_handle

    def getTime(self):
        return self.current_time

    def getStrTime(self):
        return ':'.join(["%02d"%(x) for x in self.current_time])

    def getHours(self):
        return self.current_time[0]

    def getMinutes(self):
        return self.current_time[1]

    def getSeconds(self):
        return self.current_time[2]

    def __call__(self):
        self.getTime()

    def changeTime(self):
        self.button.config(text=self.getStrTime())

    def addHour(self):
        if self.current_time[0] < 23:
            self.current_time[0] += 1
        else:
            self.current_time[0] = 0

    def show(self):
        self.label = Tkinter.LabelFrame(self.wh, text='Zegar')
        self.button = Tkinter.Button(
            self.label,
            command=lambda: self.addHour()
        )
        self.label.pack()
        self.button.pack()

        t = threading.Thread(target=self.run)
        t.start()

        return self

    def run(self):

        while 1:
            while self.current_time[0] < 24:
                while self.current_time[1] < 60:
                    while self.current_time[2] < 60:
                        self.current_time[2] += 1
                        self.changeTime()
                        sleep(1.0)

                    self.current_time[2] = 0
                    self.current_time[1] += 1

                self.current_time[1] = 0
                self.current_time[0] += 1

            self.current_time[0] = 0
