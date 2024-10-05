from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
text = """
Python is an interpreted high-level general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""
stopwords = set(STOPWORDS)
wordcloud = WordCloud(
    width=600, 
    height=400, 
    background_color='black',   # Background color of the word cloud
    colormap='Set1',            # Colormap to highlight the words
    stopwords=stopwords,        # Exclude stopwords
    max_font_size=150,          # Maximum font size
    min_font_size=10,           # Minimum font size
    random_state=42             # Random seed for color
).generate(text)

plt.figure(figsize=(7, 5))  
plt.imshow(wordcloud, interpolation='bilinear')  
plt.axis('off')  
plt.tight_layout(pad=2)  
plt.show()
