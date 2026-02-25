# Hash Table Implementation

This document provides a step-by-step explanation of the Hash Table implementation found in `hash table.py`.

## 1. Class Structure

### The `HashTable` Class
This class manages the storage and retrieval of key-value pairs using a hashing mechanism.

```python
class HashTable:
    def __init__(self):
        self.collection = {}
```
*   **`class HashTable`**: Defines the blueprint for the hash table.
*   **`__init__`**: The constructor method that runs when a new object is created.
*   **`self.collection = {}`**: Initializes an empty dictionary for the specific instance to store data.

---

## 2. Methods Breakdown

### Hashing: `hash`
Converts a string key into a numerical index (hash value).
```python
def hash(self, string: str):
    hash = 0
    for char in string:
        hash += ord(char)
    return hash
```
*   **`hash = 0`**: Initializes the hash counter to 0.
*   **`for char in string:`**: Iterates through every character in the input key.
*   **`hash += ord(char)`**: Converts the character to its ASCII integer value and adds it to the sum.
*   **`return hash`**: Returns the final calculated integer.

### Adding Items: `add`
Inserts a new key-value pair into the table.
```python
def add(self, key, value):
    hash_value = self.hash(key)
    if hash_value not in self.collection:
        self.collection[hash_value] = {}
    self.collection[hash_value][key] = value
```
*   **`hash_value = self.hash(key)`**: Calculates the hash index for the given key.
*   **`if hash_value not in self.collection:`**: Checks if a bucket (nested dictionary) already exists for this hash.
*   **`self.collection[hash_value] = {}`**: If not, creates a new empty dictionary at that index.
*   **`self.collection[hash_value][key] = value`**: Stores the value in the nested dictionary. This handles **collisions** (different keys with the same hash) by chaining them in the same bucket.

### Removing Items: `remove`
Removes a key-value pair if it exists.
```python
def remove(self, key):
    hash_value = self.hash(key)
    if hash_value in self.collection and key in self.collection[hash_value]:
        del self.collection[hash_value][key]
```
*   **`hash_value = self.hash(key)`**: Computes the hash to find the bucket.
*   **`if ... in ...`**: Checks two things: 1) Does the bucket exist? 2) Is the key inside that bucket?
*   **`del ...`**: Deletes the specific key-value pair if found.

### Looking Up Items: `lookup`
Retrieves a value associated with a key.
```python
def lookup(self, key):
    hash_value = self.hash(key)
    if hash_value in self.collection and key in self.collection[hash_value]:
        return self.collection[hash_value][key]
    return None
```
*   **`hash_value = self.hash(key)`**: Computes the hash.
*   **`if ... in ...`**: Verifies the key exists in the correct bucket.
*   **`return ...`**: Returns the value if found.
*   **`return None`**: Returns `None` if the key is not in the table.