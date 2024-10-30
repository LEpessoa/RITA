import pandas as pd
import random

df = pd.read_csv(
    "./complete_dataset_with_subtypes_COMPLETE.csv",
    sep=";",
    header=None,
    encoding="utf8",
)
df.columns = ["phrase", "start", "end", "word", "tag"]

word_freq_dic = {}  # Dictionary to hold the frequency of each word


def upcount(word):
    if word in word_freq_dic:
        word_freq_dic[word] += 1
    else:
        word_freq_dic[word] = 1


for row in df.iterrows():  # Populating word_freq_dic
    # phrase = row[1][0]
    # start = row[1][1]
    # end = row[1][2]
    # tag = row[1][4]
    word = row[1][3]
    upcount(word)

words_for_train_count_dic = (
    {}
)  # Dictionary to hold, for each word, the number of words needed for the train dataset

for key, value in word_freq_dic.items():  # Populate words_for_train_count_dic
    total_freq = value
    to_train = int(0.7 * value)
    words_for_train_count_dic[key] = to_train

# Split train and test on a proportion 70% X 30%
rows_for_train = []
rows_for_test = []
for row in df.iterrows():
    # phrase = row[1][0]
    # start = row[1][1]
    # end = row[1][2]
    # tag = row[1][4]
    word = row[1][3]
    to_train = words_for_train_count_dic[word] > 0
    words_for_train_count_dic[word] -= 1
    if to_train:
        rows_for_train.append(row)
    else:
        rows_for_test.append(row)

# Build the CSVs ################################################################################
import spacy
from spacy.tokens import DocBin, Span
from spacy.matcher import PhraseMatcher

nlp = spacy.blank("en")


def genCSV(data_list, is_train_data):
    df = pd.DataFrame([dado[1] for dado in data_list])
    df.columns = ["phrase", "start", "end", "word", "tag"]
    df.sort_values(by="word")
    if is_train_data:
        df.to_csv("./train.csv", index=False, header=None, sep=";")
    else:
        df.to_csv("./test.csv", index=False, header=None, sep=";")


# Train docBin
genCSV(rows_for_train, is_train_data=True)
# Test docBin
genCSV(rows_for_test, is_train_data=False)


count_train = len(rows_for_train)
count_test = len(rows_for_test)
pct_train = count_train / (count_train + count_test) * 100
pct_test = count_test / (count_train + count_test) * 100
print(f"The train list has {count_train} elements: {pct_train:.2f}%")
print(f"The test list has {count_test} elements: {pct_test:.2f}%")
