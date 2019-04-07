
def count_word_frequency(doc):
    freq = {}
    for piece in open(doc).read().lower().split():
        word = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = freq.get(word, 0) + 1

    max_count = 0
    max_word = ''
    for w, c in freq.items():
        if c > max_count:
            max_word = w
            max_count = c

