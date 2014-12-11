class Sensor():
    '''abstrakcyjna'''
    def reading():
        pass

class Device():
    '''abstrakcyjna dla urzadzen'''
    def showAllParams():
        pass

class LightBulb(Device):
    '''dla konkretnego urzadzenia/sensora'''
    def __init__(self, name, brightness):
        pass

    def setOn(brightness=100)
        pass
    
    def setOff()
        pass
    
    def setBrightness(val);
        pass
    
    def isOn()
        return on

class Sensor1(Sensor):
    '''dla konkretnego sensora'''
    def readValue()
        pass
    
    def setValue()
        pass

class Monitor():
    '''zarzadzanie sensorami i urzadzeniami'''
    pass
