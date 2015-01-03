import Tkinter

class LightBulb(object):
    '''
    Zarowka (nazwa, jasnosc)
    '''
    def __init__(self, name, brightness=50):
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
    def __init__(self, name, temp=20):
        self.name = name
        self.temp = temp
        self.on = True

    def setOnOff(self):
        self.on = not self.on

    def setTemperature(self, value):
        self.temp = value
        print '%s: %s' % (self.name, self.temp)

    def isOn(self):
        print self.on
        return self.on

    def get(self):
        return self.temp

    def show(self, room):

        label = Tkinter.LabelFrame(room, text=self.name)

        def set_config():
            self.setOnOff()
            if self.isOn():
                scale.config(state=Tkinter.ACTIVE)
                scale.config(bg='white')
                button.config(bg='green')
                button.config(text='Turn OFF')
                label.config(bg='green')
            else:
                scale.config(state=Tkinter.DISABLED)
                scale.config(bg='black')
                button.config(bg='red')
                button.config(text='Turn ON')
                label.config(bg='red')

        scale = Tkinter.Scale(
            label,
            from_=10,
            to=30,
            state=Tkinter.ACTIVE,
            orient=Tkinter.HORIZONTAL,
            command=lambda x: self.setTemperature(scale.get())
        )

        button = Tkinter.Button(
            label,
            command=lambda: set_config()
        )

        set_config()

        label.pack()
        button.pack()
        scale.pack()
