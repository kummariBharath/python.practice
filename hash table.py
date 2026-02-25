class HashTable: # Define the HashTable class
    def __init__(self):
        self.collection={} # Initialize the collection dictionary to store key-value pairs

    def hash(self,string:str): # Define the hash method that takes a string key
        hash=0 # Initialize the hash value to 0
        for char in string: # Iterate through each character in the input string
            hash+=ord(char) # Add the ASCII value of the character to the hash sum
        return hash # Return the calculated hash value

    def add(self, key, value): # Define the add method to insert a key-value pair
        hash_value = self.hash(key) # Compute the hash value for the given key
        if hash_value not in self.collection: # Check if the hash value already exists in the collection
            self.collection[hash_value] = {} # If not, create a new nested dictionary for this hash
        self.collection[hash_value][key] = value # Store the key-value pair in the nested dictionary

    def remove(self, key): # Define the remove method to delete a key-value pair
        hash_value = self.hash(key) # Compute the hash value for the key
        if hash_value in self.collection and key in self.collection[hash_value]: # Check if the key exists in the collection
            del self.collection[hash_value][key] # Remove the key-value pair from the nested dictionary

    def lookup(self, key): # Define the lookup method to retrieve a value by key
        hash_value = self.hash(key) # Compute the hash value for the key
        if hash_value in self.collection and key in self.collection[hash_value]: # Check if the key exists
            return self.collection[hash_value][key] # Return the value associated with the key
        return None # Return None if the key is not found
    

my_hash_table = HashTable() # Create an instance of the HashTable class
my_hash_table.add("name","bharath") # Add a key "name" with value "bharath"
my_hash_table.add("age",20) # Add a key "age" with value 20
print(my_hash_table.lookup("name")) # Look up the key "name" and print the result