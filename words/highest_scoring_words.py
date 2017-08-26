import string
import sys

score_map = {"a": 2, "b": 5, "c": 4, "d": 4, "e": 1, "f": 6, "g": 5, "h": 5,
             "i": 1, "j": 7, "k": 6, "l": 3, "m": 5, "n": 2, "o": 3, "p": 5,
             "q": 7, "r": 2, "s": 1, "t": 2, "u": 4, "v": 6, "w": 6, "x": 7,
             "y": 5, "z": 7}


def get_letter():
    letter = input("Enter between 3 and 10 lowercase letters:")
    letter = letter.replace(" ", "")
    if not is_lowercase(letter):
        print("Incorrect input, giving up...")
        sys.exit()
    if len(letter) <= 2 or len(letter) > 10:
        print("Incorrect input, giving up...")
        sys.exit()
    return letter


def is_lowercase(letter):
    for char in letter:
        if char not in string.ascii_lowercase:
            return False
    return True


def get_score(word):
    total = 0
    for char in word:
        total += score_map[char]
    return total


def is_built_from_letter(word, letter):
    if len(word) > len(letter):
        return False
    word_set = set(word)
    letter_set = set(letter)
    if not word_set.issubset(letter_set):
        return False
    for char in word_set:
        count1 = word.count(char)
        count2 = letter.count(char)
        if count1 > count2:
            return False
    return True

def get_highest_score():
    letter = get_letter()
    fp = open("wordsEn.txt", "r")
    highest_score = 0
    highest_score_words = set()
    for line in fp:
        word = line.strip()

        if is_built_from_letter(word, letter):
            score = get_score(word)
            if score >highest_score:
                highest_score = score
                highest_score_words = set([word])
            if score == highest_score:
                highest_score_words.add(word)
    highest_score_words = list(highest_score_words)
    highest_score_words.sort()
    print("The highest score is %s." % highest_score)
    if len(highest_score_words) == 1:
        print("The highest scoring word is %s" % highest_score_words[0])
    else:
        print("The highest scoring words are, in alphabetical order:")
        for word in highest_score_words:
            print("\t" + word)



def main():
    get_highest_score()

if __name__ == "__main__":
    main()