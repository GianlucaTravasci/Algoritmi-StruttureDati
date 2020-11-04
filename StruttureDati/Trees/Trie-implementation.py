class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return str(self.__dict__)

    def _character_index(self, char):
        if char.isupper():
            return ord(char) - ord('A')
        else:
            return ord(char) - ord('a')

    def insert(self, string):
        pointer = self.root
        for character in string:
            index = self._character_index(character)
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True
        return

    def search(self, string):
        pointer = self.root
        for character in string:
            index = self._character_index(character)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer and pointer.is_end_of_word


mytrie = Trie()
mytrie.insert('Data')
mytrie.insert('Structure')
mytrie.insert('And')
mytrie.insert('Algorithms')
print(mytrie.search('and'))
print(mytrie.search('asdasdaa'))
