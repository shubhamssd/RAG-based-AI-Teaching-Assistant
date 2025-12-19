import requests
import os
import json 
import pandas as pd

def create__embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model":"bge-m3",
        "prompt": text_list
    })

    embedding = r.json()['embedding']
    return embedding

jsons = os.listdir("jsons")  #list all jsons

my_dict = []
chunk_id = 0
 
for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
        print(f"Creating embeddings for {json_file}")
        embeddings = create__embedding([c['text'] for c in content['text']])
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dict.append(chunk)

df = pd.DataFrame.from_records(my_dict)
print(df)

# print(my_dict)

# a = create__embedding(["cat sat on mat","Lion hunting in jungle"])
# print(a)