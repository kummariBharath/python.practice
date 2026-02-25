class HashTable:
    collection={}
    def hash(self,string:str):
        hash=0
        for char in string:
            hash+=ord(char)
        return hash

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        return None