import Tkinter

class SmokeSensor(object):
    '''
    Czujnik dymu
    '''
    def __init__(self, name, my_room_obj):

        self.name = name
        #obiekt pokoju do ktorego nalezy sensor
        self.room = my_room_obj

    def read(self):
        #tutaj czytamy z pokoju lub z generowanych wartosci sensora (do uzgodnienia)
        #print self.room.getVal()
        print 'odczyt'

    def show(self, windowh):
        button = Tkinter.Button(
            windowh,
            text='Read Smoke',
            command=lambda: self.read()
        )
        button.pack()