import Tkinter
import random
import threading

from time import sleep

class Room(object):
    '''
    pokoje i ich parametry
    '''
    def __init__(self, name, window, rooms_list=[], devices_list=[], timer=None):
        self.rooms = rooms_list
        self.devices = devices_list
        self.name = name
        self.window = window
        self.timer = timer

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
            },
            'motion': {
                'value': 0,
                'max': 1,
                'min': 0,
                'step': 1,
                'default': 0
            }
        }

    def getVal(self, param):
        return self.params[param]

    def getDevices(self):
        return self.devices

    def randVal(self):
        while 1:
            for key in ['humidity', 'smoke', 'temperature']:
                step = self.params[key]['step']
                self.params[key]['value'] += random.randint(-1*step, step)
            sleep(3)

    def simulateUser(self):
        self.params['motion']['value'] = 1
        self.room.config(bg='red')
        sleep(5)
        self.params['motion']['value'] = 0
        self.room.config(bg='white')

    def show(self):
        '''
        zwraca uchyt do okna
        :return: room
        '''
        self.room = Tkinter.LabelFrame(self.window, text=self.name, bg='white')
        self.room.pack(fill='both', side=Tkinter.LEFT)

        t = threading.Thread(target=self.randVal)
        t.start()

        return self.room