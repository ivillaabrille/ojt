import spacy

#load spacy model
nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

#tokenization
for token in doc:
	print(token.text)

#after tokenization, parts of speech parse,tag and dependencies
for token in doc:
	print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

#named entities	
for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label)

#word vectors and similarity
#doc, span and token comes with .similarity()
tokens = nlp(u'dog cat banana')
for token1 in tokens:
	if token2 in tokens:
		print(token1.similarity(token2))
for token in tokens:
	print(token.text, token.has_vector, token.vector_norm, token.is_oov)