
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans

nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object

# create training data
import json
def gen_spacy_obj(fname):
    f = open(f'{fname}.json')
    TRAIN_DATA = json.load(f)
    for text, annot in tqdm(TRAIN_DATA['annotations']): 
        doc = nlp.make_doc(text) 
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        filtered = filter_spans(ents)
        doc.ents = filtered 
        db.add(doc)

    db.to_disk(f'./{fname}.spacy') # save the docbin object

# create validation data
# f2 = open('val_dataset.json')
# VAL_DATA = json.load(f2)
# for text, annot in tqdm(VAL_DATA['annotations']): 
#     doc2 = nlp2.make_doc(text) 
#     ents2 = []
#     for start, end, label in annot["entities"]:
#         span = doc2.char_span(start, end, label=label, alignment_mode="contract")
#         if span is None:
#             print("Skipping entity 2")
#         else:
#             ents2.append(span)
#     doc2.ents = ents2
#     db2.add(doc2)

# db2.to_disk("./validation_data.spacy") # save the docbin object

# obtain config file
#! python -m spacy init config config.cfg --lang en --pipeline ner --optimize efficiency

# train
#! python3.10 -m spacy train config.cfg --output ./ --paths.train ./train_dataset.spacy --paths.dev ./val_dataset.spacy --gpu-id 0
# ...Using CPU
# ℹ To switch to GPU 0, use the option: --gpu-id 0

# demo
# nlp_ner = spacy.load("/content/model-best") ...

gen_spacy_obj("train_dataset")
gen_spacy_obj("val_dataset")