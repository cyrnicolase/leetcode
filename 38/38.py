#!/usr/bin/python

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        unit = [1]
        for i in range(1, n + 1):
            counter = 0
            item = None
            new_unit = []
            for j in range(0, len(unit)):
                if None == item:
                    item = unit[j]
                    counter += 1
                    continue

                if item == unit[j]:
                    counter += 1
                    continue
                
                new_unit.append(counter)
                new_unit.append(item)
                item = unit[j]
                counter = 1

            unit = new_unit

        return unit


so = Solution()
print so.countAndSay(4)


