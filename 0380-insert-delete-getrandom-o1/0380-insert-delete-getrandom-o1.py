import random

class RandomizedSet(object):

    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            return False
        self.data.append(val)
        self.index_map[val] = len(self.data) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index_map:
            return False
        last_element = self.data[-1]
        idx_to_remove = self.index_map[val]
        
        self.data[idx_to_remove] = last_element
        self.index_map[last_element] = idx_to_remove
        
        self.data.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)


