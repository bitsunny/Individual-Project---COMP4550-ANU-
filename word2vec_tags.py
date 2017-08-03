import gensim.models.word2vec as w2v

# import the EXCEL library
import xlrd
import re

class MySentences(object):
    def __init__(self, alltags_sentences):
        self.alltags_sentences = alltags_sentences

    def __iter__(self):
        for fn in self.alltags_sentences:
            with open(fn, 'r') as f:
                for line in f:
                    yield line.split()


## sentences = MySentences('/Users/songshuaichen/Desktop/alltags_sentences.txt')  # a memory-friendly iterator
##myModel = w2v(sentences)


words = []
alltags = []
processed_category = {}
allcategory_grouping = []
sentences = []
sets = []

def read_file(file):

    for i in range(len(file)):
        file[i] = '/media/gm/系统/mm/word2vec/' + file[i]
        # file[i] = '/home/gm/Downloads/word2vec/' + file[i]

    global words
    global alltags
    global processed_category
    global allcategory_grouping

    alltags_F = open(file[0], "r")
    processed_category_F = open(file[1], "r", encoding = 'gbk') # avoid the encoding problem
    allcategory_grouping_F = xlrd.open_workbook(file[2])
    words_F = open(file[3], "r")



    while True:
        line = alltags_F.readline()
        if not line:
            break
        alltags.append(line[:-1])
    print("alltags_finished")

    while True:
        line = processed_category_F.readline()
        if not line:
            break
        temp = line.split('\t')
        processed_category[temp[0]] = temp[1]

    print("processed_category_finished")

    table = allcategory_grouping_F.sheets()[0]

    for i in range(table.ncols):
        allcategory_grouping.append(table.col_values(i))
    print("allcategory_grouping_finished")


    while True:
        line = words_F.readline()
        if not line: break
        temp = line.split(' ')
        words.append(temp[0])
    print("words_finished")

def model_compare(model, word):
    tags = []
    try:
        for w in model.most_similar(word):

            tags.append(w[0])
    except KeyError:
        print(word + " is not in the model!-------------------------------------------------------------------")
        return []

    return tags

def inTags(tags):

    global alltags
    filtered_tags = []

    for i in tags:
        if i in alltags:
            filtered_tags.append(i)
    return filtered_tags



def find_category(tags):

    global processed_category
    cat_dic = {}

    for i in tags:
        try:
            cat_dic[i] = processed_category[i]
        except KeyError:
            continue
    return cat_dic

def grouping(category_i, cat_dic):

    global allcategory_grouping

    target = []
    related_tags = []

    for i in allcategory_grouping:

        if category_i in i:
            target = i
            break

    for j in cat_dic.keys():
        if cat_dic[j] in target:
            related_tags.append(j)
    return related_tags

sentences = []

def read_sentence(path):

	global sentences

	file = open(path, 'r')
	while True:
		line = file.readline()
		if not line:
			break
		temp = line.split('\t')
		sentences.append(temp[1])

	for i in sentences:
		print(i)

def sentences_divided():



if __name__ == "__main__":
    model = w2v.Word2Vec.load('myModel')

    read_file(['alltags.txt','processed_category.txt','allCategory_grouping.xlsx','a.txt'])

    read_sentence('/home/gm/Downloads/tagWiki.txt')

    no_category = 0
    no_word = 0

    global sets

    for i in words:
        try:
            category_i = processed_category[i]
        except KeyError:
            ## print(i+ "  has no category!*****************************")
            no_category += 1
            continue
        tags_1 = model_compare(model, i)
        if tags_1 == []:
            continue
        tags_2 = inTags(tags_1)
        cat_dic = find_category(tags_2)
        related_tags = grouping(category_i, cat_dic)

        if related_tags != []:

            related_tags.append(i)
            sets.append(related_tags)

        else:
            no_word += 1

    print("no category: " + str(no_category))
    print("no word: " + str(no_word))

    for i in sets:
        print(str(i))


    # get the word vector


        #print model.similarity('java', 'javascript')

        #language_vec = model["c#"]
        #print type(language_vec)
        #print language_vec


