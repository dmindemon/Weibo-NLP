import os,json
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

path_to_json = '/Users/shenguangmin/Desktop/ChineseNLP/comments/2015-08-29'
mk_keywords = ['MK','mk','Michael', 'Kors','michael','kors']
ks_keywords = ['Kate','Spade','kate','spade','ks','KS']

def get_df(path_to_json, mk_keywords, ks_keywords):
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    jsons_data = pd.DataFrame(columns=['user','gender','province','time','text'])

    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            user = json_text['user']['id']
            gender = json_text['user']['gender']
            province = json_text['user']['province']
            time = json_text['user']['created_at']
            text = json_text['text']
            jsons_data.loc[index] = [user, gender, province, time, text]
    n = 0
    length = len(jsons_data['text'])
    jsons_data['mk'] = Series(np.zeros(length))
    jsons_data['ks'] = Series(np.zeros(length))
    for t in jsons_data['text']:
        if any(w in t for w in mk_keywords):
            jsons_data['mk'][n]=1
        if any(w in t for w in ks_keywords):
            jsons_data['ks'][n]=1
        n = n + 1
    df = jsons_data[(jsons_data.mk!= 0)|(jsons_data.ks!=0)]
    return df

def get_dfs(path, mk_keywords, ks_keywords):
    folder_names = [folder for folder in os.listdir(path) if folder.startswith('2')]
    df = pd.DataFrame(columns=['user','gender','province','time','text','mk','ks'])

    for name in folder_names:
        df_new = get_df((comment_path+'/'+name),mk_keywords,ks_keywords)
        df = pd.merge(df,df_new,how='outer')
    return df

comment_path = '/Users/shenguangmin/Desktop/ChineseNLP/comments'

comment = get_dfs(comment_path, mk_keywords, ks_keywords)
comment.to_csv('comment.csv')





