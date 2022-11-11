import os
from pprint import pprint

import gensim
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import re, nltk, spacy, gensim

import warnings
warnings.filterwarnings("ignore")

def alloc(df):
    alloc_df = df.drop(['product'], axis=1)
    # print(alloc_df)

    alloc_df['review'] = [re.sub(r'\S*@\S*\s?', '', sent) for sent in alloc_df['review']]
    alloc_df['review'] = [re.sub(r'\s+', ' ', sent) for sent in alloc_df['review']]
    alloc_df['review'] = [re.sub(r"\'", "", sent) for sent in alloc_df['review']]

    # alloc_df['review'] = alloc_df['review'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
    #
    # from nltk.tokenize import RegexpTokenizer
    # tokenizer = RegexpTokenizer(r'\w+')
    #
    # # lower = alloc_df['review'].str.lower()
    # lower = alloc_df['review'].map(lambda x: x.lower())
    #
    # from stop_words import get_stop_words
    # en_stop = get_stop_words('en')
    #
    # for word in lower:
    #     for w in word.split():
    #         for k in en_stop:
    #             if k == w:
    #                 lower = lower.str.replace(str(w), '')
    # # print(type(lower))
    # print(lower)
    # lower = pd.DataFrame(lower)
    #
    # # tokens = lower.apply(lambda x: x.split())
    # tokens = lower.apply(lambda sentence: [tokenizer.tokenize(word) for word in sentence])
    # print(tokens)
    #
    # # for t in tokens:
    # #     print(t)
    # # print(tokens)
    # # filtered_sentence = [i for i in tokens if not i in en_stop]
    #
    # from nltk.stem.porter import PorterStemmer
    # p_stemmer = PorterStemmer()
    #
    # filtered_sentence = lower.apply(lambda x: x.split())
    # filtered_sentence = filtered_sentence.apply(lambda x: ' '.join([w for w in x if len(w) > 3]))
    #
    # # print(filtered_sentence)
    #
    # texts = filtered_sentence.apply(lambda sentence: [p_stemmer.stem(word) for word in sentence])
    #
    # # for t in texts:
    # #     print(t)
    # # print(texts)
    #
    # from gensim import corpora, models
    #
    # dictionary = corpora.Dictionary(texts)
    #
    # corpus = [dictionary.doc2bow(text) for text in texts]
    #
    # # print(corpus[0])
    #
    # ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=20)
    #
    # print(ldamodel.print_topics(num_topics=3, num_words=3))


    alloc_df['processed'] = alloc_df['review'].map(lambda x: re.sub('[,\.!?]', '', x))
    alloc_df['processed'] = alloc_df['review'].map(lambda x: x.lower())

    from wordcloud import WordCloud

    long_string = ','.join(list(alloc_df['processed'].values))

    wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    wordcloud.generate(long_string)
    wordcloud.to_image()

    plt.figure(figsize=(15, 8))  # size of graph
    plt.imshow(wordcloud, interpolation='bilinear')  # puts wordcloud into image
    plt.axis('off')  # no axis
    plt.show()

    import gensim
    from gensim.utils import simple_preprocess
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords

    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

    def sent_to_words(sentences):
        for sentence in sentences:
            yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))

    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    data = alloc_df['processed'].values.tolist()
    data_words = list(sent_to_words(data))

    data_words = remove_stopwords(data_words)

    # print(data_words[:1][0][:30])

    import gensim.corpora as corpora  # Create Dictionary
    id2word = corpora.Dictionary(data_words)  # Create Corpus
    texts = data_words  # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]  # View
    # print(corpus[:1][0][:30])

    from pprint import pprint
    num_topics = 5
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)
    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]
