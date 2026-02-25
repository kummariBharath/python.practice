class HashTable:
    collection={}
    def hash(self,string:str):
        hash=0
        for char in string:
            hash+=ord(char)
        return hash

    def add(self, key, value):
        hash_value = self.hash(key)
        self.collection[hash_value] = {key: value} # Store the key-value pair in the collection using the hash value as the key,key:value are values of the hash table