"""
Could create multiple tests testing say_name() without battery,
learn_skill with/without enough battery, whether the skill is IN
a predetermined list, or use some decorator to ensure that new_skill
isn't numeric, etc.

Notice that so far I've had to recreate the mega_man Robot instance
again and again for each test. You might think that adding a Class
variable that has mega_man would work, but if that variable gets changed
by any of the other testing functions, then all the subsequent tests
would be affected.

Better would be to use setUp() since it RERUNS the code every time before
it runs each function!

"""


import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        #self.mega_man = Robot("Mega Man", battery=50) - no longer needed w/ setUp
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        #self.mega_man = Robot("Mega Man", battery=50) - no longer needed w/ setUp
        self.assertEqual(
            self.mega_man.say_name(), 
            "BEEP BOOP BEEP BOOP. I AM MEGA MAN"
        )
        self.assertEqual(
            self.mega_man.battery,49)

    def test_say_name_low_battery(self):
        self.mega_man.battery = 0
        self.assertEqual(
            self.mega_man.say_name(),
            "Low power. Please charge and try again"
        )

    def test_learn_skill(self):
        self.mega_man.learn_skill("kung fu", 10)
        self.assertEqual(
            self.mega_man.battery, 40)
        self.assertEqual(
            self.mega_man.skills[-1], "kung fu")
        self.assertEqual(
            self.mega_man.learn_skill("kung fu", 10), 
            "WOAH. I KNOW KUNG FU"
        )

    def test_learn_skill_low_battery(self):
        self.assertEqual(
            self.mega_man.learn_skill("python", 99),
            "Insufficient battery. Please charge and try again"
        )
    
if __name__ == "__main__":
    unittest.main()

