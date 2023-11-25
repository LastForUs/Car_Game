from ast import While
from queue import PriorityQueue
import time
import random
car_can_start = True
speed_changes = 0
quitting = False
car_commands_giver = ""
max_speed = 0
cars_current_speed = 0
did_car_crashed = False
wanna_play_again = ""
car_game = True
car_crashed = False
type_of_the_verb = ""
speed_change_multiplayer = 0
speed_change_multiplayer_bool = bool
def wait(time_waiting):
    time.sleep(time_waiting)


class CarCommands:
    def time_pass_speed_change(self):
        global speed_changes
        global speed_change_multiplayer
        global cars_current_speed
        speed_change_multiplayer = speed_changes
        speed_change_multiplayer_bool = True
        for i in range(0, speed_change_multiplayer + 1, 5):
            print(f"Your Car {type_of_the_verb} By {i}")
            wait(1.5)
            


    def show_cars_max_speed(self):
        global max_speed
        print(f"Your maximum speed is {max_speed}")

    def show_cars_current_speed(self):
        global cars_current_speed
        print(f"Your Cars Current Speed is:{cars_current_speed}")

    def add_speed_to_car(self):
        global cars_current_speed
        global speed_changes
        global type_of_the_verb
        type_of_the_verb = "Speed Up"
        cars_current_speed = speed_changes + cars_current_speed
        car_commands.time_pass_speed_change()
        print("Speed Added")
        print(f"Your Cars Current Speed is:{cars_current_speed}")
        return cars_current_speed


    def slow_down_the_car(self):
        global cars_current_speed
        global speed_changes
        global type_of_the_verb
        type_of_the_verb = "Slowed Down"
        cars_current_speed = cars_current_speed - speed_changes
        car_commands.time_pass_speed_change()
        print("Slowed Down")
        print(f"Your Cars Current Speed is:{cars_current_speed}")
        return cars_current_speed

    def car_crashed(self):
        print("You Crashed Your Car")
        wait(0.5)
        print("Do you want to play again")
        global wanna_play_again
        wanna_play_again= input(">>").lower()
        return wanna_play_again


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
            wait(1)
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
            wait(1)
            print("Car Stoped")
            car_can_start = True
        else:
            print("Slow The Car Down to 0")
    
    def qutting_car(self):
        global car_game
        global quitting
        global car_crashed
        car_game = False
        quitting = True
        if car_crashed == True:
            print("You Crashed The Car")
        else:
            return ''



car_commands = CarCommands()
car_commands.set_max_speed_car()
print("Type 'Help' for commands")
while car_game:
    
    if cars_current_speed > max_speed:
        while True:
            car_commands.car_crashed()
            if wanna_play_again == 'y':
                print("Starting The Game Again...")
                wait(0.5)
                print("------------------------------------------------------------------------------------------")
                wait(0.5)
                car_commands = CarCommands()
                car_commands.set_max_speed_car()
                print("Type 'Help' for commands")
                cars_current_speed = 0
                car_game = True
                car_can_start = True
                quitting = False
                break
            elif wanna_play_again == 'n':
                print("Stopping The Game...")
                car_commands.qutting_car()
                break
            else:
                print("I Don't understand that")

    if quitting == False:
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
        if not car_can_start and not quitting:
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
            # Shows Cars Current Speed
        else:
            print("Car is not started")
    elif car_commands_giver == "max":
        car_commands.show_cars_max_speed()
    else:
        print("I don't understand that")

    

