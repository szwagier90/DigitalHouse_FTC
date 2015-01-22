import threading
import Tkinter

from time import sleep

class SmokeDetector(object):
    '''
    Wykrywacz dymu (nazwa, jasnosc)
    '''
    def __init__(self, name, room_obj=None, monitor=None):
        self.name = name
        self.room_obj = room_obj
        self.monitor = monitor

    def show(self, room):
        t = threading.Thread(target=self.run)
        t.start()

    def run(self):
        while 1:
            if self.room_obj.params['smoke']['value'] > 95:
                self.monitor.warnings.append('SMOKE')

            sleep(2)
