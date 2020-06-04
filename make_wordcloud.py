# Python Script to make WordClouds
import os
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import json

mask = np.array(Image.open("masks/Skyrim Logo.png"))
data = json.load(open("output_data/count.json","r"))

print(f"Diffrent Words: {len(data.keys())} | Total Words: {sum(data.values())}")
wc = WordCloud(width=512,height=512,background_color="white", max_words=6000,mask=mask,
               max_font_size=250, random_state=42,contour_width=1, font_path="fonts/SovngardeLight.ttf")

wc.generate_from_frequencies(data)
wc.to_file("out/cloud.png")
s = wc.to_svg()
print(s,file=open("out/cloud.svg","w"))


