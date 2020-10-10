# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import operator

// Space O(n)  and time O(n)
def yahtzee(dice_roll):
    dmap = {key:0 for key in range(1,7)}
    for num in dice_roll:
        dmap[num] += num
    return max(dmap.items(), key=operator.itemgetter(1))[1]
print(yahtzee([2, 3, 5, 5, 6]))

// Space O(1)  and time O(n)
def yahtzee2(dice_roll):
    cm, pm = 0, 0
    index = 0
    for num in dice_roll:
        if index == 0:
            cm += num
        elif num == dice_roll[index-1]:
            cm += num
        elif num != dice_roll[index-1] and cm > pm:
            pm = cm
            cm = num
        elif num != dice_roll[index-1] and cm < pm:
            cm = num
        index += 1
    return max(pm, cm)
print(yahtzee2([2, 3, 5, 5, 6]))
