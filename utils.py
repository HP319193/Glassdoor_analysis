from gensim.models import KeyedVectors
import pandas as pd
model = KeyedVectors.load_word2vec_format('models/word2vec-google-news-300.gz', binary=True)

def get_similar_words(word, lower_limit=0, top_n=40):
    word = word.replace("-", "")
    similar_words = model.most_similar(word, topn=top_n)
    
    result = []
    print(similar_words)
    for similar_word in similar_words:
        if similar_word[1] > lower_limit:
            result.append(similar_word)
        else:
            break

    return result

def get_common_ISIN(file1, file2):
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)

    res_data = []

    column1 = data1['ISIN']  
    column2 = data2['ISIN']

    list1 = column1.tolist()
    list2 = column2.tolist()

    common_substrings = [a for a in list1 for b in list2 if a in b]
    return list(set(common_substrings))

