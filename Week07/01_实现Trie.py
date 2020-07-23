# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
#  示例:
#
#  Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
#
#  说明:
#
#
#  你可以假设所有的输入都是由小写字母 a-z 构成的。
#  保证所有输入均为非空字符串。
#
#  Related Topics 设计 字典树


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:200 ms,击败了41.58% 的Python3用户 内存消耗:26.7 MB,击败了10.00% 的Python3用户
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_mark = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_mark] = self.end_mark

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end_mark in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
