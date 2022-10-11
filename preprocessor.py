import pandas as pd
import os

def preprocessor():

    df1 = pd.read_csv('reviews.txt', sep='----', engine='python')


    df1.columns = ['review', 'n']
    df1 = df1[pd.notnull(df1['review'])]
    df1 = df1.drop(['n'], axis=1)
    df1 = df1.reset_index()


    with open('stars.txt') as f:
        fl = f.readline().strip()
        if (fl == 'stars'):
            pass
        else:
            prepend_line("stars.txt", "stars")  # puts 'stars' at first line

    df2 = pd.read_csv('stars.txt')
    df2.columns = ['stars']

    # print(df1)
    # print(df2)

    df = pd.concat([df1, df2], axis=1)


    print(df[['review', 'stars']])

def prepend_line(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)