import time
import random
car_can_start = True
quitting = False


class CarCommands:
    def help_car_c(self):
        print('''
Start - starts the car
Stop - stops the car
Quit - closes the game        
''')

    def start_car(self):
        global car_can_start
        if car_can_start:
            print ("Car Started")
            car_can_start = False
        elif not car_can_start:
            print("Car Already Started")

    def stop_car(self):
        global car_can_start
        if car_can_start:
            print("Car is not started")
        elif not car_can_start:
            print("Car Stopped")
            car_can_start = True


car_commands = CarCommands()
print("Type 'Help' for commands")
while True:
    car_commands_giver = input(">>").lower()
    if car_commands_giver == ('start' or 'sr'):
        car_commands.start_car()
    elif car_commands_giver == ('stop' or 'so'):
        car_commands.stop_car()
    elif car_commands_giver == ('help' or 'h'):
        car_commands.help_car_c()
    elif car_commands_giver == ('quit' or 'q'):
        quitting = True
        break
    else:
        print("I don't understand that")
