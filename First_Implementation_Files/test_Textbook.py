import unittest
from Textbook import Textbook

class TestTexbook(unittest.TestCase):

    def setUp(self):
        # make copy of testbook for testing on
        self.tb1 = Textbook("testbooks/testbook1.txt")

    
    def test_initializations(self):
        # make sure all the things about all the Textbooks made in setUp are accurate
        self.assertEqual(self.tb1.name, "testbook1.txt")
        self.assertEqual(len(self.tb1.finished), 0)
        self.assertEqual(len(self.tb1.unfinished),11)
        print(self.getLengths(self.tb1.unfinished))
        print(self.tb1.unfinished["2.7"])
        self.assertCountEqual(self.getLengths(self.tb1.unfinished), [20,9,25,16,32,13,18,8,9,16,13])

    def tearDown(self):
        # delete copy of testbook
        x = 4

    

    def getLengths(self, dict):
        lengths = []
        for (k,v) in dict.items():
            lengths.append(len(v))
        return lengths
