class vehicle:
    def move(self):
        print("This vehichle is moving ")
        
class car(vehicle):
    def move(self):
        print("driving on the road")
        
class bicycle(vehicle):
    def move(self):
        print("pedaling on the road")
        
vehicles=[car(),bicycle]
for vehicle in vehicles:
    vechile,move()
print(vehicles)