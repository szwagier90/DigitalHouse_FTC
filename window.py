import threading
import Tkinter

from time import sleep

class Window(object):
    '''
    Okno (nazwa, stopien)
    '''
    def __init__(self, name, open_level=0, room_obj=None, monitor=None):
        self.name = name
        self.lvl = open_level  # stopien otworzenia okna
        self.timer = room_obj.timer
        self.room_obj = room_obj
        self.monitor = monitor

    def setOn(self, level=2):
        self.lvl = level
        if self.lvl == 0:
            print "Window {} is closed".format(self.name)
            self.set_config(0)
        else:
            self.set_config(level)

    def setOff(self):
        self.lvl = 0
        self.set_config(0)

    def isOn(self):
        return self.lvl

    def get(self):
        return self.lvl

    def set_config(self, lvl):
        self.scale.set(lvl)
        if lvl > 0:
            self.scale.config(bg='white')
        else:
            self.scale.config(bg='black')

    def show(self, room):
        self.label = Tkinter.LabelFrame(room, text=self.name)

        self.scale = Tkinter.Scale(
            self.label,
            from_=0,
            to=3,
            state=Tkinter.ACTIVE,
            orient=Tkinter.HORIZONTAL,
            command=lambda x: self.setOn(self.scale.get())
        )
        self.label.pack(fill=Tkinter.X)
        self.scale.pack(fill=Tkinter.X)

        t = threading.Thread(target=self.run)
        t.start()

    def run(self):
        pass