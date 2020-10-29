class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for i in range(self.size)] #we init the hashtable like and array of length 'size' filled with value none

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the current character at key[i]
        return hash

    def set(self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])

    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return []

    def keys(self): #a function that returns all the keys in the list
        keysArray = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i])>1:
                    for j in range(len(self.data[i])):
                        keysArray.append(self.data[i][j][0])
                else:
                    keysArray.append(self.data[i][0][0])
        return keysArray

    def values(self):
        valuesArray = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i])>1:
                    for j in range(len(self.data[i])):
                        valuesArray.append(self.data[i][j][1])
                else:
                    valuesArray.append(self.data[i][0][1])
        return valuesArray

    def remove(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    self.data[hash].pop(i)
                    return None
        else:
            return None

    def modifyItem(self, key, newVal):
        hash = self._hash(key)
        reference = self.data[hash]
        if reference:
            for i in range(len(reference)):
                if reference[i][0] == key:
                    reference[i][1] = newVal

new_hash = HashTable(6)
new_hash.set('one', 1)
new_hash.set('one', 2)
new_hash.set('two', 2)
print(new_hash)
new_hash.remove('one')
print(new_hash)
new_hash.modifyItem('x', 'blabla')
print(new_hash)
print(new_hash.keys())
print(new_hash.values())

#print(new_hash)