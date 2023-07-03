import spacy
nlp = spacy.load('en_core_web_md')
movielist=[]

#movie description and conversion into nlp
movie_descr=("""Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
 the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
 Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator""")
nlpblurb = nlp(movie_descr)


#converting movies in file into list format, by adding each line to movielist variable
f = open('movies.txt', 'r')
for line in f:
    movielist.append(line)

def moviechecker (nlpblurb):
#checking movie description for similarities with list  
    for token in movielist:
        token = nlp(token)
        (token.similarity(nlpblurb))
#finding largest value to get most similar movie and then printing    
    title = max((nlp(token).similarity(nlpblurb), token) for token in movielist)
    print("Your closest match is as follows: " + str(title))


#calling function    
moviechecker(nlpblurb)










