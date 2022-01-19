#Design a HashSet without using any built-in hash table libraries.

#Implement MyHashSet class:

#1. void add(key) Inserts the value key into the HashSet.
#2. bool contains(key) Returns whether the value key exists in the HashSet or not.
#3. void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

#--- APPROACH----> Use a hash function that will store the values corresponding to different 'key' value in a list. And then add, delete or access elements from that list based on program requirements.

#-----SOLUTION----
class MyHashSet:

    def __init__(self):
        
        self.size = 100
        self.table = [None]*self.size
        
    def hash_val(self, key:int):
        return key% self.size
        

    def add(self, key: int) -> None:
        hv = self.hash_val(key)
        if self.contains(key):
            return
        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)
        

    def remove(self, key: int) -> None:
        hv = self.hash_val(key)
        if self.contains(key):
            self.table[hv].remove(key)
        

    def contains(self, key: int) -> bool:
        hv = self.hash_val(key)
        if self.table[hv] != None:
            return key in self.table[hv]
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)