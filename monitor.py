import json
import Tkinter
import threading
import random

from aircondition import AirTemp
from smoke_detector import SmokeDetector
from window import Window
from light import LightBulb
from sensors import Sensor
from room import Room
from timer import Timer
from time import sleep

DEV = {
    'light': LightBulb,
    'smoke_detector': SmokeDetector,
    'humidity_sensor': Sensor,
    'air_condition': AirTemp,
    'temperature_sensor': Sensor,
    'window': Window,
    'motion_sensor': Sensor
}

DOOR_SECRET_PASSWORD = "32167"

class Monitor(object):
    '''
    Przeplyw sterowania
    '''
    def __init__(self, config_file):
        self.warning_strings = {
            'SMOKE': 'Uwaga wykryto dym! Możliwy pożar!',
            'PASSWORD_INCORRECT': "Ktos chcial sie wlamac!!!"
        }

        self.window = Tkinter.Tk()

        self.filename = config_file

        self.rooms = {}  #uchwyty do okien dla pokojow
        self.timer = Timer(1, 2, 3, self.window).show()
        self.auto = False
        self.manual_auto()
        self.warnings = []
        self.open_door_button = None
        self.warning_window()
        self.open_the_door()

    def manual_auto(self):

        def set_auto_manual():
            self.auto = not self.auto
            if self.auto:
                self.button_ma.config(text='SET MANUAL')
            else:
                self.button_a.config(text='SET AUTO')

        self.label_ma = Tkinter.LabelFrame(self.window, text='Set auto/manual')
        self.button_ma = Tkinter.Button(
            self.label_ma,
            text = 'SET AUTO',
            command=lambda: set_auto_manual()
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

    def open_the_door(self):
        def input_door_password():
            password_window = Tkinter.Toplevel()
            password_window.title('Input password')
            password_window.focus_set()

            input_password_label = Tkinter.Label(password_window, text="Wprowadz haslo")
            input_password_label.pack(side=Tkinter.LEFT)
            password = Tkinter.Entry(password_window, bd=4)
            password.pack(side = Tkinter.RIGHT)

            def confirm_door_password():
                if password.get() == DOOR_SECRET_PASSWORD:
                    self.warnings.append('PASSWORD_OK')
                else:
                    self.warnings.append('PASSWORD_INCORRECT')
                password_window.destroy()

            confirm_door_password_button = Tkinter.Button(
                password_window,
                text = 'OK',
                command=lambda: confirm_door_password()
            )       
            confirm_door_password_button.pack()

        self.open_door_button = Tkinter.Button(
            self.window, 
            text = 'Otworz drzwi',
            command=lambda: input_door_password()
        )
        self.open_door_button.pack()

    def warning_window(self):
        label_war = Tkinter.LabelFrame(self.window, text='WARNING')
        label = Tkinter.Label(label_war, text='jakie tam ostrzezenie\ntrolololo\ndgfdg\n', fg='red')
        label.pack(fill='both')
        label_war.pack(fill='x', side=Tkinter.TOP)

        def cancel_alarms():
            self.warnings = []

        cancel_alarms_button = Tkinter.Button(
            label_war,
            text = 'Zresetuj system alarmowy',
            command=lambda: cancel_alarms()
        )       
        cancel_alarms_button.pack()

        def generate_warning_string():
            while 1:
                string = ""

                for w in self.warning_strings.keys():
                    if w in self.warnings:
                        string += self.warning_strings[w] + "\n"
                label.config(text=string)

                if 'PASSWORD_OK' in self.warnings:
                    self.open_door_button.config(bg="green")
                    self.open_door_button.config(text="Access Granted")
                    sleep(3)
                    self.open_door_button.config(bg="light grey")
                    self.open_door_button.config(text="Otworz drzwi")
                    self.warnings.remove('PASSWORD_OK') 

                sleep(2)

        t = threading.Thread(target=generate_warning_string)
        t.start()

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
