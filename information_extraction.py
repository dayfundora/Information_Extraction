from nltk.tag.stanford import POSTagger

def get_nouns(text):
    doc = nlp(text)
    
    spanish_postagger = POSTagger('models/spanish.tagger', 'stanford-postagger.jar', encoding='utf8')

    for sent in doc.sents:

        words = sent.split()
        tagged_words = spanish_postagger.tag(words)

        nouns = []

        for (word, tag) in tagged_words:

            print(word+' '+tag).encode('utf8')
            if isNoun(tag): nouns.append(word)
    return nouns

def chunked_sentences(text):
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunk_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    return chunk_sentences
