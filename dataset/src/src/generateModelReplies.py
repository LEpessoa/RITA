# Purpose of the script: Load the ChosenPhraseFromSheets.csv file and feed every phrase to the model, recording the answers in a csv
import pandas as pd
import spacy

df = pd.read_csv("./ChosenPhrasesFromSheets.csv")
print(df.columns)

nlp = spacy.load("../../target_trf/model-best")


def separateText(text):
    text_separate_dot = str.split(text, ".")
    final_separated_phrases = []
    for phrase in text_separate_dot:
        # sep_comma = str.split(phrase, ",")
        # for txt in sep_comma:
        #     final_separated_phrases.append(txt)
        final_separated_phrases.append(phrase)
    # print(f"Count of phrases found: {len(final_separated_phrases)}")
    return final_separated_phrases


data = []
for index, row in df.iterrows():
    # print(f"INdex:{index}, Phrase: {row['Phrase']}")
    phrase = row["Phrase"]
    ents = []
    for sep_phrase in separateText(row["Phrase"]):
        # print(f"Dealing with subPhrase: {sep_phrase}")
        doc = nlp(sep_phrase.lower())
        for ent in doc.ents:
            tup = (
                ent.text,
                ent.label_,
            )
            ents.append(tup)
    data.append(ents)

df_out = pd.DataFrame(data)
df_out.to_csv("./model_classification_test.csv", sep=";", index=None, header=None)
