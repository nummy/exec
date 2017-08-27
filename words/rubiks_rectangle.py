import sys
import copy

def get_digits():
    digits = input("Input final configuration:")
    digits = digits.replace(" ", "")
    if len(digits) != 8:
        print("Incorrect configuration, giving up...")
        sys.exit()
    temp = "".join(sorted(list(set(digits))))
    if temp != "12345678":
        print("Incorrect configuration, giving up...")
        sys.exit()
    first_part = digits[0:4]
    second_part = list(digits[4:])
    second_part.reverse()
    second_part = "".join(second_part)
    return first_part + second_part

def row_exchange(digits):
    return digits[4:] + digits[:4]

def circular_shift(digits):
    lst = list(digits)
    first = lst[:4]
    second = lst[4:]
    first = first[-1:] + first[:-1]
    second = second[-1:] + second[:-1]
    return "".join(first + second)

def clock_rotation(digits):
    lst = list(digits)
    first = lst[:4]
    second = lst[4:]
    temp = first[1] 
    first[1] = second[1]
    second[1] = second[2]
    second[2] = first[2]
    first[2] = temp
    return "".join(first + second)

def main():
    init_digits = "12348765" 
    final_digits = get_digits()
    print(final_digits)
    step = transform(init_digits, final_digits)
    print("%s steps are needed to reach the final configuration." % step)

def get_successors(init_digits):
    return [row_exchange(init_digits), circular_shift(init_digits), clock_rotation(init_digits)]


def transform(init_digits, final_digits):
    start = init_digits
    queue = []
    queue.append(start)
    visited = set()
    edgeTo = {}
    while len(queue) != 0:
        state = queue.pop(0)
        if state not in visited:
            visited.add(state)
            for successor in get_successors(state):
                if successor not in visited:
                    edgeTo[successor] = state
                    queue.append(successor)
    node =  edgeTo[final_digits]
    count = 1
    while node != init_digits:
        node = edgeTo[node]
        count += 1
    return count


if __name__ == "__main__":
    main()