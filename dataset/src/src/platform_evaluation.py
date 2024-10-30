import pandas as pd
import spacy
from typing import List

df = pd.read_csv("./dataset/platform_evaluation/platform_evaluation.csv",sep=';',header=None)
df.columns = ["phrase_kind","ico_type","phrase","word"]

def split_phrase(text):
    return str.split(text, ".")

def process_phrases(split_phrases:List[str], nlp:spacy.Language, result_array:List[str]):
    r = ";"
    for p in split_phrases:
        doc = nlp(p.lower())
        for ent in doc.ents:
            r = r +  f"('{ent.text}','{ent.label_}');"
    result_array.append(r)
        
if __name__ == "__main__":
    result_array = []
    nlp = spacy.load("./NER_MODEL/target/model-best")
    
    for id,row in df.iterrows():
        phrase = row['phrase']
        split_phrases:List[str] = split_phrase(phrase)
        process_phrases(split_phrases,nlp,result_array)
        
    results_df = pd.DataFrame(result_array)
    results_df.to_csv("./dataset/platform_evaluation/result.csv",sep=";",header=None,index=False)