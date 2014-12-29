import Tkinter

class Room(object):
    '''
    pokoje i ih parametry
    '''
    def __init__(self, name, window, rooms_list=[], devices_list=[], **params):
        self.rooms = rooms_list
        self.devices = devices_list
        self.name = name
        self.window = window

    def getVal(self, param):
        return self.params[param]

    def show(self):
        '''
        zwraca uchyt do okna
        :return: room
        '''
        room = Tkinter.LabelFrame(self.window, text=self.name)
        room.pack(fill='both', expand='yes', side=Tkinter.LEFT)

        return room