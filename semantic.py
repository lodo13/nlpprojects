"""the progam calculates the similarity among selected words"""


#importing module and dictionary
import spacy
nlp = spacy.load('en_core_web_sm')

#selected words to compare
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#selected sentences to compare to the model sentence
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""monkey and banana have a big similarity, surely because monkeys eat bananas
banana and apple are both fruit so they share a high similarity

where did my dog go is most similar to hello, there is my car
that's surprising, surely for the use of the adverbs 

when i run with a simpler dictionary, the similarities are very different, banana and monkey aren't similar anymore
even banana and apple aren't very similar, surprisingly apple and monkey are the most similar

same result for the sentences, where i can't understand why the sentences are similar any longer"""