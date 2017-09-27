import math

altitude = 1000
velocity = 40
fuel = 25
strength = 4
gravity = 1.622
velocity_change_per_thrust =  4


def get_status():
    return "Alt = %.2f Vel = %.2f Fuel = %s Str = %s" % (altitude, velocity, fuel, strength)

def thrust(number):
    global fuel
    global velocity
    arr = str(fuel).split(".")
    if len(arr) == 1:
        prec = 0
    else:
        prec = len(arr[1])
    number = math.floor(number)
    if number > strength:
        number = strength
    if number > fuel:
        number = fuel
    velocity = velocity - number*velocity_change_per_thrust
    fuel = fuel - number

def update_onesecond():
    global velocity
    global altitude
    velocity = velocity + gravity
    altitude = altitude - velocity
    if altitude < 0:
        altitude = 0

def has_crashed():
    if altitude <= 0 and velocity>strength:
        return True
    else:
        return False

def has_safely_landed():
    if altitude <= 0 and velocity <=  strength:
        return True
    else:
        return False


def reset_lander(a, v, f):
    global altitude
    global velocity
    global fuel
    altitude = a
    velocity = v
    fuel = f

def human_controller():
    print(get_status())
    t = input("How much thrust this round? ")
    return math.floor(t)

def simulate_landing(player):
    while True:
        t = player()
        thrust(t)
        update_onesecond()
        if has_crashed():
            return "Oh no the lander has crashed! Better skill next time!"
        if has_safely_landed():
            return "Great success! You should apply for an internship with NASA!"

def smart_controller():
    pass

