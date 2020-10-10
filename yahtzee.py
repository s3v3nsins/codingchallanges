# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import operator

# Space O(n)  and time O(n)
def yahtzee(dice_roll):
    dmap = {key:0 for key in range(1,7)}
    for num in dice_roll:
        dmap[num] += num
    return max(dmap.items(), key=operator.itemgetter(1))[1]
print(yahtzee([2, 3, 5, 5, 6]))

# Space O(1)  and time O(n)
def yahtzee2(dice_roll):
    # current max, previos max
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
    # return max
    return max(pm, cm)
print(yahtzee2([2, 3, 5, 5, 6]))


from collections import defaultdict
import operator, time

# Space: O(n) & time O(n)
def yahtzee_bonus(file_name):
    f = open(file_name, 'r') 
    lines = f.readlines() 
    dmap = defaultdict()
    for line in lines:
      line = line.strip()
      if line in dmap.keys(): 
        dmap[line.strip()] += line.strip()
      else:
        dmap[line.strip()] = line.strip()
    return max(dmap.items(), key=operator.itemgetter(1))[1]
print(yahtzee_bonus("yahtzee-upper-1.txt"))


# def yahtzee_bonus2(nums):
#     dmap = defaultdict()
#     for num in nums:
#       if num in dmap.keys(): 
#         dmap[num] += num
#       else:
#         dmap[num] = num
#     return max(dmap.items(), key=operator.itemgetter(1))[1]
# print(yahtzee_bonus2([1654, 1654, 50995, 30864, 1654, 50995, 22747,
#     1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
#     30864, 4868, 30864]))
