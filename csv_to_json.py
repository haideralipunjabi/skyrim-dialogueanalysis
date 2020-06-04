# Python Script to extract RESPONSE TEXT & TOPIC TEXT from data.csv to output JSON files
import numpy as np
import csv
import pandas as pd
import json

import re
regex_string = "\<.+\>"

def regex_filter(s):
    return re.sub(regex_string,'',s)

data=list(csv.reader(open('raw_data/data.csv','r'),delimiter='\t'))

data[0] = data[0][0:19]
df = pd.DataFrame(data[1:], columns =data[0])  

data_rt = df.groupby(["RESPONSE TEXT"]).size().sort_values().to_dict()
data_tt = df.groupby(["TOPIC TEXT"]).size().sort_values().to_dict()

# To filter out some Constants or non dialogues from TOPIC TEXT
to_remove = []
data_tt = {regex_filter(k): v for k, v in data_tt.items()}

for key in data_tt.keys():
    if not key.__contains__(" ") and not key.__contains__(".") and not key.__contains__("?"):
        to_remove.append(key)
   
for key in to_remove:
    del data_tt[key]


json.dump(data_rt,open("output_data/out_rt.json","w"))
json.dump(data_tt,open("output_data/out_tt.json","w"))
