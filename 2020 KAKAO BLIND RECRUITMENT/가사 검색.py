class Node:
    def __init__(self, data):
        self.data = data
        self.children = dict()
        self.words = set()


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node(ch)
            node = node.children[ch]
            node.words.add(word)

    def search(self, query):
        node = self.root
        for ch in query:
            if ch == '?':
                break

            if ch not in node.children:
                return 0

            node = node.children[ch]

        counter = 0
        for word in node.words:
            if len(word) == len(query):
                counter += 1
        return counter


def solution(words, queries):
    trie_prefix = Trie()
    trie_suffix = Trie()

    query_freq = dict()

    for word in words:
        if '?'*len(word) not in query_freq:
            query_freq['?'*len(word)] = 0
        query_freq['?'*len(word)] += 1

    for word in words:
        trie_prefix.insert(word)
        trie_suffix.insert(word[::-1])

    result = list()
    for query in queries:
        if query in query_freq:
            result.append(query_freq[query])
            continue

        if query[0] == '?':
            counter = trie_suffix.search(query[::-1])
        else:
            counter = trie_prefix.search(query)

        query_freq[query] = counter
        result.append(counter)

    return result


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    assert solution(words, queries) == [3, 2, 4, 1, 0]
