import gensim.models.word2vec as w2v


class MySentences(object):
    def __init__(self, alltags_sentences):
        self.alltags_sentences = alltags_sentences

    def __iter__(self):
        for fn in self.alltags_sentences:
            with open(fn, 'r') as f:
                for line in f:
                    yield line.split()


sentences = MySentences('/Users/songshuaichen/Desktop/alltags_sentences.txt')  # a memory-friendly iterator
myModel = w2v(sentences)


if __name__ == "__main__":
    model = w2v.Word2Vec.load('/Users/songshuaichen/Downloads/myModel')

    # get the word vector
    for w in model.most_similar("java"):
        print w[0], w[1]

        print model.similarity('java', 'javascript')

        language_vec = model["c#"]
        print type(language_vec)
        print language_vec


