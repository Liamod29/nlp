#importing spacy
import spacy
nlp = spacy.load('en_core_web_sm')

#creating list of sentences and adding to list
gardenpathSentences = ['The old man the boat.', 'The florist sent the flowers was pleased.']
gardenpathSentences.extend(['Mary gave the child a Band-Aid.', 'That Jill is never here hurts', 'The cotton clothing is made of grows in Mississippi.'])

#tokenising gardenpath sentences, and then printing them
doc = nlp (str(gardenpathSentences))
[token.orth_ for token in doc]
print ([token.orth_ for token in doc if not token.is_punct | token.is_space])

#get labels and entities, then print them
print([(i, i.label_, i.label) for i in doc.ents])

#examing entity labels
print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))


#For GPE, the explanation given was Countries, cities and states, this makes sense as the word in question was Mississippi- a state in USA
#For PERSON, the explanation given is People, including fictional people. So this also makes sense as both Jill and Mary were listed as "PERSON", and even though they dont refer
#to anyone specifically they're names so they could refer to either a real or fictional person  