import unittest
from Backend.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.data = [16, "1","Harry"]
        self.db = Database()

    def test_insert(self):
        query = "insert into department ( id, dep_code, name) values (%s,%s,%s)"
        val = self.data
        a = self.db.insert(query,val)
        query = "select * from department where id = 16"
        b = self.db.select(query)
        c = []
        for i in b[0]:
            c.append(i)
        actual = c
        print(c)
        expect = self.data
        self.assertEqual(expect,actual)