from queue import PriorityQueue
import time
import random
car_can_start = True
speed_changes = 0
quitting = False
max_speed = 0
cars_current_speed = 0
did_car_crashed = False
Car_Game = True
Car_Crashed = False


class CarCommands:

    def show_cars_max_speed(self):
        global max_speed
        print(f"Your maximum speed is {max_speed}")

    def show_cars_current_speed(self):
        global cars_current_speed
        print(cars_current_speed)

    def add_speed_to_car(self):
        global cars_current_speed
        global speed_changes
        cars_current_speed = speed_changes + cars_current_speed
        print("Speed Added")
        return cars_current_speed


    def slow_down_the_car(self):
        global cars_current_speed
        global speed_changes
        cars_current_speed = cars_current_speed - speed_changes
        print("Slowed Down")
        return cars_current_speed

    def car_crashed(self):
        global did_car_crashed
        did_car_crashed = True
        global Car_Crashed
        Car_Crashed = True
        car_commands.qutting_car()
        # Crashes The Car

    def set_max_speed_car(self):
        global max_speed
        max_speed = random.randint(100, 200)
        print (max_speed)
        return max_speed

    def help_car_c(self):
        print('''
Start - starts the car
Stop - stops the car
Add(_Speed) - adds speed to the car but be careful there is a limit 
Slow(_Down) - slow down the car
Current(_Speed) - shows haw fast car is going
Max(_Speed) - shows the speed litmit of your car
Quit - closes the game        
''')

    def start_car(self):
        global car_can_start
        if car_can_start:
            print ("Car İs Starting")
            time.sleep(1)
            print("Car Started")
            car_can_start = False
        elif not car_can_start:
            print("Car Already Started")

    def stop_car(self):
        global car_can_start
        if car_can_start:
            print("Car is not started")
        elif not car_can_start and cars_current_speed == 0:
            print("Car İs Stopping")
            time.sleep(1)
            print("Car Stoped")
            car_can_start = True
        else:
            print("Slow The Car Down to 0")
    
    def qutting_car(self):
        global Car_Game
        global quitting
        global Car_Crashed
        Car_Game = False
        quitting = True
        if Car_Crashed == True:
            print("You Crashed The Car")
        else:
            return ''



car_commands = CarCommands()
car_commands.set_max_speed_car()
print("Type 'Help' for commands")
while Car_Game:
    
    if cars_current_speed > max_speed:
        car_commands.car_crashed()
        break

    car_commands_giver = input(">>").lower()
    if car_commands_giver == 'start':
        car_commands.start_car()
        # Starts The Car
    elif car_commands_giver == 'stop':
        car_commands.stop_car()
        # Stops the car
    elif car_commands_giver == ('help' or 'h'):
        car_commands.help_car_c()
        # Shows the commands
    elif car_commands_giver == ('quit' or 'q'):
        if car_can_start:
            car_commands.qutting_car()
            break
        else:
            print("Stop The Car")
        # Closes The Game
    elif car_commands_giver == "add" or car_commands_giver == "slow":
        if not car_can_start:
            print ("How Much Speed You Want To Change")
            x = True
            while x:
                x = False
                try:
                    speed_changes = int(input(">>"))
                except ValueError:
                    print("Please Write A Number")
                    x = True
                if car_commands_giver == "slow":
                    car_commands.slow_down_the_car()
                elif car_commands_giver == "add":
                    car_commands.add_speed_to_car()
        else:
            print("Car is not started")
        # Changes The Speed Of The Car
    elif car_commands_giver == "current":
        if not car_can_start:
            car_commands.show_cars_current_speed()
        else:
            print("Car is not started")
    elif car_commands_giver == "max":
        car_commands.show_cars_max_speed()
    else:
        print("I don't understand that")
