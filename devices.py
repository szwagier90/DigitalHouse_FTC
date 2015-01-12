import Tkinter
import threading
import math

from time import sleep

class LightBulb(object):
    '''
    Zarowka (nazwa, jasnosc)
    '''
    def __init__(self, name, brightness=50, room_obj=None):
        self.name = name
        self.brightness = brightness

    def setOn(self, power=100):
        self.brightness = power

    def setOff(self):
        self.brightness = 0

    def setBrightness(self, value):
        self.brightness = value
        print '%s: %s' % (self.name, self.brightness)

    def isOn(self):
        return bool(self.brightness) or False

    def get(self):
        return self.brightness

    def show(self, room):
        label = Tkinter.LabelFrame(room, text=self.name)
        label.pack()
        scale = Tkinter.Scale(
            label,
            orient=Tkinter.HORIZONTAL,
            command=lambda x: self.setBrightness(scale.get())
        )
        scale.pack()

class AirTemp(object):
    '''
    Klimatyzacja (temperatura)
    '''
    def __init__(self, name, temp=20, room_obj=None):
        self.name = name
        self.temp = temp
        self.on = True
        self.room_obj = room_obj

    def setOnOff(self):
        self.on = not self.on
        print self.on

    def setTemperature(self, value):
        self.temp = value
        print '%s: %s' % (self.name, self.temp)

    def isOn(self):
        return self.on

    def get(self):
        return self.temp

    def set_config(self, temp=20):
            self.setOnOff()
            if self.isOn():
                self.scale.config(state=Tkinter.ACTIVE)
                self.scale.config(bg='white')
                self.button.config(bg='green')
                self.button.config(text='Turn OFF')
                self.label.config(bg='green')
                self.scale.set(temp)
            else:
                self.scale.config(state=Tkinter.DISABLED)
                self.scale.config(bg='black')
                self.button.config(bg='red')
                self.button.config(text='Turn ON')
                self.label.config(bg='red')

    def show(self, room):

        self.label = Tkinter.LabelFrame(room, text=self.name)

        self.scale = Tkinter.Scale(
            self.label,
            from_=self.room_obj.params['temperature']['min'],
            to=self.room_obj.params['temperature']['max'],
            state=Tkinter.ACTIVE,
            orient=Tkinter.HORIZONTAL,
            command=lambda x: self.setTemperature(self.scale.get())
        )

        self.button = Tkinter.Button(
            self.label,
            command=lambda: self.set_config()
        )

        self.set_config()

        self.label.pack()
        self.button.pack()
        self.scale.pack()

        t = threading.Thread(target=self.run)
        t.start()

    def run(self):
        while 1:
            p = self.room_obj.params['temperature']
            if self.on:
                sign = math.copysign(1, self.temp - p['value'])
                p['value'] += sign * p['step']
            elif p['value'] < p['min'] or p['value'] > p['max']:
                print 'Zbyt niska temperatura - WLACZAMY klimatyzacje'
                self.set_config(p['default'])
            sleep(3)


class Window(object):
    '''
    Okno (nazwa, stopien)
    '''
    def __init__(self, name, open_level=0, room_obj=None):
        self.name = name
        self.lvl = open_level  # stopien otworzenia okna

    def setOn(self, level=2):
        self.lvl = level
        if self.lvl == 0:
            print "Window {} is closed".format(self.name)

    def setOff(self):
        self.lvl = 0

    def isOn(self):
        return self.lvl

    def get(self):
        return self.lvl

    def show(self, room):
        label = Tkinter.LabelFrame(room, text=self.name)

        scale = Tkinter.Scale(
            label,
            from_=0,
            to=3,
            state=Tkinter.ACTIVE,
            orient=Tkinter.HORIZONTAL,
            command=lambda x: self.setOn(scale.get())
        )
        label.pack()
        scale.pack()

        t = threading.Thread(target=self.run)
        t.start()

    def run(self):
        pass
