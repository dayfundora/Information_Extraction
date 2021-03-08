from nltk.tag.stanford import POSTagger

def open_file(archivo):
    with open(archivo, encoding= 'utf8' ) as f: 
        text =f.read()
        return text

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

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

def entity_names(text):
    entity_names = []
    chunk_sentences=chunked_sentences(text)
    for tree in chunk_sentences:
        entity_names.extend(extract_entity_names(tree))
    return entity_names

if __name__ == "__main__":
    text =open_file('input.txt')
    nouns=get_nouns(text)
    print(nouns)
    