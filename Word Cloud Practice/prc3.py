from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt

os.chdir(sys.path[0])

#Read Text
text=open('jeff_bezos_speech.txt', mode='r', encoding='utf-8').read()
stopwords = stopwords

wc = WordCloud(
     background_color='white',
     stopwords=stopwords,
     height=600,
     width=400
)
wc.generate(text)

wc.to_file('wordcloud_output.png')