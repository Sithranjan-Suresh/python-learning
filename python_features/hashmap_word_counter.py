"""
Problem: Word Frequency Counter Using Hashmap
---------------------------------------------
We implement a simple hashmap to count the occurrences of words.
1. Each bucket handles collisions using chaining (list of key-count pairs).
2. add_word(): adds a word or increments its count if it already exists.
3. count_words(): processes a list of words and updates counts.
4. display_counts(): returns a dictionary of word counts.
"""

class Hashmap:
    def __init__(self):
        self.MAX = 10  # Number of buckets
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        """
        Compute hash based on sum of character ordinals
        """
        return sum(ord(c) for c in key) % self.MAX

    def add_word(self, key):
        """
        Add a word to the hashmap or increment its count if it already exists
        """
        the_hash = self.get_hash(key)
        for item in self.arr[the_hash]:
            if item[0] == key:
                item[1] += 1
                return
        # Word not found, append with count 1
        self.arr[the_hash].append([key, 1])

    def count_words(self, words):
        """
        Count all words in a list
        """
        for word in words:
            self.add_word(word)

    def display_counts(self):
        """
        Return a dictionary of word counts
        """
        result = {}
        for bucket in self.arr:
            for word, count in bucket:
                result[word] = count
        return result

# ------------------ DEMO ------------------
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_count = Hashmap()
word_count.count_words(words)

print(word_count.display_counts())
# Expected output: {'apple': 3, 'banana': 2, 'orange': 1}
