import unittest

def is_older_than_18(age):
    if age >= 18:
        return True
        # return False  #throws error
    else:
        return False
    

class WhiteBoxTest(unittest.TestCase):
    
    def test_is_older_than_18(self):
        age = 20
        result = is_older_than_18(age)
        self.assertEqual(result, True)

    def test_is_younger_than_18(self):
        age = 16
        result = is_older_than_18(age)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()


''' White Box Testing
White Box Testing assumes that the tester has access to the source code of the program and can examine the internal logic of the program. The tester can then use this knowledge to create test cases that will exercise the internal logic of the program. This is in contrast to black box testing, where the tester does not have access to the source code of the program and must rely on the program's external behavior to create test cases.
'''