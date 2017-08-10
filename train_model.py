import gensim.models as gm
import os

#wordList = []
#model = w2v.Word2Vec([['Paris', 'is', 'the', 'captial', 'of','France'],['Beijing', 'is', 'the', 'captial', 'of','China']], size=50, window=4, min_count=1, workers=4)
#print model.wv.most_similar(positive=['Paris', 'France'], negative=['Beijing'])

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences('F:/training_set_quadgram')  # a memory-friendly iterator

model = gm.word2vec.Word2Vec(sentences, size = 200, window = 5, min_count = 20, workers = 8)
model.save('F:/model_quadgram_normal/myModel')

model = gm.word2vec.Word2Vec(sentences, size = 200, window = 5, min_count = 50, workers = 8)
model.save('F:/model_quadgram_version/myModel')

