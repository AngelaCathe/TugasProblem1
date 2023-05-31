class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        self.search_results = []

        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])

    def insert(self, sentence, time):
        node = self.root

        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def search(self, node, path):
        if node.is_word:
            self.search_results.append(path)

        for char, child in node.children.items():
            self.search(child, path + char)

    def autocomplete(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        self.search_results = []
        self.search(node, prefix)

        return self.search_results


# Contoh penggunaan
sentences = ["apple", "banana", "apple pie", "banana bread", "apple juice"]
times = [3, 2, 1, 1, 2]

autocomplete_system = AutocompleteSystem(sentences, times)

# Mencari penyelesaian otomatis berdasarkan prefix
print(autocomplete_system.autocomplete("app"))  # Output: ['apple', 'apple pie', 'apple juice']
print(autocomplete_system.autocomplete("ban"))  # Output: ['banana', 'banana bread']