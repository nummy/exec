import math
from decimal import Decimal


class similarity:
    def __init__(self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    def minkowksi(self, r):
        keys1 = set(self.ratings1.keys())
        keys2 = set(self.ratings2.keys())
        keys = keys1.intersection(keys2)
        x = []
        y = []
        for key in keys:
            x.append(self.ratings1[key])
            y.append(self.ratings2[key])
        value = sum(pow(abs(a - b), r) for a, b in zip(x, y))
        rv = 1 / float(r)
        return round(Decimal(value) ** Decimal(rv), 4)

    def pearson(self):
        keys1 = set(self.ratings1.keys())
        keys2 = set(self.ratings2.keys())
        keys = keys1.intersection(keys2)
        x = []
        y = []
        for key in keys:
            x.append(self.ratings1[key])
            y.append(self.ratings2[key])

        avg_x = sum(x)/len(x)
        avg_y = sum(y)/len(y)
        std_x = math.sqrt(sum([(item-avg_x)**2 for item in x])/len(x))
        std_y = math.sqrt(sum([(item-avg_y)**2 for item in y])/len(y))
        
        res = 0

        for i in range(len(x)):
            res += (x[i]-avg_x)*(y[i]-avg_y)/(std_x*std_y)
        return round(res/len(x),4)

    def manhattan(self):
        keys1 = set(self.ratings1.keys())
        keys2 = set(self.ratings2.keys())
        keys = keys1.intersection(keys2)
        x = []
        y = []
        for key in keys:
            x.append(self.ratings1[key])
            y.append(self.ratings2[key])
        res = 0
        for i in range(len(x)):
            res += abs(x[i]-y[i])
        return float(res)

    def euclidean(self):
        keys1 = set(self.ratings1.keys())
        keys2 = set(self.ratings2.keys())
        keys = keys1.intersection(keys2)
        x = []
        y = []
        for key in keys:
            x.append(self.ratings1[key])
            y.append(self.ratings2[key])
        res = 0
        for i in range(len(x)):
            res += (x[i]-y[i])**2
        return round(math.sqrt(res),4)

UserPRatings = {'Motorola': 8, 'LG': 5, 'Sony': 1,
                'Apple': 1, 'Samsung': 5, 'Nokia': 7, }
UserQRatings = {'Apple': 7, 'Samsung': 1,
                'Nokia': 4, 'LG': 4, 'Sony': 6, 'Blackberry': 3}


sm = similarity(UserPRatings, UserQRatings)
print(sm.pearson())
print(sm.minkowksi(3))
print(sm.manhattan())
print(sm.euclidean())
