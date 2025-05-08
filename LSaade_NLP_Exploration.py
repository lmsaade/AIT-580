import nltk
import matplotlib.pyplot as plt

nltk.download('book')
nltk.download('punkt_tab')

textfile = open("narrative.txt", mode ='r')
allwords = textfile.read()

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

tokens = tokenizer.tokenize(allwords.lower())
from nltk.corpus import stopwords

tokens = [token for token in tokens if token not in stopwords.words('english')]

freq_dist = nltk.FreqDist(tokens)
print(freq_dist.most_common(25))

freqplot = freq_dist.plot(25)
plt.show()
