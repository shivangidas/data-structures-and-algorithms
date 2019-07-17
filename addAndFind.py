#Design and implement a TwoSum class. It should support the following operations: add and find.

#add - Add the number to an internal data structure.
#find - Find if there exists any pair of numbers which sum is equal to the value.
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.hmap[number] = self.hmap.get(number, 0) + 1
        
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for c in self.hmap:
            diff = value - c
            if diff in self.hmap and self.hmap[diff] - (diff is c):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

#Custom test case
#["TwoSum","add","add","add","find","find"]
#[[],[1],[3],[5],[4],[7]]
