# builds the npy file with the sentences in the format: ["sentence",[(start,end,label)]]
import _6_sentences as _6
import numpy as np
import re


def escapeSpecials(word):
    word = word.replace(")", "\)")
    word = word.replace("(", "\(")
    word = word.replace("+", "\+")
    return word


def createAnnotatedArrayOfPhrases(in_list):
    # list must have the format [{type:"type", word:"word", phrase:"phrase"}]
    # example: {'type': 'DEVICE', 'word': 'Nidec Servo Corporation MAC series brushless motor', 'phrase': 'The robotic arm in the factory was powered by the Nidec Servo Corporation MAC series brushless motor, providing smooth and precise movements.'},
    result = []
    # Result is an array with each item in the format: ["phrase",[(start,end,label)]]
    for cat in in_list:
        try:
            word = escapeSpecials(cat["word"])
            r = re.finditer(
                word,
                cat["phrase"],
                re.IGNORECASE,
            )
        except Exception as e:
            print("Failed processing line:")
            print(re.sub(re.escape(")"), "\)", cat["phrase"]))
            print(e)
        match_spans = []
        for m in r:
            span = (m.start(), m.end(), cat["type"])
            match_spans.append(span)
        if len(match_spans) == 0:
            print("Found empty span for phrase:")
            print(cat["phrase"])
            exit(1)
        result.append({"phrase": cat["phrase"], "spans": match_spans})
    return result


if __name__ == "__main__":
    path = "./_7_result.npy"
    r = createAnnotatedArrayOfPhrases(_6.sentences)
    np.save(path, r)
    # a = np.load(path, allow_pickle=True)
    # for cat in a:
    #     print(cat)