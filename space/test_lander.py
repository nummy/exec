import lander as L

def close(a, b, e=0.000001):
    return abs(a-b) < e

def test_lander_part1():
    L.thrust(1)

    assert close(L.velocity, 36) and close(L.fuel, 24), "thrust"

    L.thrust(1.7)
    assert close(L.velocity, 32) and close(L.fuel, 23), "thrust"

    L.thrust(6)

    assert close(L.velocity, 16) and close(L.fuel, 19), "thrust"
    
    L.fuel = 0
    L.thrust(1)
    assert close(L.velocity, 16) and close(L.fuel, 0), "thrust"
    
    L.update_onesecond()
    assert close(L.velocity, 17.622) and close(L.fuel, 0), "update_onesecond"
    
    L.altitude = 1
    L.update_onesecond()
    assert close(L.altitude, 0), "update_onesecond"
    
    L.altitude = 0
    assert L.has_crashed(), "has_crashed"
    
    L.velocity = 1
    assert L.has_safely_landed(), "has_safely_landed"
    print(L.get_status())
    assert L.get_status() == "Alt = 0.00 Vel = 1.00 Fuel = 0 Str = 4", \
           "get_status"

    print("test_lander part 1 SUCCESS!")
    
test_lander_part1()

# two test controllers that allow us to test simulate_landing as if the
#  human returned 0 or 4 every time when asked for how many thrusts.
def broken_controller():
    """ A broken implementation of a controller that doesn't use any
    thrusts """
    return 0    
def bad_controller():
    """ A bad implementation of a controller as using 4 thrusts every
    chance it gets will undoubtedly cause the lander to crash """
    return 4

def test_lander_part2():
    L.reset_lander(500, 40, 25)
    assert close(L.altitude, 500) and close(L.velocity, 40) \
            and close(L.fuel, 25) and close(L.strength, 4), "reset_lander"    
    
    assert L.simulate_landing(bad_controller) == \
           "Oh no the lander has crashed! Better skill next time!", \
           "simulate_landing"

    L.reset_lander(4, 0, 0)
    assert L.simulate_landing(broken_controller) == \
           "Great success! You should apply for an internship with NASA!", \
           "simulate_landing"
    
    
    #difficult to test user input, so we replace the input and print function
    # with test versions and capture what was input/printed
    L.reset_lander(4, 0, 0)
    import builtins, random
    r = random.randrange(1,4)
    printed = None
    asked_user = None
    def test_input(value):
        nonlocal asked_user #similar to global except special nonlocal namespace
        asked_user = value
        return r
    def test_print(value):
        nonlocal printed
        printed = value
    L.input = test_input
    L.print = test_print
    t = L.human_controller()
    # put the builtin functions back in global namespace
    L.input = builtins.input
    L.print = builtins.print
    assert t == r, "human_controller"
    assert printed == "Alt = 4.00 Vel = 0.00 Fuel = 0 Str = 4"
    assert asked_user == "How much thrust this round? ", "human_controller"    

    print("test_lander part 2 SUCCESS!")

test_lander_part2()

def test_lander_part3():
    # finally let's test the smart_controller
    L.reset_lander(500, 40, 25)
    assert L.simulate_landing(L.smart_controller) == \
           "Great success! You should apply for an internship with NASA!", \
           "simulate_landing(smart_controller) at altitude=500"
    L.reset_lander(1500, 40, 50)
    assert L.simulate_landing(L.smart_controller) == \
           "Great success! You should apply for an internship with NASA!", \
           "simulate_landing(smart_controller) at altitude=1500"
    L.reset_lander(2500, 40, 75)
    assert L.simulate_landing(L.smart_controller) == \
           "Great success! You should apply for an internship with NASA!", \
           "simulate_landing(smart_controller) at altitude=2500"
    
    print("test_lander part 3 SUCCESS!")
    
test_lander_part3()


def test_lander_part4():

    #can you land on earth with more fuel and a stronger lander?
    L.reset_lander(1000, 40, 50)
    L.reset_world(9.807, 20, -1, -1)
    assert L.simulate_landing(L.smart_controller) == \
               "Great success! You should apply for an internship with NASA!", \
               "simulate_landing(smart_controller) at alt=1000 on earth"

    L.reset_lander(500, 40, 50)
    L.reset_world(1.622, 8, 400, 800)
    L.update_onesecond()
    assert L.strength == 7, "update_onesecond atmosphere effects strength"

    
    L.reset_lander(1000, 40, 50)
    L.reset_world(1.622, 8, 400, 800)
    assert L.simulate_landing(L.smart_controller) == \
               "Great success! You should apply for an internship with NASA!", \
               "simulate_landing(smart_controller) at alt=1000 atm=300,800"
    
    print("test_lander part 4 SUCCESS!")
    
    
test_lander_part4()