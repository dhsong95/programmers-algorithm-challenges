class Node:
    def __init__(self, data):
        self.data = data
        self.children = dict()
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node(ch)
            node = node.children[ch]
            node.counter += 1

    def get_prefix(self, word):
        node = self.root
        prefix = ''
        for ch in word:
            if prefix == word or node.counter == 1:
                break
            prefix += ch
            node = node.children[ch]

        return prefix


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    prefix_list = list()
    for word in words:
        prefix = trie.get_prefix(word)
        prefix_list.append(prefix)

    return sum([len(prefix) for prefix in prefix_list])


if __name__ == "__main__":
    assert solution(['go', 'gone', 'guild']) == 7
    assert solution(['abc', 'def', 'ghi', 'jklm']) == 4
    assert solution(['word', 'war', 'warrior', 'world']) == 15
