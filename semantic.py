import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#results from the above seem to look like the closer the number is to 1 then the more similar a word is, the highest number was for comparing cat and monkey presumably as both are animals.
#interestingly the 2nd highest was for monkey and banana, so spacy has taken into account the association of monkeys with bananas

tokens = nlp('cat apple monkey banana human ape gorilla')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text,token1.similarity(token2))

# on the above, whats interesting is that monkey, ape and gorilla are all rated as around 0.99 for similarity, so spacy recognises these as being almost the same thing.
# What i've also found interesting is that "human" however is rated as only 0.19 similarity even though we are also apes


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

#EXAMPLE FILE TEST- When changing to sm the similarity figures seem to be significantly lower, i think this is because the simple model has no word vectors loaded so sm is less effective at
#comparing similarities
