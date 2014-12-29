import json
import Tkinter
from devices import LightBulb
from sensors import SmokeSensor
from room import Room


class Monitor(object):
    '''
    Przeplyw sterowania
    '''
    def __init__(self):
        self.window = Tkinter.Tk()

        self.room1 = Room('Room1', self.window)
        self.room2 = Room('Room2', self.window)

        self.light1 = LightBulb('light1', 50)
        self.light2 = LightBulb('light2', 30)

        self.smoke1 = SmokeSensor('smoke1', self.room1)

    def readFromFile(self, filename):
        #na podstawie tego pliku bedziemy generowac pomieszczenia
        with open(filename, 'r') as fileh:
            json_data = fileh.read()
            data = json.loads(json_data)

        return data['device'], data['rooms'], data['start_time']

    def showBoard(self):

        room1 = self.room1.show()
        room2 = self.room2.show()

        self.light1.show(room1)

        self.light2.show(room2)

        self.smoke1.show(room1)

        self.window.mainloop()

if __name__ == '__main__':
    m=Monitor()
    m.showBoard()

    #m.readFromFile('in.txt')
