"""
BEFORE and AFTER HOOKS - Continuing with unit tests. Here are some features we 
get with unittest that are useful when testing larger apps. Often you have 
to run code before/after all of your tests. For example, maybe you need to:

adding data to a DB, 
creating fake data, 
creating a fake user account, etc. 

Rather than re-creating this fake user account in every single test function,
you want it to be available everywhere. Can do this by using setUp and tearDown.

setUp and tearDown
- For larger applications, you may want similar application state BEFORE
    running tests so you put that in setUp
- Similarly, if you have code you want to run AFTER all of your tests
    (e.g., usually needed when working with a DB, you've added a bunch of fake
    data for your tests), then you call tearDown to remove all that data.
- Common use cases: adding/removing data from a test DB, creating instances
    of a class that you're going to reuse (in a DB or not)

Example:

class SomeTests(unittest.TestCase):

    def setUp(self):
        # do setup here
        pass

    def test_first(self):
        # setUp runs before
        # tearDown runs after
        pass

    def test_second(self):
        # setUp runs before
        # tearDown runs after
        pass
    
    def tearDown(self):
        # do teardown here
        pass



"""