from bunco_module import Player
from bunco_module import Cheat_Swapper
from bunco_module import Cheat_Loaded_Dice

cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

cheater1.roll()
cheater2.roll()

cheater1.cheat()
cheater2.cheat()

print "cheater 1 rolled " + str(cheater1.get_dice())
print "cheater 2 rolled " + str(cheater1.get_dice())

if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
    print "Draw"
elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
    print "cheater 1 wins"
else:
    print "cheater 2 wins"
