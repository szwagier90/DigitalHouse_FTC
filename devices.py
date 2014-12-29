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
