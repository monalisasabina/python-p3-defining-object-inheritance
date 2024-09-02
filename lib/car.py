from vehicle import Vehicle

class Car(Vehicle):

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


print(Car.__bases__) #(<class 'vehicle.Vehicle'>,)
print(int.__bases__) #(<class 'object'>,)
print(Car.__class__) #<class 'type'>
print(int.__class__) #<class 'type'>