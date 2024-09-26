import matplotlib.pyplot as plt
from wordcloud import WordCloud
# Sample text data (replace with your own)
text = "This is a sample text for generating a word cloud. Word clouds are a visual representation of the frequency of words in a given text. The more frequently a word appears, the larger its size in the word cloud."
# Create a WordCloud object with desired parameters
wordcloud = WordCloud(
    width=500,
    height=800,
    background_color="white",
    max_words=200,
    stopwords=["the", "and", "in", "to", "is", "it", "of", "that", "for", "this", "a", "on", "as", "with", "by", "or", "are", "from", "not", "an", "as", "in", "of", "on", "to"],
    collocations=False,  # Prevent collocations (e.g., "word cloud")
    random_state=42,  # Ensure consistent results
)
# Generate the word cloud
wordcloud.generate(text)
# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()