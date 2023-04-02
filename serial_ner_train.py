import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans

nlp = spacy.blank("en") # load a new spacy model

# create training data
import json

def gen_spacy_obj(fname):
    f = open(f'{fname}.json')
    TRAIN_DATA = json.load(f)

    doc_bins = [] # create a list to hold the DocBin objects
    docs_per_bin = 100 # set the number of documents per DocBin object

    for i, (text, annot) in enumerate(tqdm(TRAIN_DATA['annotations'])):
        if i % docs_per_bin == 0:
            db = DocBin() # create a new DocBin object
            doc_bins.append(db)
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
        doc_bins[-1].add(doc) # add the document to the last DocBin object in the list

    for i, db in enumerate(doc_bins):
        db.to_disk(f'./{fname}_{i}.spacy') # save each DocBin object separately


# train
#! python3.10 -m spacy train config.cfg --output ./ --paths.train ./traindata --paths.dev ./valdata --gpu-id 0


# demo
# nlp_ner = spacy.load("/content/model-best") ...

gen_spacy_obj("train_dataset")
gen_spacy_obj("val_dataset")
