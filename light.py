import threading
import Tkinter

from time import sleep

class LightBulb(object):
    '''
    Zarowka (nazwa, jasnosc)
    '''
    def __init__(self, name, brightness=50, room_obj=None):
        self.name = name
        self.brightness = brightness
        self.timer = room_obj.timer
        self.room_obj = room_obj
        self.get_devices = room_obj.getDevices  #funkcja, ktora zwraca liste urzadzen

    def setOn(self, power=100):
        self.brightness = power

    def setOff(self):
        self.brightness = 0
        self.set_config(0)

    def setBrightness(self, value):
        self.brightness = value
        self.set_config(value)
        #print '%s: %s' % (self.name, self.brightness)

    def isOn(self):
        return bool(self.brightness) or False

    def get(self):
        return self.brightness

    def set_config(self, value):
        color = '#'+str(hex(int('0xffffff', 16) - value*2))[2:]
        #self.room_obj.room.config(bg=color)
        if value == 0:
            color = 'black'
        self.scale.config(bg=color)
        self.scale.set(value)

    def show(self, room):
        self.label = Tkinter.LabelFrame(room, text=self.name)
        self.label.pack(fill=Tkinter.X)
        self.scale = Tkinter.Scale(
            self.label,
            orient=Tkinter.HORIZONTAL,
            command=lambda x: self.setBrightness(self.scale.get())
        )
        self.scale.pack(fill=Tkinter.X)

        t = threading.Thread(target=self.run)
        t.start()

    def run(self):

        sleep(3)
        t = None    #sensor temperatury

        for dev in self.get_devices():
            print dev.name
            try:
                if dev.sensor == 'motion':
                    t = dev
            except AttributeError:
                pass

        while 1:
            try:
                if t.value:
                    self.setBrightness(80)
                else:
                    self.setBrightness(0)

            except AttributeError:
                pass