from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator
import pandas as pd
import matplotlib.pylab as plt
from PIL import Image
import numpy as np
stopwords = set(STOPWORDS)
mask = np.array(Image.open('E:/twiiter.png'))
#we will read the text
data_file = pd.read_csv('E:/combined_csv.csv')
#wordcloud
wordcloud = WordCloud(stopwords = stopwords , width=1600 , height=800,mask=mask,background_color="White",colormap="Set2").generate(''.join(data_file['text']))
plt.figure(figsize=(20,10),facecolor='k')
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.tight_layout (pad=0)
#saving the image of wordcloud
wordcloud.to_file ('E:/nasirsoft_wordcloud.png')
plt.show()
