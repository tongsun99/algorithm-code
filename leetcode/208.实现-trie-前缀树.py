#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        N = 500000
        self.son = [[0] * 26 for _ in range(N)]
        self.label = [False] * N
        self.idx = 0

    def insert(self, word: str) -> None:
        p = 0
        for char in word:
            if self.son[p][ord(char) - ord('a')] == 0:
                self.idx += 1
                self.son[p][ord(char) - ord('a')] = self.idx

            p = self.son[p][ord(char) - ord('a')]

        self.label[p] = True    

    def search(self, word: str) -> bool:
        p = 0
        for char in word:
            if self.son[p][ord(char) - ord('a')] == 0:
                return False
            p = self.son[p][ord(char) - ord('a')]
        return self.label[p]
        

    def startsWith(self, prefix: str) -> bool:
        p = 0
        for char in prefix:
            if self.son[p][ord(char) - ord('a')] == 0:
                return False
            p = self.son[p][ord(char) - ord('a')]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

