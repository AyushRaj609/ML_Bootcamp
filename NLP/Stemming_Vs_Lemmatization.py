
# this two line needs to run for the first time!
# import nltk
# nltk.download('punkt')
from nltk.stem import PorterStemmer
stemming=PorterStemmer()

words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

for word in words:
    print(word+"---->"+stemming.stem(word))

stemming.stem('congratulations')
stemming.stem('sitting')

### LAncaster  Stemming algorithm
from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
print("----------------LancasterStemmer-output----------------")
for word in words:
    print(word+"---->"+lancaster.stem(word))

from nltk.stem import RegexpStemmer
reg_stemmer=RegexpStemmer('ing|s$|e$|able$', min=4)
print("----------------RegexpStemmer-output----------------")
print(reg_stemmer.stem("eating"))
print(reg_stemmer.stem("ingplaying"))

# Snowball Stemmer 
from nltk.stem import SnowballStemmer
snowballstemmer=SnowballStemmer('english',ignore_stopwords=False)
print("----------------SnowballStemmer-output----------------")
for word in words:
    print(word+"---->"+snowballstemmer.stem(word))

print(stemming.stem("fairly"),stemming.stem("sportingly"))
print(snowballstemmer.stem("fairly"),snowballstemmer.stem("sportingly"))

# this two line needs to run for the first time!
# import nltk
# nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

'''
POS- Noun-n
verb-v
adjective-a
adverb-r
'''
print("----------------WordNetLemmatizer-output----------------")
for word in words:
    print(word+"---->"+lemmatizer.lemmatize(word,pos='v'))

print(lemmatizer.lemmatize("good",pos='v'))

