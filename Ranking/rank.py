import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
from nltk.tokenize import PunktSentenceTokenizer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def freqDist(text):
    # sentences = nltk.sent_tokenize(text)
    # for sent in sentences:
    #     print(nltk.pos_tag(nltk.word_tokenize(sent)))
    ps = SnowballStemmer("english")

    text = text.replace("said","say")
    tokens = word_tokenize(text)


    tokens[:] = [ps.stem(word) for word in tokens]


    freq = nltk.FreqDist(tokens)
    # sort_dict = sorted(freq, key=lambda x: (-freq[x], x))
    # wordCount = tokens.__len__()
    # for key in sort_dict:
    #     percent = (freq[key] / wordCount)*100
    #     if percent > 0.2:
    #         print(key + ":"+str(percent)+"%")

    return freq

def get_key_words_count(text,words):
    ps = SnowballStemmer("english")

    text = text.replace("said", "say")
    tokens = word_tokenize(text)

    tokens[:] = [ps.stem(word) for word in tokens]

    wordCount = []
    for word in words:
        wordCount.append(tokens.count(word))

    return wordCount








