import Tkinter
import random
import threading

from time import sleep

class Room(object):
    '''
    pokoje i ich parametry
    '''
    def __init__(self, name, window, rooms_list=[], devices_list=[]):
        self.rooms = rooms_list
        self.devices = devices_list
        self.name = name
        self.window = window
        self.params = {
            'humidity': {
                'value': 40,
                'max': 60,
                'min': 10,
                'step': 2,
                'default': 40
            },
            'smoke': {
                'value': 30,
                'max': 50,
                'min': 10,
                'step': 2,
                'default': 30
            },
            'temperature': {
                'value': 20,
                'max': 25,
                'min': 15,
                'step': 1,
                'default': 20
            }
        }

    def getVal(self, param):
        return self.params[param]

    def randVal(self):
        while 1:
            for key in self.params.keys():
                step = self.params[key]['step']
                self.params[key]['value'] += random.randint(-1*step, step)
            sleep(3)

    def show(self):
        '''
        zwraca uchyt do okna
        :return: room
        '''
        room = Tkinter.LabelFrame(self.window, text=self.name)
        room.pack(fill='both', expand='yes', side=Tkinter.LEFT)

        t = threading.Thread(target=self.randVal)
        t.start()

        return room