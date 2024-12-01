"""
For example:

3   4
4   3
2   5
1   3
3   9
3   3
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
"""

with open("./part1.txt", encoding='utf-8') as file:
    data = file.read().splitlines()
    left, right = [], []
    for line in data:
      left.append(int(line.split()[0]))
      right.append(int(line.split()[1]))

    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
      total += abs(left[i] - right[i])
    print(total)