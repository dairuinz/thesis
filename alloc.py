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

    alloc_df['processed'] = alloc_df['review'].map(lambda x: re.sub('[,\.!?]', '', x))
    alloc_df['processed'] = alloc_df['review'].map(lambda x: x.lower())

    from wordcloud import WordCloud

    long_string = ','.join(list(alloc_df['processed'].values))

    # wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    # wordcloud.generate(long_string)
    # wordcloud.to_image()
    #
    # plt.figure(figsize=(15, 8))  # size of graph
    # plt.imshow(wordcloud, interpolation='bilinear')  # puts wordcloud into image
    # plt.axis('off')  # no axis
    # plt.show()

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
    # pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]

    # print(alloc_df['processed'])
    # print(corpus[:1][0][:30])
    # print(len(corpus[:1][0][:30]))

    # pyLDAvis.enable_notebook()

    # vis = pyLDAvis.prepare(lda_model, corpus, id2word, mds='mmds', R=30)
    # print(vis)
    # vis
    #
    # plt.figure(figsize=(15, 8))  # size of graph
    # plt.imshow(vis, interpolation='bilinear')  # puts wordcloud into image
    # plt.axis('off')  # no axis
    # plt.show()

    return corpus
