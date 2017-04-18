from bunco_module import *

swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()

swapper_score = 0
loaded_dice_score =0

number_of_games = 100000
game_number = 0

print "simulation running"
print "-----------"

while game_number < number_of_games:
    swapper.roll()
    loaded_dice.roll()

    swapper.cheat()
    loaded_dice.cheat()

    print "cheater 1 rolled" + str(swapper.get_dice())
    print "cheater 2 rolled" + str(loaded_dice.get_dice())

    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
        print "Draw"
        pass
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
        print "dice swapper wins"
        swapper_score += 1
    else:
        print "loaded dice wins"
        loaded_dice_score += 1

    game_number += 1

print "simulation complete"
print "-------------------"
print "final scores"
print "------------"

print "swapper won " + str(swapper_score)
print "loaded dice won " + str(loaded_dice_score)

if swapper_score == loaded_dice_score:
    print "Game was Drawn"
elif swapper_score > loaded_dice_score:
    print "Swapper won most games"
else:
    print "Loaded dice won most games"
