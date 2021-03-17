## Information Extraction

In this project, two models are presented to label the words of a text according to the part of the sentence to which they belong. The objective with these models is to prepare the document to lay the foundations for the extraction of information from it.

There are different frameworks to be able to classify words according to their part of the sentence to which they belong (**POS-TAG**) as well as entity recognition (**NER**). Among them we find **NLTK**,** Spacy**, **Freeling** and **Stanford-NLP**. Based on what has been done in these frameworks, we will create models that allow us to carry out these tasks.
### Model to Identify Parts of Sentence:
The POS Tagger takes a text in a language and assigns parts of speech to each word (*verb, adjective, noun…*). To achieve this model we use the **NLP architecture**.

### Model for NER
It is used to identify entities in a document, for example, organizations, people, etc. Some of the standard libraries used are **Standford NER**, **spaCy** and **NLTK**; the NLTK was the one implemented in the project. To perform NER using NLTK, it is necessary to do it in 3 stages:
1. Work Tokenization
2. Parts of Speech (POS) tagging
3. Named Entity Recognition