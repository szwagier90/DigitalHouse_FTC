import json
import Tkinter
import threading
import random

from aircondition import AirTemp
from window import Window
from light import LightBulb
from sensors import Sensor
from room import Room
from timer import Timer
from time import sleep

DEV = {
    'light': LightBulb,
    'smoke_sensor': Sensor,
    'humidity_sensor': Sensor,
    'air_condition': AirTemp,
    'temperature_sensor': Sensor,
    'window': Window,
    'motion_sensor': Sensor
}

class Monitor(object):
    '''
    Przeplyw sterowania
    '''
    def __init__(self, config_file):
        self.window = Tkinter.Tk()

        self.filename = config_file
        #rooms = {
        #   room1: {
        #       handle:,
        #       object:,
        #       devices: [],
        #   },
        # }
        self.rooms = {}  #uchwyty do okien dla pokojow
        self.timer = Timer(1, 2, 3, self.window).show()
        self.auto = False
        self.manual_auto()
        self.control()

    def manual_auto(self):

        def change_ma():
            self.auto = not self.auto
            if self.auto:
                self.button_ma.config(text='Set manual')
            else:
                self.button_ma.config(text='Set auto')

        self.label_ma = Tkinter.LabelFrame(self.window, text='Set auto/manual')
        self.button_ma = Tkinter.Button(
            self.label_ma,
            text = 'set_auto',
            command=lambda: change_ma()
        )
        self.label_ma.pack(side=Tkinter.TOP)
        self.button_ma.pack()

    def readFromFile(self, filename):
        '''
        odczyt pliku Json
        '''
        with open(filename, 'r') as fileh:
            json_data = fileh.read()
            data = json.loads(json_data)

        return data['device'], data['rooms'], data['start_time']

    def control(self):
        label_war = Tkinter.LabelFrame(self.window, text='WARNING')
        label = Tkinter.Label(label_war, text='jakie tam ostrzezenie\ntrolololo\ndgfdg\n', fg='red')
        label.pack(fill='both')
        label_war.pack(fill='x', side=Tkinter.TOP)


    def generateRooms(self):
        '''
        generowanie objektow pomieszczen,
        dane obiekty zapisujemy do self.rooms (patrz __init__)
        '''
        devices, self.room_plan, time = self.readFromFile(self.filename)

        print self.room_plan

        for room in devices.keys():
            self.rooms[room] = {
                'object': Room(room, self.window, timer=self.timer)
            }
            self.rooms[room]['handle'] = self.rooms[room]['object'].show()
            self.rooms[room]['devices'] = []

            for device in devices[room]:
                #dodajemy obiekty urzadzen na liste
                try:
                    self.rooms[room]['devices'].append(
                        DEV[device](
                            name='{}:{}'.format(device, room),
                            room_obj=self.rooms[room]['object'],
                            monitor=self
                        )
                    )
                    self.rooms[room]['devices'][-1].show(self.rooms[room]['handle'])
                except KeyError:
                    print 'Nie mozna zidentyfikowac urzadzenia {}. Nie zostalo dodane.'.format(device)
            self.rooms[room]['object'].devices = self.rooms[room]['devices']

        #przelaczanie na auto lub manual

        t = threading.Thread(target=self.showUser)
        t.start()

    def showUser(self):
        name = random.choice(self.rooms.keys())

        while 1:
            key = random.choice(self.room_plan[name])
            r = self.rooms[key]['object']
            name = r.name
            r.simulateUser()


    def showBoard(self):
        self.generateRooms()
        self.window.mainloop()

if __name__ == '__main__':
    m = Monitor('in.txt')
    m.showBoard()