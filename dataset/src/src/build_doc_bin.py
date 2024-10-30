import pandas as pd
import spacy
from spacy.tokens import DocBin, Span
from spacy.matcher import PhraseMatcher

test_df = pd.read_csv("./dataset/test.csv", sep=";")
test_df.columns = ["phrase", "start", "end", "word", "tag"]
test_doc_bin_diskpath = "./NER_MODEL/DOC_BINS/test.spacy"

train_df = pd.read_csv("./dataset/train.csv", sep=";")
train_df.columns = ["phrase", "start", "end", "word", "tag"]
train_doc_bin_diskpath = "./NER_MODEL/DOC_BINS/train.spacy"

nlp = spacy.blank("en")


def createDocBin(data_frame, disk_path: str):
    db = DocBin()
    for id, row in data_frame.iterrows():
        phrase = row.phrase
        start = row.start
        end = row.end
        tag = row.tag
        word = row.word
        doc = nlp(phrase)
        matcher = PhraseMatcher(nlp.vocab)
        matcher.add(tag, list(nlp.pipe([word])))
        matches = matcher(doc)
        try:
            doc.ents = [Span(doc, match[1], match[2], tag) for match in matches]
        except Exception as e:
            print(e)
            print("Mostrando Matches")
            print(matches)
            print(doc)
            print(word)
            print(tag)
            print(matches)
            print("#" * 40)
            exit(1)
        db.add(doc)
    db.to_disk(disk_path)


if __name__ == "__main__":
    createDocBin(test_df, test_doc_bin_diskpath)
    createDocBin(train_df, train_doc_bin_diskpath)
