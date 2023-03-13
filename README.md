# ner
spaCy ner model

how to train ner model:
1. generateExamples.py creates train_dataset.json and val_dataset.json
2. ner_train.py turns train_dataset.json and val_dataset.json into .spacy objects
3. run the following command 
    "python3.10 -m spacy train config.cfg --output ./ --paths.train ./train_dataset.spacy --paths.dev ./val_dataset.spacy --gpu-id 0"
4. interact with model by running ner_prompt.py
