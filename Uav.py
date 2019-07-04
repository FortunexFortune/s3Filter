from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
    return abs((d2 - d1).days)
    
class Uav:
    uavsOfIntrest = []

    def __init__(self):
        pass

    def addUav(self, uavs):
        for uav in uavs:
            LastModified = uav.get('LastModified')
            objCreationDate = LastModified.strftime("%Y-%m-%d %H:%M:%S")
            currentDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            diff = days_between(objCreationDate, currentDate)
            if diff <= 7:
                self.uavsOfIntrest.append(uav)
        return self.uavsOfIntrest