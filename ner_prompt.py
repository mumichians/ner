import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy import displacy
import json
import sys

prompt = sys.argv[1]
print(prompt)
#nlp = spacy.load("en_core_web_sm")
nlp_ner = spacy.load("./model-best")
doc = nlp_ner(prompt) # input sample text
# nlp_ner = nlp.create_pipe("./model-last")
# nlp.add_pipe(nlp_ner)
# doc = nlp_ner(prompt)
# displacy.render(doc, style="ent")

# docJSON = doc.to_json()
# print(docJSON)
artist = ""
title = ""
genre = ""
for e in doc.ents:    
    if (e.label_ == "ARTIST"):
        artist += (str(e) + " ")
    if (e.label_ == "TITLE"):
        title += (str(e) + " ")
    if (e.label_ == "GENRE"):
        genre += (str(e) + " ")

print("TITLE: ", title)
print("ARTIST: ", artist)
print("GENRE: ", genre)


# for entry in doc:
#     #print('Current entry\n {}'.format(entry))
#     for entity in sp(', '.join(entry)).ents:
#         print(entity.text, entity.label)


