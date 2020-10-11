# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import operator

# Space O(n) or almost O(1)  and time O(n)
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
            cm = num
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


import operator, time

# Space: O(n) & time O(n)
def yahtzee_bonus(file_name):
    start = time.time()
    f = open(file_name, 'r') 
    lines = f.readlines() 
    dmap = dict()
    for line in lines:
      line = int(line.strip())
      if line in dmap.keys(): 
        dmap[line] += line
      else:
        dmap[line] = line
    print("time is", time.time()-start )
    return max(dmap.items(), key=operator.itemgetter(1))[1]
print(yahtzee_bonus("yahtzee-upper-1.txt"))
# print(yahtzee_bonus("input.txt"))

def yahtzee_bonus2(nums):
    dmap = dict()
    for num in nums:
      if num in dmap.keys(): 
        dmap[num] += num
      else:
        dmap[num] = num
    return max(dmap.items(), key=operator.itemgetter(1))[1]
print(yahtzee_bonus2([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864]))

# Space: O(n) & time O(n)
# faster than yahtzee_bonus
def yahtzee_bonus3(file_name):
    start = time.time()
    f = open(file_name, 'r') 
    lines = f.readlines() 
    dmap = dict()
    for line in lines:
      line = int(line.strip())
      if line in dmap.keys(): 
        dmap[line] += 1
      else:
        dmap[line] = 1
    maxi = 0
    for k in dmap:
        maxi = max(maxi, int(k)*dmap[k])
    print("time is", time.time()-start )
    return maxi
print(yahtzee_bonus3("yahtzee-upper-1.txt"))
