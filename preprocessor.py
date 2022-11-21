import pandas as pd
import os
import re
import numpy as np

import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.max_columns', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)

def preprocessor():
    with open("reviews.txt", 'r') as r, open('reviews2.txt', 'w') as o:
        for line in r:
            # strip() function
            if line.strip():
                o.write(line)
    f = open("reviews2.txt", "r")
    # print("New text file:\n", f.read())

    with open('reviews.txt') as f:    # print(df2.stars)
        fl = f.readline().strip()
        if (fl == 'reviews'):
            pass
        else:
            prepend_line("reviews2.txt", "reviews")  # puts 'stars' at first line

    df1 = pd.read_csv('reviews2.txt')
    df1.columns = ['reviews']

    with open('stars.txt') as f:    # print(df2.stars)
        fl = f.readline().strip()
        if (fl == 'stars'):
            pass
        else:
            prepend_line("stars.txt", "stars")  # puts 'stars' at first line

    df2 = pd.read_csv('stars.txt')
    df2.columns = ['stars']

    # print(df1.head())
    # print(df2.head())
    print(len(df1))
    print(len(df2))

    # df1.to_csv('reviews.csv', index=False)
    # df2.to_csv('stars.csv', index=False)

    return df1, df2

def merger(df1, df2):
    df = pd.concat([df1, df2], axis=1, ignore_index=True)
    df.columns = ['review', 'stars']

    names = []
    for i in range(10):
        names.append(df.stars[0])
    j=0
    for i in df.stars:
        j+=1
        if i.startswith('https'):
            for k in range(j-1):
                names.append(i)
            j=0

    # print(len(names))

    df = pd.DataFrame(names)
    df.columns = ['product']
    # print(len(df))

    df1 = df1[df1["review"].str.startswith("~~~~~~~~~~~~~~~~~~")==False]
    df1 = df1.drop(df1.iloc[0].name)
    df1 = df1.reset_index()
    df1.columns = ['n', 'review']
    df1 = df1.drop(['n'], axis=1)
    # print(len(df1))

    df2 = df2[df2["stars"].str.startswith("http")==False]
    df2 = df2.reset_index()
    df2.columns = ['n', 'stars']
    df2 = df2.drop(['n'], axis=1)
    # print(len(df2))

    df = pd.concat([df, df1], axis=1)
    df = pd.concat([df, df2], axis=1)
    # print(df)

    return df

def prepend_line(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)