# Python Script to count & filter the words in the JSON files output by csv_to_json.py
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from progress.bar import Bar



gfile = open("raw_data/custom_stopwords.txt","r")
to_remove = [l.strip() for l in gfile.readlines()]
stopwords = stopwords.words('english')
stopwords.extend(to_remove)

data_rt = json.load(open("output_data/out_rt.json","r"))
data_tt = json.load(open("output_data/out_tt.json","r"))

data = {}

bar = Bar('Counting Response Text', max=len(list(data_rt.keys())))
for key in list(data_rt.keys()):
    tokens = word_tokenize(key)
    for word in tokens:   
        if word.lower() not in stopwords and word.isalpha():
            if word in data.keys():
                data[word] += data_rt[key]
            else:
                data[word] = data_rt[key]
    bar.next()
bar.finish()

bar = Bar('Counting Topic Text', max=len(list(data_tt.keys())))
for key in list(data_tt.keys()):
    tokens = word_tokenize(key)
    for word in tokens:   
        if word.lower() not in stopwords and word.isalpha():
            if word in data.keys():
                data[word] += data_tt[key]
            else:
                data[word] = data_tt[key]
    bar.next()
bar.finish()

data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
json.dump(data,open("output_data/count.json","w"))