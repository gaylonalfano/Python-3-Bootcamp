'''
This is from an exercise challenge where we yield yes, no, yes, no, etc.
This stumped me but I learned a new operator called TERNARY OPERATOR.
Also know as CONDITIONAL EXPRESSION. It simply allows to test a condition
in a single line replacing the multi-line if-else making the code compact.


Resources:
https://www.webucator.com/how-to/how-do-ternary-operator-assignment-python.cfm
https://www.python.org/dev/peps/pep-0308/#adding-a-conditional-expression

SEQUENCE TERNARY OPERATOR:
answer = "no" if answer == "yes" else "yes"
Step 1. if answer == "yes"
Step 2. if True, answer set to 'no'
Step 3. otherwise if False, answer set to 'yes'

Another example from webscraping section while looking for a "Next" button url:
url = next_btn.find('a')['href'] if next_btn else None 

'''
# Incorrect since it's not infinite:
# def yes_or_no(times):
#     for n in range(times):
#         if n % 2 == 0:
#             yield 'yes'
#         else:
#             yield 'no'


# COLT'S SOLUTION
def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        answer = 'no' if answer == 'yes' else 'yes'

sample = yes_or_no()
print(next(sample))
print(next(sample))
print(next(sample))
print(next(sample))





'''
LONG discussion regarding these TERNARY OPERATORS

def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        answer = 'no' if answer == 'yes' else 'yes'

The task here is to create a function which returns a generator that will alternate between yielding "yes" and "no" indefinitely, when we call next() on it (see Colt's example code for this exercise in the Udemy editor).

Colt does this in his solution by setting answer = "yes" and initiating a while True: loop. Since the True boolean will always be true, the while loop will run indefinitely, since the condition is never false.

Inside the loop, we yield the answer ("yes") which prints when next() is called on the generator.

Then, to make sure the next value yielded is "no", we use a one-line if statement:

answer = "no" if answer == "yes" else "yes"
That conditional statement checks if  answer == "yes" , and if that is true, it will set it to  answer = "no".

If the answer isn't currently "yes", it will set it to "yes". That ensure that each time we call next() the "yes" and "no" values alternate between each other.

Let me know if you have additional specific questions about it.

Regards,
Zarko - I'm a Teaching Assistant working for Colt and I will be helping out on the Q&A boards. Colt will also still be around and actively participate in the community.



Mark as helpful
RV
Rajat  · 13 days ago 
Hi,

Did not understand the formatting of the conditional statement. The line to be executed if the condition is true is written before the actual if condition ( answer = "no" if answer == "yes" else "yes" )

Can you please elaborate this?

Can't this be written as :

if answer == 'yes':

    answer = no

else:

    answer = 'yes'

yield answer



Mark as helpful (1)
Zarko — Teaching Assistant  · 12 days ago 
Hello Rajat,

Thanks for the question.

Yes, that does the same thing and it will work well in this scenario also:

def yes_or_no():
    answer = "no"  # if you place your if/else logic first, then start with "no" here so "yes" gets yielded first
    while True:
        if answer == 'yes':
            answer = 'no'
        else:
            answer = 'yes'
        yield answer
In your example, you would start with answer = "no" so that "yes" gets yielded first as the exercise expects (because you first used the conditional if/else logic, and the yield statement after).

This would also work fine:

def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        if answer == 'yes':
            answer = 'no'
        else:
            answer = 'yes'


The "no" if answer == "yes" else "yes" line that you are wondering about is called a conditional expression (often also called the ternary operator). It simply allows to test a condition in a single line replacing the multiline if-else making the code compact.

This syntax first evaluates if answer == "yes"; if it is true, answer will be set to "no", otherwise if it the condition is false, answer will be set to "yes".

See these links:

https://www.webucator.com/how-to/how-do-ternary-operator-assignment-python.cfm

https://www.python.org/dev/peps/pep-0308/#adding-a-conditional-expression

Please let me know if you have any more questions.

Regards,
Zarko - I'm a Teaching Assistant working for Colt and I will be helping out on the Q&A boards. Colt will also still be around and actively participate in the community.

Mark as helpful (2)
AV
Ananth  · 12 days ago 
Thanks Zarko, that was a clear explanation. Thanks Rajat for pointing out the query more clearly.



Mark as helpful (1)
RV
Rajat  · 12 days ago 
Thank You Zarko,

Fantastic explanation.

I was not aware if such expressions exists in python. Since we normally end up having multiple if-else blocks on daily basis, usage of such expressions makes life very easy. Can you please suggest some sources where we could find similar stuff (not usually used but exist). Also is it possible to have a small video or may be a document in this course for this kind of stuff.

Thanks,

Rajat



Mark as helpful (1)
Zarko — Teaching Assistant  · 12 days ago 
You're welcome, Ananth and Rajat! Great to hear that the question has been cleared up.

Rajat,

You can find a number of these approaches and tips throughout the course (like we encounter the conditional expression in this exercise), just make sure to pay attention and research all the syntax and expressions that you encounter here, and you are curious to learn more about.

You can check the following link from Python's official website to find a detailed overview and reference for the programming language: https://docs.python.org/3/tutorial/

There is this great thread on stackoverflow.com I can highly recommend, I'm sure you will like it: https://stackoverflow.com/questions/101268/hidden-features-of-python

I will pass your feedback further, but as I said, most of these features are indeed already covered here!

Keep up the hard work.

Regards,
Zarko - I'm a Teaching Assistant working for Colt and I will be helping out on the Q&A boards. Colt will also still be around and actively participate in the community.

Mark as helpful (1)
AV
Ananth  · 6 days ago 
Thanks Zarko.

Just eager to know if there are any discounts to the Colt's new course i.e. JavaScript Algorithms and Data Structures Masterclass. I always wanted a course from Colt on JS since the time he thought Javascript in The Web Developer Bootcamp. I am his ardent follower, will I get some discount ? ???? 

Mark as helpful
Zarko — Teaching Assistant  · 6 days ago 
Hello Ananth,

Thanks for the question.

If you check the email that is associated with your Udemy account you should have received an email titled 'Udemy Instructor: Colt Steele' which has a launch discount coupon code for the new course (if you are enrolled in any of Colt's courses on this website).

But, the course is already discounted to its lowest price (as far as I've seen discounts go) without a coupon code, in a Udemy website-wide discount called 'Back-To-School Sale' which is ongoing for 6 more days, you will be able to find more details if you visit the new course page.

Regards,
Zarko - I'm a Teaching Assistant working for Colt and I will be helping out on the Q&A boards. Colt will also still be around and actively participate in the community.

Mark as helpful (1)
GA
Add an answer
Add an answer
 

Improve captions
Edit and submit for approval 


 



'''