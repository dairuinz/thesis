import pandas as pd
import os
import re
import numpy as np

import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.max_columns', None)
# pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

def preprocessor():
    df1= pd.read_csv('reviews.txt', sep='----', engine='python', on_bad_lines='skip')
    df1 = df1.replace('<br/><br/>', '')
    df1 = df1.replace('<a class="a-link-normal" data-hook="product-link-linked" href="/hard-case-from-Caseling/dp/B00LZ3VFW8/ref=cm_cr_arp_d_rvw_txt?ie=UTF8">hard case from Caseling</a>', '')

    d = str(df1.columns)
    d = d.replace("Index(['~~~~~~~~~~~~~~~~~~", '')
    d = d.replace("'], dtype='object')", '')

    df1 = df1.reset_index()
    df1.columns = ['review', 'n']
    df1 = df1[pd.notnull(df1['review'])]
    df1 = df1.drop(['n'], axis=1)

    d = pd.Series(d)
    df1 = pd.concat([d, df1]).reset_index(drop=True)
    df1['review'][0] = df1[0][0]
    df1 = df1.drop([0], axis=1)

    df1['review'] = df1['review'].str.replace('a class="a-link-normal" data-hook="product-link-linked" href="/hard-case-from-Caseling/dp/B00LZ3VFW8/ref=cm_cr_arp_d_rvw_txt?ie=UTF8">', '')
    # re.sub('<[^>]+>', '', df1['review'])
    p = re.compile(r'<[^>]+>')
    df1['review'] = [p.sub('', x) for x in df1['review']]

    # print(df1.iloc[1] + df1.iloc[2] + df1.iloc[3])

    df1.iloc[1] = df1.iloc[1] + df1.iloc[2] + df1.iloc[3]
    df1 = df1.drop(df1.iloc[2].name)
    df1 = df1.drop(df1.iloc[2].name)

    df1 = pd.DataFrame.reset_index(df1)

    df1 = df1.drop(['index'], axis=1)
    df1.columns = ['review']

    df1['review'].replace('', np.nan, inplace=True)
    df1['review'].replace('The media could not be loaded.', np.nan, inplace=True)

    df1 = df1.dropna()

    df1 = pd.DataFrame.reset_index(df1)
    df1 = df1.drop(['index'], axis=1)
    df1.columns = ['review']

    # df1 = df1.drop(df1.iloc[112].name)
    # print(df1['review'][112])

    df1.iloc[265] = df1.iloc[265] + df1.iloc[266] + df1.iloc[267]
    df1 = df1.drop(df1.iloc[266].name)
    df1 = df1.drop(df1.iloc[266].name)

    # print(df1['review'][265])

    df1 = pd.DataFrame.reset_index(df1)
    df1 = df1.drop(['index'], axis=1)
    df1.columns = ['review']


    with open('stars.txt') as f:    # print(df2.stars)
    # print(df1['review'][99:150])
    # print(df2['stars'][99:150])
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

    # df = pd.concat([df1, df2], axis=1)


    # print(df[['review', 'stars']])

def prepend_line(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)