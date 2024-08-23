class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur_depth = self.trie
        for char in word:
            if char not in cur_depth:
                cur_depth[char] = {}
            cur_depth = cur_depth[char]
        cur_depth['*'] = {}

    def search(self, word: str) -> bool:
        return self.dfs(word, self.trie)

    def dfs(self, word: str, cur_depth: dict) -> bool:
        if not word:
            return '*' in cur_depth.keys()
        if word[0] == '.':
            for char in cur_depth.keys():
                if self.dfs(word[1:], cur_depth[char]):
                    return True
            return False
        if word[0] not in cur_depth:
            return False
        return self.dfs(word[1:], cur_depth[word[0]])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
