import sys
sys.setrecursionlimit(30000)


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
        node.terminal = True

    def _search(self, node, index, query):
        data = query[index]

        counter = 0
        if data == '?':
            for word in node.words:
                if len(word) == len(query):
                    counter += 1
        else:
            if data not in node.children:
                return 0
            else:
                counter += self._search(node.children[data], index+1, query)

        return counter

    def search(self, query):
        node = self.root
        counter = self._search(node, 0, query)
        return counter


def solution(words, queries):
    trie_prefix = Trie()
    trie_suffix = Trie()
    query_info = dict()

    for word in words:
        if '?'*len(word) not in query_info:
            query_info['?'*len(word)] = 0
        query_info['?'*len(word)] += 1

    for word in words:
        trie_prefix.insert(word)
        trie_suffix.insert(word[::-1])
    result = list()
    for query in queries:
        if query in query_info:
            counter = query_info[query]
        else:
            if query.startswith('?'):
                counter = trie_suffix.search(query[::-1])
            else:
                counter = trie_prefix.search(query)
            query_info[query] = counter
        result.append(counter)
    return result


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    assert solution(words, queries) == [3, 2, 4, 1, 0]
