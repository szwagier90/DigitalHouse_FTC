import Tkinter

class SmokeSensor(object):
    '''
    Czujnik dymu
    '''
    def __init__(self, name):

        self.name = name

    def read(self):
        #tutaj czytamy z pokoju lub z generowanych wartosci sensora (do uzgodnienia)
        print 'odczyt z urzadzenia: {}'.format(self.name)

    def show(self, windowh):
        button = Tkinter.Button(
            windowh,
            text='Read {}'.format(self.name),
            command=lambda: self.read()
        )
        button.pack()