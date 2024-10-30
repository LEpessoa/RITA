import pandas as pd
import re

original_dataset_path = "./complete_dataset_with_subtypes_COMPLETE.csv"
corrected_dataset_path = "./complete_dataset_with_subtypes_CORRECTED.csv"
phrasesWithoutWordPath = "./phrases_without_word.csv"

###################
##### CONFIG ######
###################
parse_original = True
checkFrequency_bool = True
checkBoundaries_bool = True
organizeData_bool = False
buildCahtGPTPrompts = False  # If true, generates prompts to create new phrases using chatGPT and awaits for an input to create the new phrase's CSV data point.

###############################
##### Dataset Loading #########
###############################
dataset_to_parse = ""
if parse_original:
    dataset_to_parse = original_dataset_path
else:
    dataset_to_parse = corrected_dataset_path
df = pd.read_csv(dataset_to_parse, delimiter=";", header=None)
df.columns = ["phrase", "start", "end", "word", "tag"]
df = df.sort_values(by=["word"])


def formatForRegexPatternSafety(value):
    value = value.replace(")", "\)")
    value = value.replace("(", "\(")
    value = value.replace("+", "\+")
    return value


def checkFrequency(buildChatGPTPrompts: bool):
    """buildChatGPTPrompts=True will cause the program to generate prompts to ask chatGPT for new phrases whenever words with less than 5 phrases are found"""
    dic = {}
    df.sort_values(by="word")
    for index, row in df.iterrows():
        try:
            word = row[3].lower()
        except Exception as e:
            print(f"Phrase: {row[0]}\n WordBounded: {row[3]}")
            print("Exiting early.")
            exit(-1)
        if not word in dic.keys():
            dic[word] = 1
            continue
        dic[word] += 1
    total = 0
    for k in dic.keys():
        # print('Dictionary of words.')
        # print(f'{k}: {dic[k]}')
        if dic[k] < 5:
            diff = 5 - dic[k]
            total += diff
            if buildChatGPTPrompts:
                generateNewPhrasesPipeline(df, k)
            # print(f"Word: **{k}** Count: {dic[k]}")
        if dic[k] > 5:
            print(f"Found {dic[k]} phrases for word {k}")
    print(f"Total new phrases that need generation: {total}")


def checkBoundaries():
    phrases_with_bad_boundaries = 0
    count_phrases_without_word = 0
    with open(corrected_dataset_path, "w+") as corrected_dataset:
        with open(phrasesWithoutWordPath, "w+") as phrases_without_word:
            for index, row in df.iterrows():
                try:  # Catch errors where row[1] or row[2] might not be numbers for some reason.
                    s = int(row[1])
                    e = int(row[2])
                    span = row[0][s:e]
                    word = row[3]
                    if span.lower() != word.lower():
                        # print(f"{index} - Word **{word}** not equal span **{span}**")
                        phrases_with_bad_boundaries += 1
                except Exception as e:
                    print(e)
                    print(f'"{row[0]}";{row[1]};{row[2]};"{row[3]}";"{row[4]}"')
                    print("Finishing early.")
                    exit(1)

                # try:  # Catch errors where the word is simply not found in the phrase
                patternToFind = formatForRegexPatternSafety(row[3])

                match = re.search(
                    rf"""\b{patternToFind}(?=(\b| |'s\b|,|\.))""",
                    row[0],
                    re.IGNORECASE,
                )
                # print(f"Did it match? {match}")
                if match != None:
                    start = match.start()
                    end = match.end()
                    rowCSV_STRING = f'"{row[0]}";{start};{end};"{row[3]}";"{row[4]}"\n'
                    corrected_dataset.write(rowCSV_STRING)
                else:
                    print(f"Trying to find: **{patternToFind}** in:\n**{row[0]}**")
                    count_phrases_without_word += 1
                    phrase_without_word = (
                        f'"{row[0]}";{row[1]};{row[2]};"{row[3]}";"{row[4]}"\n'
                    )
                    # print(f"Found phrase without word:\n{phrase_without_word}")
                    phrases_without_word.write(phrase_without_word)
                # except AttributeError as e:

    print(f"Found {count_phrases_without_word} phrases without word.")
    print("Finished")


def buildPhrasesToPasteOnTheDataset(text: str, word: str, tag: str):
    m = re.search(f"({word} | {word}| {word} )", text, re.IGNORECASE)
    try:
        phrase = f'"{text}";{m.start()};{m.end()};"{word}";"{tag}"\n'
        with open("./newPhrases.csv", "a+") as f:
            f.write(phrase)
    except Exception as e:
        print("BAD PHRASE TRY AGAIN")
        raise e


def generateNewPhrasesPipeline(df: pd.DataFrame, word):
    dfFiltered = df.loc[df["word"] == word]
    numPhrasesToGenerate = 5 - dfFiltered.shape[0]
    knownPhrases = ""
    tag = ""
    for index, row in dfFiltered.iterrows():
        tag = row[4]
        knownPhrases += f"\n{row[0]}"
    # generate ChatGPT query
    query = (
        "#" * 20
        + "\n"
        + f'Here are phrases with the word " {word} "'
        + "\n"
        + "The phrases must be part of a System Storyline"
        + "\n"
        + knownPhrases
        + "\n"
        + f'Please provide me with {numPhrasesToGenerate} new phrases with the word " {word} " as is with spaces around.\n'
        + "#" * 20
    )
    # pyperclip.copy(query)
    print(query)
    # Receive text back to write to file
    phrasesGenerated = 0
    while phrasesGenerated != numPhrasesToGenerate:
        tx = input("Paste phrase.\n")
        if tx == "ok":
            break
        try:
            buildPhrasesToPasteOnTheDataset(tx, word, tag)
            phrasesGenerated += 1
        except Exception as e:
            continue


def sortDataset(df: pd.DataFrame):
    df: pd.DataFrame = df.sort_values(by=["word"])
    df.to_csv(original_dataset_path, sep=";", index=None, header=None)


if __name__ == "__main__":
    if checkFrequency_bool:
        checkFrequency(buildCahtGPTPrompts)
    if checkBoundaries_bool:
        checkBoundaries()
