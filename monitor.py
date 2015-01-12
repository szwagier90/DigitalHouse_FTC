import json
import Tkinter
from devices import LightBulb, AirTemp, Window
from sensors import Sensor
from room import Room
from timer import Timer

DEV = {
    'light': LightBulb,
    'smoke_sensor': Sensor,
    'humidity_sensor': Sensor,
    'air_condition': AirTemp,
    'temperature_sensor': Sensor,
    'window': Window,
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
        self.timer = Timer(1,2,3, self.window).show()

    def readFromFile(self, filename):
        '''
        odczyt pliku Json
        '''
        with open(filename, 'r') as fileh:
            json_data = fileh.read()
            data = json.loads(json_data)

        return data['device'], data['rooms'], data['start_time']

    def generateRooms(self):
        '''
        generowanie objektow pomieszczen,
        dane obiekty zapisujemy do self.rooms (patrz __init__)
        '''
        devices, rooms, time = self.readFromFile(self.filename)



        for room in devices.keys():
            self.rooms[room] = {
                'object': Room(room, self.window)
            }
            self.rooms[room]['handle'] = self.rooms[room]['object'].show()
            self.rooms[room]['devices'] = []

            for device in devices[room]:
                #dodajemy obiekty urzadzen na liste
                try:
                    self.rooms[room]['devices'].append(
                        DEV[device](
                            name='{}:{}'.format(device, room),
                            room_obj=self.rooms[room]['object'])
                    )
                    self.rooms[room]['devices'][-1].show(self.rooms[room]['handle'])
                except KeyError:
                    print 'Nie mozna zidentyfikowac urzadzenia {}. Nie zostalo dodane.'.format(device)

    def showBoard(self):
        self.generateRooms()
        self.window.mainloop()

if __name__ == '__main__':
    m = Monitor('in.txt')
    m.showBoard()