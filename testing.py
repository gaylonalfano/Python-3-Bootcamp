'''
OBJECTIVES:

DESCRIBE WHAT TESTS ARE AND WHY THEY ARE ESSENTIAL
Why test? - Reduce bugs in existing code. Ensure bugs that are fixed stay fixed.
Important especially when working with teams. Ensure new features don't break old ones!
Ensure that cleaning up code doesn't introduce new bugs. Makes development more fun!
Bummer is that it's a lot of additional code and takes time. Depends on the project.
Can save you a lot of time in the end.


EXPLAIN WHAT TEST DRIVEN DEVELOPMENT IS (TDD)
Idea that you FIRST write your tests and then write your code to make tests pass
Once the tests pass, a feature is considered complete! Yay! Note that this isn't
totally mainstream, but there are some big advocates. Totally up to you but maybe
not the right approach for EVERY occasion.

The mantra/workflow you practice with TDD:
RED - Very first thing you do is write tests that fail (eg. login())
GREEN - THEN, you write the MINIMAL amount of code necessary to make the test pass.
REFRACTOR - Clean up the code, while ensuring that tests still pass



TEST PYTHON CODE USING DOCTESTS



TEST PYTHON CODE USING ASSERT (NOT a function, it's a STATEMENT)
Assertions allow us to mkae simple assertions with the ASSERT keyword
assert accepts an expression. Returns NONE if the expression is truthy
Raises an ASSERTIONERROR if the expression is falsy.
Accepts an optional error message as a second argument. It used to be the end-all
for testing but there are better options now (unit tests, etc.) that we'll look
at later.

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

add_positive_numbers(1, 1)  # 2
add_positive_numbers(1, -1)  # AssertionError: Both numbers must be positive!

******  if not some_valid_expression: raise AssertionError() ******

Assertions Warning - This can all be overwritten using optimized mode (-O flag).
If it has the -O flag then assertions will NOT be evaluated!

Example, if I write in terminal:  python -O testing_assertions.py  then all of the
assert statements will be ignored!



EXPLAIN WHAT UNIT TESTING IS



WRITE UNIT TESTS USING THE UNITTEST MODULE



REMOVE CODE DUPLICATION USING BEFORE AND AFTER HOOKS


'''