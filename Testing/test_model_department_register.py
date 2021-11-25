import unittest
from Model_class.department_register import DepartmentRegistration


class TestDepartmentRegistration(unittest.TestCase):

    def setUp(self):
        self.o = DepartmentRegistration('M2',"Design")

    def test_get_code(self):
        actual = self.o.get_code()
        expect = "M2"
        self.assertEqual(expect,actual)

    def test_get_name(self):
        actual = self.o.get_name()
        expect = "Design"
        self.assertEqual(expect, actual)