import random

POKERS = ["Ace", "King", "Queen", "Jack", "10", "9"]


def play():
    # play poker game
    nums = get_poker([])
    nums.sort()
    pokers = translate(nums)
    print("The roll is: %s" % " ".join(pokers))
    hand = get_hands(nums)
    print("It is a %s" % hand)
    count = 0
    while True and count < 2:
        if count == 0:
            keeps = input("Which dice do you want to keep for the second roll?")
        else:
            keeps = input("Which dice do you want to keep for the third roll?")
        keeps = keeps.strip()
        if keeps  == "all" or keeps == "All":
            print("Ok, done")
            break
        keeps = keeps.split()
        keeps.sort()
        pokers.sort()
        if keeps == pokers:
            print("Ok, done")
            break
        valid = True
        for keep in keeps:
            if keep not in pokers:
                valid = False
                break
        if not valid:
            print("That is not possible, try again!")
            continue
        nums = get_poker(keeps)
        nums.sort()
        pokers = translate(nums)
        print("The roll is: %s" % " ".join(pokers))
        hand = get_hands(nums)
        print("It is a %s" % hand)
        count += 1

        


def is_valid(keeps, pokers):
    '''if the poker is valid'''
    valid = True
    for keep in keeps:
        if keep not in pokers:
            valid = False
    return valid


def translate(nums):
    '''translate num to pokers'''
    result = []
    for num in nums:
        result.append(POKERS[num])
    return result


def get_poker(keeps):
    '''get random pokers'''
    pokers = []
    for keep in keeps:
        pokers.append(POKERS.index(keep))
    while len(pokers) != 5:
        poker = random.randint(0, 5)
        pokers.append(poker)
    return pokers


def get_hands(nums):
    '''get the hand of the pokers'''
    nums_set = set(nums)
    if len(nums_set) == 1:
        return "Five of a kind"
    if len(nums_set) == 2:
        lst = list(nums_set)
        count1 = nums.count(lst[0])
        count2 = nums.count(lst[1])
        counts = [count1, count2]
        if 4 in counts:
            return "Four of a kind"
        else:
            return "Full house"
    if len(nums_set) == 3:
        lst = list(nums_set)
        count1 = nums.count(lst[0])
        count2 = nums.count(lst[1])
        count3 = nums.count(lst[2])
        counts = [count1, count2, count3]
        if 3 in counts:
            return "Three of a kind"
        else:
            return "Two pair"
    if len(nums_set) == 4:
        return "One pair"
    if len(nums_set) == 5:
        nums = list(nums_set)
        nums.sort()
        v = nums[-1] - nums[0]
        if v == 4:
            return "Straight"
        else:
            return "Bust"


def simulate(count):
    '''simulate the poker game'''
    hands = {"Five of a kind": 0, "Four of a kind": 0, "Full house": 0, "Straight": 0, "Three of a kind": 0,
             "Two pair": 0, "One pair": 0}
    for i in range(count):
        nums = get_poker([])
        nums.sort()
        pokers = translate(nums)
        hand = get_hands(nums)
        if hand != "Bust":
            hands[hand] += 1
    keys = ["Five of a kind", "Four of a kind", "Full house", "Straight", "Three of a kind", "Two pair", "One pair"]
    for key in keys:
        percent = hands[key]/count*100.0
        print("%s : %.2f%%" % (key, percent))
