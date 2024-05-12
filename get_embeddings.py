import spacy
import json

nlp = spacy.load('en_core_web_lg')


pdf_list = ['Product_1.txt','Product_2.txt','Product_3.txt','Product_4.txt','Product_5.txt']
descriptions = []
for file in pdf_list:
    with open(f'data/{file}','r') as f:
        text = f.read()
    descriptions.append(text) 

description_vectors_list = []

for description in descriptions:
    doc = nlp(description)

    reduced_vector = doc.vector[:128].tolist()

    entry = {"vector": reduced_vector, "text": description}
    description_vectors_list.append(entry)

with open('Product_data.json', 'w') as json_file:
    json.dump(description_vectors_list, json_file, indent=2)

print("JSON file created: dummy_data.json")