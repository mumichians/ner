import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy import displacy
import json
sp = spacy.load("en_core_web_sm")
nlp_ner = spacy.load("./model-last")
doc = nlp_ner('''I would like a rock song in the style of Eminem please''') # input sample text
displacy.render(doc, style="ent")
docJSON = doc.to_json()
# print(docJSON)
for e in doc.ents:
    print(e, e.label_)

# for entry in doc:
#     #print('Current entry\n {}'.format(entry))
#     for entity in sp(', '.join(entry)).ents:
#         print(entity.text, entity.label)


# 2023-03-08 14:44:09.195637: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
# To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
# 2023-03-08 14:44:09.669968: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
# 2023-03-08 14:44:09.670007: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
# 2023-03-08 14:44:09.670013: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
# 2023-03-08 14:44:10.185323: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
# 2023-03-08 14:44:10.185611: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
# 2023-03-08 14:44:10.185718: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
# /home/convai/.local/lib/python3.10/site-packages/spacy/displacy/__init__.py:139: UserWarning: [W005] Doc object not parsed. This means displaCy won't be able to generate a dependency visualization for it. Make sure the Doc was processed with a model that supports dependency parsing, and not just a language class like `English()`. For more info, see the docs:
# https://spacy.io/usage/models
#   warnings.warn(Warnings.W005)

# Using the 'dep' visualizer
# Serving on http://0.0.0.0:5000 ... 

# for entity in processed.ents ...
# Look into this for extracting entity info TODO 