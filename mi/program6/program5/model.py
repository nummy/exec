import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
from goody     import type_as_str
from ball      import Ball
from hunter    import Hunter
from special   import Special 
from floater   import Floater
from pulsator  import Pulsator
from blackhole import Black_Hole



# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running       = False
cycle_count   = 0
kind          = "Ball"
balls         = set()
pulsators     = set()
black_holes   = set()
floaters      = set()
hunters       = set()
specials      = set()

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, balls, hunters, floaters, pulsators, black_holes, specials
    running = False
    cycle_count = 0
    balls = set()
    floaters = set()
    black_holes = set()
    pulsators = set()
    hunters = set()
    specials = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running
    running = True
    update_all()
    display_all()
    running = False



#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(simulton_kind):
    global kind
    kind = simulton_kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if kind != "Remove":
        simulton = eval("%s(%s, %s)" % (kind,x, y))
        add(simulton)
    else:
        simultons = balls|pulsators|hunters|specials|black_holes|floaters
        for simulton in simultons:
            if simulton.contains((x,y)):
                remove(simulton)
        


#add simulton s to the simulation
def add(s):
    simulton_type = type_as_str(s)
    if simulton_type == "ball.Ball":
        balls.add(s)
    elif simulton_type == "floater.Floater":
        floaters.add(s)
    elif simulton_type == "blackhole.Black_Hole":
        black_holes.add(s)
    elif simulton_type == "pulsator.Pulsator":
        pulsators.add(s)
    elif simulton_type == "hunter.Hunter":
        hunters.add(s)
    elif simulton_type == "special.Special":
        specials.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simulton_type = type_as_str(s)
    if simulton_type == "ball.Ball":
        balls.remove(s)
    elif simulton_type == "floater.Floater":
        floaters.remove(s)
    elif simulton_type == "blackhole.Black_Hole":
        black_holes.remove(s)
    elif simulton_type == "pulsator.Pulsator":
        pulsators.remove(s)
    elif simulton_type == "hunter.Hunter":
        hunters.remove(s)
    elif simulton_type == "special.Special":
        specials.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    simultons = balls|pulsators|hunters|specials|black_holes|floaters
    res = set()
    for simulton in simultons:
        if p(simulton):
            res.add(simulton)
    return res


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        eaten = set()
        cycle_count += 1
        for ball in balls:
            ball.update()
        for floater in floaters:
            floater.update()
        for black_hole in black_holes:
            eaten = eaten | black_hole.update()
        for pulsator in pulsators:
            eaten = eaten | pulsator.update()
        for hunter in hunters:
            eaten = eaten | hunter.update()
        for special in specials:
            special.update()
        for prey in eaten:
            remove(prey)


#delete from the canvas each simulton in the simulation; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for ball in balls:
        ball.display(controller.the_canvas)
    
    for floater in floaters:
        floater.display(controller.the_canvas)

    for black_hole in black_holes:
        black_hole.display(controller.the_canvas)

    for pulsator in pulsators:
        pulsator.display(controller.the_canvas)

    for hunter in hunters:
        hunter.display(controller.the_canvas)

    for special in specials:
        special.display(controller.the_canvas)

    simultons = balls|floaters|black_holes|pulsators|hunters|specials
    controller.the_progress.config(text=str(cycle_count)+" cycles/" + str(len(simultons))+"simultons")
