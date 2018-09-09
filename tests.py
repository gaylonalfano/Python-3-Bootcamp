'''
You can also add docstrings to your tests (functions) so when you run the 
tests, you'll get a more descriptive printout by RUNNING:

NAME_OF_TEST_FILE.PY -v (verbose)

class SomeTests(unittest.TestCase):
    def first_test(self):
        """testing a thing"""
        self.assertEqual(thing(), "something")
    
    def second_test(self):
        """testing another thing"""
        self.assertEqual(another_thing(), "something else")


'''



# linked with activities - unittest
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a POSITIVE message for HEALTHY eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because it's healthy"
        )
    def test_eat_unhealthy(self):
        """eat should have a NEGATIVE message for UNHEALTHY eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )
    # testing for error using WITH
    # initially get: AssertionError: ValueError not raised - it's expecting a ValueError
    # therefore need to add logic in eat() method to check (see activities.py)
    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        """long napes should be discouraging"""
        self.assertEqual(
            nap(3),
            "Ugh. Didn't mean to nap for 3 hours"
        )
    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False)
        #self.assertFalse(expr=is_funny("tim"),msg="tim should not be funny")

    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    # Could test laugh noise but it will randomly pick something and return
    # but in our case there are only a few options
    def test_laugh(self):
        self.assertIn(laugh(), container=('lol', 'haha', 'tehehe'))



    

if __name__ == "__main__":
    unittest.main()

# test_eat_healthy (__main__.ActivityTests) ... ok
# test_eat_unhealthy (__main__.ActivityTests) ... ok
# test_long_nap (__main__.ActivityTests) ... ok
# test_short_nap (__main__.ActivityTests) ... ok




