from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle, random.randint

#random.shuffle(alist) mutates its alist argument into a random permutation
#random.randint(1,10)  returns random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d', 'a', 'b', 'd', 'c', 'b', 'd']
        self.bag = Bag(self.alist)

    def test_len(self):
        self.assertEqual(len(self.bag), 7)
        random.shuffle(self.alist)
        for index, value in enumerate(self.alist):
            self.bag.remove(value)
            self.assertEqual(len(self.bag), 7-index-1)

    def test_unique(self):
        self.assertEqual(self.bag.unique(), 4)
        random.shuffle(self.alist)
        for index, value in enumerate(self.alist):
            self.bag.remove(value)
            self.assertEqual(self.bag.unique(), len(self.bag.counts))

    def test_contains(self):
        for item in ["a", "b", "c", "d"]:
            self.assertIn(item, self.bag)
        self.assertNotIn('x', self.bag)

    def test_count(self):
        self.assertEqual(self.bag.count('a'), 1)
        self.assertEqual(self.bag.count('b'), 2)
        self.assertEqual(self.bag.count('c'), 1)
        self.assertEqual(self.bag.count('d'), 3)
        self.assertEqual(self.bag.count('x'), 0)
        random.shuffle(self.alist)
        for index, value in enumerate(self.alist):
            self.bag.remove(value)
            total = self.bag.count('a') + self.bag.count('b') + self.bag.count('c') + self.bag.count('d')
            self.assertEqual(total, 7-index-1)

    def test_equals(self):
        alist = [random.randint(1,10) for i in range(1000)]
        bag1 = Bag(alist)
        random.shuffle(alist)
        bag2 = Bag(alist)
        self.assertEqual(bag1, bag2)
        bag2.remove(alist[0])
        self.assertNotEqual(bag1, bag2)

    def test_add(self):
        alist = [random.randint(0,10) for i in range(1000)]
        bag1 = Bag(alist)
        random.shuffle(alist)
        bag2 = Bag()
        for value in alist:
            bag2.add(value)
        self.assertEqual(bag1, bag2)


    def test_remove(self):
        alist = [random.randint(0,10) for i in range(1000)]
        bag1 = Bag(alist)
        with self.assertRaises(ValueError):
            bag1.remove(62)
        bag2 = Bag(alist)
        random.shuffle(alist)
        for value in alist:
            bag2.add(value)
        for value in alist:
            bag2.remove(value)
        self.assertEqual(bag1, bag2)


if __name__ == "__main__":
    unittest.main()
