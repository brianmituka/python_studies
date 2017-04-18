#!/usr/bin/env python

class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzz"
    def count_legs(self):
        print "I have %s legs" % self.number_of_legs



# doug = Pet()
# # doug.sleep()
# doug.number_of_legs = 4
# doug.count_legs()
#
# nemo = Pet()
# nemo.number_of_legs = 0
# nemo.count_legs()

# print "doug has %s legs." % doug.number_of_legs

class dog(pet):

    def bark(self):
        print "woof"
doug = dog()
doug.bark()
doug.sleep()
doug.number_of_legs= 4
doug.count_legs()
