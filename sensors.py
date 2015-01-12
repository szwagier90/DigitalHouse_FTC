import Tkinter
import threading
import re

from time import sleep

class Sensor(object):
    '''
    Czujnik dymu
    '''
    def __init__(self, name, room_obj=None):

        self.name = name
        self.sensor = self.getSensorName(name)
        self.room_obj = room_obj
        self.value = None

    def read(self):
        #tutaj czytamy z pokoju lub z generowanych wartosci sensora (do uzgodnienia)
        self.value = self.room_obj.getVal(self.sensor)['value']
        print 'odczyt z urzadzenia: {} = {}'.format(self.name, self.value)

    def show(self, windowh):
        button = Tkinter.Button(
            windowh,
            text='Read {}'.format(self.name),
            command=lambda: self.read()
        )
        button.pack()
        t = threading.Thread(target=self.run)
        t.start()

    def run(self):

        while 1:
            param = self.room_obj.getVal(self.sensor)
            self.value = param['value']
            print 'odczyt cykliczny z urzadzenia: {} = {}'.format(self.name, self.value)
            if param['max'] < self.value or param['min'] > self.value:
                print 'WARNING: {} = {}'.format(self.name, self.value)
            sleep(5)

    def getSensorName(self, name):
        return re.match(r'([a-z]*)_sensor.*', name).groups()[0]
