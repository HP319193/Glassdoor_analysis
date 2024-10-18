from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('models/word2vec-google-news-300.gz', binary=True)

def get_similar_words(word, lower_limit=0, top_n=40):

    similar_words = model.most_similar(word, topn=top_n)
    
    result = []

    for similar_word in similar_words:
        if similar_word[1] > lower_limit:
            result.append(similar_word[0])
        else:
            break

    return result