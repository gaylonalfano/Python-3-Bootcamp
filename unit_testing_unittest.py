"""
UNIT TESTING CONCEPT (outside of Python)
- Idea that you test the smaller components in isolation (units)
- Good candidates for unit testing: individual classes, modules, functions
- Bad candidates for unit testing: an entire application, dependencies
    across several classes or modules

UNITTEST - Is a testing framework, which means we forgo some flexibility
but get lots of powerful features. Python comes with a built-in 
module called unittest. You can write unit tests encapsulated as classes
that inherit from unittest.TestCase. This gives us a bunch of assertions 
we can use to test our code. The inheritance gives us access to assertion
helpers. You can run tests by calling unittest.main()


# TDD approach **Look at activities.py and tests.py
def eat(food, is_healthy):
    pass

def nap(num_hours):
    pass

# Then to setup unittest in another file tests.py:
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat(self):
        self.assertEqual(
            eat("broccoli", is_healthy=True),  # TDD Define the behavior you WANT
            "I'm eating broccoli because it is healthy"
            )
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza because YOLO!"
        )

if __name__ == "__main__":
    unittest.main()


TYPES OF ASSERTIONS: https://docs.python.org/3/library/unittest.html#classes-and-functions
self.assertEqual(x, y)  # x==y
self.assertNotEqual(x, y)  # x!=y
self.assertTrue(x)  # bool(x) is True - checking for Truth-y values
self.assertFalse(x)  # bool(x) is False - checking for False-y values
self.assertIsNone(x)
self.assertIsNotNone(x)
self.assertIn(x, y)
self.assertNotIn(x, y)


TESTING FOR ERRORS USING "WITH" KEYWORD - Can use self.assertRaises() to make 
sure that we get an error in a certain situation AND we can guarantee we get a 
certain TYPE of error. For example, let's say for our test_eat_healthy we want
to raise a ValueError if is_healthy is NOT a boolean:

def test_eat_healthy_boolean():
    '''is_healthy must be a bool'''
    with self.assertRaises(ValueError):
        eat("pizza", is_healthy="who cares?")

class SomeTests(unittest.TestCase):
    def testing_for_error(self):
        '''testing for an error'''
        with self.assertRaises(IndexError):
            l = [1, 2, 3]
            l[100]



"""