class Car: 
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        
    def speed_un(self):
        self.speed += 10
    
car_n = Car("Green", 100)
car_n.speed_un()
car_n.speed #110

#car.color      # allowed (clean interface)
#car._color     # internal

# + __add__
# - __sub__
# // __div__
# % __mod__