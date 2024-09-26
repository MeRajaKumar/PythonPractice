from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Python is powerful and fast. Python is easy to learn. Python can handle a variety of tasks."
wordcloud = WordCloud(width=400, height=300, background_color='white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('on')
plt.show()
