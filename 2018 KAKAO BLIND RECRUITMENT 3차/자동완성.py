class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        current = self.root
        for character in word:
            if character not in current.children.keys():
                current.children[character] = Node(character)
            current = current.children[character]
            current.counter += 1

    def get_prefix(self, word):
        current = self.root
        prefix = ''
        for character in word:
            if prefix == word or current.counter == 1:
                break

            prefix += character
            current = current.children[character]

        return prefix


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    prefix_list = list()
    for word in words:
        prefix = trie.get_prefix(word)
        prefix_list.append(prefix)

    return sum([len(p) for p in prefix_list])


if __name__ == "__main__":
    assert solution(['go', 'gone', 'guild']) == 7
    assert solution(['abc', 'def', 'ghi', 'jklm']) == 4
    assert solution(['word', 'war', 'warrior', 'world']) == 15
