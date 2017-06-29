# SHUAICHEN 2017
Tag Categorization Extraction for tagwiki

Libraries required:
  1. NLTK v3.0.5
  2. Stanford POS Tagger v3.4.1


###6.16-6.23
1.check the 1000 high frequency of tags data and the rate is 29/1000 (tagCategory_frequency.xlsx)
2.write the script to find the data of important category and high frequency (test_category.py and test_category.txt)
3.simplify all category to a single words and collect all catagory and grouping them(processed_category.txt, findAllCategory.py and allCategory_grouping.xlsx).

###6.24-6.29
1.regrouping category
2.stduy word2vec and try to train a model to find similiar words and word's vector
3.discuss with jixuan about operating big file which is about use time to change memory, but have not do it.
the file is word2vec_tags.py, train_t2v.txt and allcategory_grouping.exel
