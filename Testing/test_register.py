import unittest
from Frontend.register import ViewEmployee


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.data = [4, 'harry', 'narayan', 'aaa', 'chaudhary', 'Male', '2008', 'Ktm', 98188888, 'Okay its fine']
        self.data2 = [1, 4, 6, 11, 345, 6, 3322, 45]
        self.data3 = [1, 4, 6, 6, 11, 45, 345, 3322]
        self.o = ViewEmployee

    def test_linear_search(self):
        expect = 11
        actual = self.o.linearsearch(self.data2, 11)
        self.assertEqual(expect, actual)

    def test_bubble_sort(self):
        expected = self.data3
        actual = self.o.b_sort_a(self.data2)
        self.assertEqual(expected,actual)
