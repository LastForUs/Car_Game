import time
import random
car_can_start = True
quitting = False
max_speed = 0
cars_current_speed = 0
did_car_crashed = False


class CarCommands:
    def slow_down_the_car(self):
        print("slowed down")

    def add_speed_to_car(self):
        print("speed added")

    def car_crashed(self):
        global did_car_crashed
        did_car_crashed = True
        # Crashes The Car

    def set_max_speed_car(self, max_speed_def):
        max_speed_def = range(100, 200)
        return max_speed_def

    def help_car_c(self):
        print('''
Start - starts the car
Stop - stops the car
Add( Speed) - adds speed to the car but be careful there is a limit 
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
car_commands.set_max_speed_car(max_speed)
print("Type 'Help' for commands")
while True:

    car_commands_giver = input(">>").lower()
    if car_commands_giver == ('start' or 'sr'):
        car_commands.start_car()
        # Starts The Car
    elif car_commands_giver == ('stop' or 'so'):
        car_commands.stop_car()
        # Stops the car
    elif car_commands_giver == ('help' or 'h'):
        car_commands.help_car_c()
        # Shows the commands
    elif car_commands_giver == ('quit' or 'q'):
        quitting = True
        break
        # Closes The Game
    elif car_commands_giver == ("add" or "add speed"):
        car_commands.add_speed_to_car()
        # Adds speed to car
    elif car_commands_giver == ("slow" or "slow down"):
        car_commands.slow_down_the_car()
        # Slows down the car
    else:
        print("I don't understand that")
