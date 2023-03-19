import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy import displacy
import json
sp = spacy.load("en_core_web_sm")
nlp_ner = spacy.load("./model-last")
doc = nlp_ner('''write lyrics in the style of Modest Mouse''') # input sample text
displacy.render(doc, style="ent")
docJSON = doc.to_json()
# print(docJSON)
for e in doc.ents:
    print(e.label_, ": ", e)

# for entry in doc:
#     #print('Current entry\n {}'.format(entry))
#     for entity in sp(', '.join(entry)).ents:
#         print(entity.text, entity.label)

