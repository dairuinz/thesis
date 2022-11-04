import pandas as pd
import os



def preprocessor():
    pd.set_option('display.width', 640)
    pd.set_option('display.max_columns', 24)

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

    df1['review'] = df1['review'].replace('<a class="a-link-normal" data-hook="product-link-linked" href="/hard-case-from-Caseling/dp/B00LZ3VFW8/ref=cm_cr_arp_d_rvw_txt?ie=UTF8">', '', regex=True)

    print(df1.head(5))


    with open('stars.txt') as f:
        fl = f.readline().strip()
        if (fl == 'stars'):
            pass
        else:
            prepend_line("stars.txt", "stars")  # puts 'stars' at first line

    df2 = pd.read_csv('stars.txt')
    df2.columns = ['stars']

    # print(df1.head(50))
    # print(df2.head(50))

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