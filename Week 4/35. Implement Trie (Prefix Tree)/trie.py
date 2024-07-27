class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for one_letter in word:
            if one_letter not in cur:
                cur[one_letter] = {}
            cur = cur[one_letter]

        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root

        for one_letter in word:
            if one_letter not in cur:
                return False
            cur = cur[one_letter]

        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for one_letter in prefix:
            if one_letter not in cur:
                return False
            cur = cur[one_letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
