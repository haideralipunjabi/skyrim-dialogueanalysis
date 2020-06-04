# Python Script to make graphs
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

data=list(csv.reader(open('raw_data/data.csv','r'),delimiter='\t'))

data[0] = data[0][0:19]
df = pd.DataFrame(data[1:], columns =data[0])  

plugin_data = df.groupby(["PLUGIN"]).size().sort_values()
plugin_data = plugin_data.rename(lambda x: x.replace(".esm",""))
plt.figure(figsize=(14,10))
ax = plugin_data.plot.bar(title="No. of Dialogues per DLC", cmap="jet")
ax.set(xlabel="DLC", ylabel="Dialogues")
plt.savefig("out/graph.eps",format="eps")
