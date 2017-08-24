def main():
    loop = True
    while loop:
        goal = input("Enter the desired goal cell number:")
        if not goal.isdigit():
            print("Incorrect value, try again")
        else:
            goal = int(goal)
            if goal <= 0:
                print("Incorrect value, try again")
            else:
                loop = False
    directions = get_directions(goal)
    die = {"TOP":3, "FRONT":2, "LEFT":6, "RIGHT":1, "BOTTOM":4, "BACK":5}
    LR = ["LEFT", "TOP", "RIGHT", "BOTTOM"]
    FB = ["FRONT", "TOP", "BACK", "BOTTOM"]
    for direction in directions:
        LR_VALUE = [die[key] for key in LR]
        FB_VALUE = [die[key] for key in FB]
        if direction == "RIGHT":
            LR_VALUE = LR_VALUE[-1:] + LR_VALUE[:-1]
            die.update(dict(zip(LR, LR_VALUE)))
        elif direction == "FORWARD":
            FB_VALUE = FB_VALUE[1:] + FB_VALUE[:1]
            die.update(dict(zip(FB, FB_VALUE)))
        elif direction == "LEFT":
            LR_VALUE = LR_VALUE[1:] + LR_VALUE[:1]
            die.update(dict(zip(LR, LR_VALUE)))
        elif direction == "BACKWARD":
            FB_VALUE = FB_VALUE[-1:] + FB_VALUE[:-1]
            die.update(dict(zip(FB, FB_VALUE)))
    print("On cell {}, {} is at the top, {} at the front, and {} on the right.".format(goal, die["TOP"], die["FRONT"], die["RIGHT"]))
    return die



def get_directions(goal):
    if goal == 1:
        return []
    directions = ["RIGHT", "FORWARD", "LEFT", "BACKWARD"]
    result = []
    index = 0
    number = 1
    while len(result) < goal:
        result.extend([directions[index]]*number)
        index = (index+1)%4
        result.extend([directions[index]]*number)
        index = (index+1)%4
        number += 1
    result = result[:goal-1]
    return result



if __name__ == "__main__":
    main()