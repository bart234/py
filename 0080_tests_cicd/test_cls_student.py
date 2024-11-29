import unittest
from cls_student import Student

class TestClsStudent(unittest.TestCase):
    
    def test_full_name(self):
        s1 = Student("Abba","Kowalczyk",3.4)
        self.assertEqual(s1.fullname, 'Abba Kowalczyk')
        s1.first = 'Beta'
        self.assertEqual(s1.fullname, 'Beta Kowalczyk')


if __name__ == '__main__':
    unittest.main()