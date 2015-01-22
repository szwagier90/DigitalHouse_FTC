import Tkinter
import threading
import math

from time import sleep

class AirTemp(object):
    '''
    Klimatyzacja (temperatura)
    '''
    def __init__(self, name, temp=20, room_obj=None, monitor=None):
        self.name = name
        self.temp = temp
        self.on = True
        self.room_obj = room_obj
        self.get_devices = room_obj.getDevices
        self.timer = room_obj.timer
        self.monitor = monitor

    def setOnOff(self):
        if self.on:
            self.setOff()
        else:
            self.setOn()

    def setOn(self):
        if self.monitor.auto and ('SMOKE' not in self.monitor.warnings):
            for dev in self.get_devices():
                if dev.name.startswith('window'):
                    dev.setOff()
        self.on = True

    def setOff(self):
        self.on = False

    def setTemperature(self, value):
        self.temp = value
        print '%s: %s' % (self.name, self.temp)

    def isOn(self):
        return self.on

    def get(self):
        return self.temp

    def set_config(self, temp=20, func=None):
            if func == None:
                self.setOnOff()
            else:
                func()

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

        self.label.pack(fill=Tkinter.X)
        self.button.pack(fill=Tkinter.X)
        self.scale.pack(fill=Tkinter.X)


        t = threading.Thread(target=self.run)
        t.start()

    def run(self):
        sleep(3)
        t = None    #sensor temperatury

        for dev in self.get_devices():
            print dev.name
            try:
                if dev.sensor == 'temperature':
                    t = dev
            except AttributeError:
                pass
        while 1:
            if self.monitor.auto:
                h = self.timer.getHours()
                p = self.room_obj.params['temperature'] #parametry pokoju
                if self.on:
                    sign = math.copysign(1, self.temp - t.value)
                    p['value'] += sign * p['step']
                elif t.value < p['min'] or t.value > p['max']:
                    print 'Zbyt niska temperatura - WLACZAMY klimatyzacje'
                    self.set_config(p['default'])

                if h > 20 or h < 6:
                    self.set_config(17, self.setOn)
                elif self.on:
                    self.set_config(p['default'], self.setOn)

            sleep(3)


