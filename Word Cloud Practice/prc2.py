from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
 

# text = open('text1.txt', 'r').read()
text = "hellow Wolrd"

wc= WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()