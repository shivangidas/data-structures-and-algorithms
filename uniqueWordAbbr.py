#Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
#A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hmap = collections.defaultdict(list)
        for word in dictionary:
            if len(word) >= 3:
                key = word[0] + str(len(word[1:-1])) + word[-1]
                self.hmap[key].append(word)

    def isUnique(self, word: str) -> bool:
        if len(word) >= 3:
            key = word[0] + str(len(word[1:-1])) + word[-1]
            if key in self.hmap:
                if word in self.hmap[key] and len(self.hmap[key]) == 1:
                    return True
                else:
                    return False
            return True
        else:
            return True
            
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)            
#["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]
#[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]
