from pandas import Series, DataFrame
import pandas as pd
import re
import zhon.hanzi
import zhon.pinyin
from string import punctuation
import jieba

df_comment = pd.read_csv('comment.csv')
df_mk = df_comment[df_comment.mk==1]
df_ks = df_comment[df_comment.ks==1]

def remove_punctuation(text):
    a = ''.join(re.findall('[%s]' % zhon.hanzi.characters, text))
    return a

mk_words = list()
for row in df_mk.text:
    string = remove_punctuation(row)
    a = jieba.lcut(string)
    for ele in a:
        mk_words.append(ele)

ks_words = list()
for row in df_ks.text:
    string = remove_punctuation(row)
    a = jieba.lcut(string)
    for ele in a:
        ks_words.append(ele)

mk_words = Series(mk_words)
orders_mk = mk_words.value_counts()

ks_words = Series(ks_words)
orders_ks = ks_words.value_counts()

print(orders_mk[1:10], orders_ks[1:10])






