'''
DEFINE WHAT IS OBJECT ORIENTED PROGRAMMING:
It's about using code to represent things in the world (car, deck of cards, casino, process, song, etc.)
The way we create these things in Python/code is by writing classes and objects. OOP is a method of
programming that attempts to model some process or thing in the world as a class or object.

CLASS - The schematics. A blueprint, recipe, specifications, etc. for OBJECTS. Classes can contain methods (functions) and
attributes (similar to keys in a dict).

Ex. Modeling users. Define a USER class and it is a blueprint for
every user we create. Say every user has a username, email, profile picture, etc. Then, we also provide/include
methods (functionality) inside of the USER class that says every user has a logout method, has a change profile pic
method, checkout method, etc. It's all about taking functionality and pieces of data (attributes) and
putting them together in a specification, so every user has this. Or, every playing card has a suit, number, color, etc.
So essentially it's a COOKIE CUTTER we can use to create the individual INSTANCES of that class. Classes are the
schematics. Objects are the instances of that class created using the recipe/schematic.

INSTANCE/OBJECTS - Objects that are constructed from a CLASS blueprint that contain their class's methods and properties.
Then when we use the term object or instance, it is an instance of a class. When create a LIST or DICT object,
it's based off of the dictionary class. If you type help(int), you'll see: class int(object)

Ex. When you do:  nums = [1, 2, 3]; This is creating an INSTANCE of the LIST class. type(nums) returns <class 'list'>



UNDERSTAND ENCAPSULATION AND ABSTRACTION
Why OOP? It doesn't unlock any functionality we didn't have before. You could still make a poker game in other
non-OOP languages. It's really just a human way of thinking and structuring your program. With OOP, the goal is
to ENCAPSULATE your code into logical, hierarchical groupings using CLASSES so that you can reason about your
code at the higher level.

Example, think of all the animal species we have. Take a common fox. Its species is Vupla Vuples, but it's also
part of the Genus "Vuplas", and it's Class is "Mammalia" and it's also related to the highest Domain "Eukarya"
The point is that you can have CLASSES that are related to other CLASSES (INHERITANCE). It doesn't just end
at the idea of organizing things.

OOP is just a nice thing we can do in our code. Just helps us to organize things and breaking things down.
You don't have to make any classes, functions, etc. - could do everything one line after another
(aka "Spaghetti Code").

Once we learn to define our own classes, we'll be able to take a giant application and break it down into
and ENCAPSULATE into individual CLASSES.

POKER GAME EXAMPLE:
We could have the following entities/classes:
-Game: All the functionality and data associated with the game.
-Player: Each player has info, profile, chips balance, bank balance, etc.
-Card: A suit, a value, a color
-Deck: Info about the cards, number of cards,
-Hand: A poker hand would consist of multiple cards
-Chip: Value, size, color
-Bet: Value of a bet
-Team: Team names, number of players, players, etc.

LET'S LOOK AT THE DECK CLASS IN MORE DETAIL (Encapsulation/Pseudocode):
What are some of the possible things a deck of cards would need to have?
What sort of things does it need to do (methods)?

Deck {class}
-_cards -- A cards list                                     {private list attribute}
-_max_cards -- Sometimes you play with multiple decks.      {private int attribute}
-shuffle -- To mix the cards.                               {public method}
-deal_card -- Take one card off the top                     {public method}
-deal_hand -- Take 2, 3, or 5 cards and deal them.          {public method}
-count -- Count how many cards are left in that deck        {public method}


PRIVATE VS. PUBLIC
Some things don't need to be exposed to the programming outside world. Ex. could just stay
inside an individual deck. For example the list of cards. We don't need to access it directly,
we could access the list of cards through deal_card or deal_hand. Shuffle, count, deal_card and
deal_hand need to be "exposed" or made public. Note that Python doesn't officially have true public or
private variables or attributes or methods. The way you make something PRIVATE, you just put
"_" in front of the name (e.g., _cards, _max_cards).

ENCAPSULATION - The grouping of public and private attributes and methods into a programmatic class,
making abstraction possible. You want the fewest entries/exits out of the "bubble" (your class). Want to expose the bare minimum
the things we might need to use from another class or outside of the class.

Ex. Designing the Deck class, I make cards a private attribute (a list). I decide that the length of
the cards should be accessed via a public method called count() -- i.e., Deck.count(). This would give us
access to cards but more indirectly.

ABSTRACTION - The idea of exposing only the relevant data, or bare minimum, to create an interface, hiding
private attributes and methods (aka the "inner workings") from users. It's an interface to something more
complex (ex Deck: hide all the cards and just create little interfaces in to shuffle, deal, etc.).
Think of driving a car and using the steering wheel. Don't know how all the inner workings of the
steering wheel. We just turn the wheel (that's our interface) and it does everything else behind the
scenes, under the car, out of site basically. We only expose what is needed.

'''