import Tkinter

window = Tkinter.Tk()

class Device(object):
    '''
    Klasa dla urzadzen/czujnikow
    '''
    def __init__(self, name, **params):
        self.name = name;
        self.params = params;

    def changeParam(self, **params):
        for k, v in params.items(): 
            self.params[k] = v
        print 'Obecne parametry urzadzenia to: {}'.format(self.params)


bulb = Device('zarowka', jasnosc=30, inout=0)

B = Tkinter.Button(
    window,
    text ="Zarowka",
    command = lambda: bulb.changeParam(jasnosc=10, inout=0)
)

scale = Tkinter.Scale(
    window,
    command = lambda x: bulb.changeParam(jasnosc=scale.get(), inout=not bulb.params['inout'])
)

scale.pack(side = Tkinter.RIGHT)
B.pack()
window.mainloop()
