#!usr/bin/env python3
#
# Author: August Frisk
# Course: CSci 270 - Fall 2017
# Assignment: Lab 04
# Filename: personality_type.py
#
# Pargraphs Author: Professor Dale Phillips
# Author URL:  https://github.com/phillipsd
#
# Description: A program which provides a "unique personality type" determined
#              from user input.  The user inputs an integer, and recieves a
#              predetermined response.  If the input is out of the given range,
#              or an invalid type, the prgram displays an error message.
#

paragraph_1 = """
THE ORIGINATOR 1's are originals. Coming up with new ideas and executing them is
natural. Having things their own way is another trait that gets them as being
stubborn and arrogant. 1's are extremely honest and do well to learn some
diplomacy skills. They like to take the initiative and are often leaders or
bosses, as they like to be the best. Being self-employed is definitely helpful
for them. Lesson to learn: Others' ideas might be just as good or better and to
stay open minded.

Famous 1's: Tom Hanks, Robert Redford, Hulk Hogan, Carol Burnett, Wynona Judd,
Nancy Reagan, Raque l Welch.
"""

paragraph_2 = """
THE PEACEMAKER 2's are the born diplomats. They are aware of others' needs and
moods and often think of others before themselves. Naturally analytical and very
intuitive they don't like to be alone. Friendship and companionship is very
important and can lead them to be successful in life, but on the other hand
they'd rather be alone than in an uncomfortable relationship. Being naturally
shy they should learn to boost their self-esteem and express themselves freely
and seize the moment and not put things off.

Famous 2's: President Bill Clinton, Madonna, Whoopee Goldberg, Thomas Edison,
Wolfgang Amadeus Mozart.
"""

paragraph_3 = """
THE LIFE OF THE PARTY 3's are idealists. They are very creative, social,
charming, romantic, and easygoing. They start many things, but don't always see
them through. They like others to be happy and go to great lengths to achieve
it. They are very popular and idealistic. They should learn to see the world
from a more realistic point of view.

Famous 3's: Alan Alder, Ann Landers, Bill Cosby, Melanie Griffith,
Salvador Dali, Jodi Foster.
"""

paragraph_4 = """
THE CONSERVATIVE 4's are sensible and traditional. They like order and routine.
They only act when they fully understand what they are expected to do. They like
getting their hands dirty and working hard. They are attracted to the outdoors
and feel an affinity with nature. They are prepared to wait and can be stubborn
and persistent. They should learn to be more flexible and to be nice to
themselves.

Famous 4's: Neil Diamond, Margaret Thatcher, Arnold Schwarzenegger, Tina Turner,
Paul Hogan, Oprah Winfrey.
"""

paragraph_5 = """
THE NONCONFORMIST 5's are the explorers. Their natural curiosity, risk taking,
and enthusiasm often land them in hot water. They need diversity, and don't like
to be stuck in a rut. The whole world is their school and they see a learning
possibility in every situation. The questions never stop. They are well advised
to look before they take action and make sure they have all the facts before
jumping to conclusions.

Famous 5's: Abraham Lincoln, Charlotte Bronte, Jessica Walter, Vincent Van Gogh,
Bette Midler, Helen Keller, Mark Hail.
"""

paragraph_6 = """
THE ROMANTIC 6's are idealistic and need to feel useful to be happy. A strong
family connection is important to them. Their actions influence their decisions.
They have a strong urge to take care of others and to help. They are very loyal
and make great teachers. They like art or music. They make loyal friends who
take the friendship seriously. 6's should learn to differentiate between what
they can change and what they cannot.

Famous 6's: Albert Einstein, Jane Seymour, John Denver, Meryl Streep,
Christopher Columbus, Goldie Hawn.
"""

paragraph_7 = """
THE INTELLECTUAL 7's are the searchers. Always probing for hidden information,
they find it difficult to accept things at face value. Emotions don't sway their
decisions. Questioning everything in life, they don't like to be questioned
themselves. They're never off to a fast start, and their motto is slow and
steady wins the race. They come across as philosophers and being very
knowledgeable, and sometimes as loners. They are technically inclined and make
great researchers uncovering information. They like secrets. They live in their
own world and should learn what is acceptable and what is not in the world at
large.

Famous 7's: William Shakespeare, Lucille Ball, Michael Jackson, Joan Baez,
Princess Diana.
"""

paragraph_8 = """
THE BIG SHOT 8's are the problem solvers. They are professional, blunt and to
the point, have good judgment and are decisive. They have grand plans and like
to live the good life. They take charge of people They viewpeople objectively.
They let you know in no uncertain terms that they are the boss! They should
learn to exude their decisions on their own needs rather than on what others
want.

Famous 8's: Edgar Cayce, Barbara Streisand, George Harrison, Jane Fonda, Pablo
Picasso, Aretha Franklin, Nostrodamus.
"""

paragraph_9 = """
THE PERFORMER 9's are natural entertainers. They are very caring and generous,
giving away their last dollar to help. With their charm, they have no problem
making friends and nobody is a stranger to them. They have so many different
personalities that people around them have a hard time understanding them. They
are like chameleons, ever changing and blending in. They have tremendous luck,
but also can suffer from extremes in fortune and mood. To be successful, they
need to build a loving foundation.

Famous 9's: Albert Schweitzer, Shirley MacLaine, Harrison Ford, Jimmy Carter,
Elvis Presley.
"""


print("Let's see what type of personality you have")
print("Pick a number and we'll tell you what makes you YOU!")

choice = int(input("Enter a number (1-9): "))


if choice == 1:
    print(paragraph_1)
elif choice == 2:
    print(paragraph_2)
elif choice == 3:
    print(paragraph_3)
elif choice == 4:
    print(paragraph_4)
elif choice == 5:
    print(paragraph_5)
elif choice == 6:
    print(paragraph_6)
elif choice == 7:
    print(paragraph_7)
elif choice == 8:
    print(paragraph_8)
elif choice == 9:
    print(paragraph_9)
else:
    print("Not a valid option")


if choice >= 1 and choice <= 9:
    print("Now you know what makes you YOU!")
else:
    print("An unknown error occured")
    print("We'll look into this...")
