import pandas as pd

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.augmenter.word as naw
import re
import random

pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
debug = False

last_index_save = 0
last_index_read = 0


def exitPrintingLastIndexRead():
    global last_index_read, list_of_phrases, outputPath

    if len(list_of_phrases) != 0:
        augmented_df = pd.DataFrame(list_of_phrases)
        augmented_df.to_csv(outputPath, index=None, header=None, sep=";", mode="a+")
    saveLastReadIndexToDisk()
    print(f"Last index read from the dataframe was: \n######{last_index_read}######")
    exit(1)


def printIfDebug(text):
    if debug:
        print(text)


def augWithSynonym(text):
    if text == "" or text == "" or text == None:
        return ""
    aug = naw.SynonymAug(
        aug_src="wordnet",
        model_path=None,
        name="Synonym_Aug",
        aug_min=1,
        aug_max=100,
        aug_p=0.4,
        lang="eng",
        stopwords=None,
        tokenizer=None,
        reverse_tokenizer=None,
        stopwords_regex=None,
        force_reload=False,
        verbose=0,
    )
    augmented = aug.augment(text)
    return augmented[0]


def truncateFile(filePath):
    f = open(filePath, "a")
    f.truncate()
    f.close()


def augWithKeyboardTypos(text):
    """text: a simple string such as  'A simple string'"""
    if text == None or text == "":
        return ""
    try:
        aug = nac.KeyboardAug(
            name="Keyboard_Aug",
            aug_char_min=1,
            aug_char_max=10,
            aug_char_p=0.2,
            aug_word_p=0.2,
            aug_word_min=1,
            aug_word_max=5,
            stopwords=None,
            tokenizer=None,
            reverse_tokenizer=None,
            include_special_char=True,
            include_numeric=True,
            include_upper_case=True,
            lang="en",
            verbose=0,
            stopwords_regex=None,
            model_path=None,
            min_char=4,
        )
        augmted = aug.augment(text)
        return augmted[0]
    except Exception as e:
        printIfDebug(e)
        printIfDebug(f"Received input: {text}")
        printIfDebug(f"Failed augmenting text:\n {text}")
        printIfDebug(f"Tried to return\n{augmted}\non index 0.\nFIN")
        raise (e)


def augWithBackTranslation(text):
    printIfDebug(f"BACKTRANSLATING:\n{text}")
    # text = 'The quick brown fox jumped over the lazy dog'
    back_translation_aug = naw.BackTranslationAug(
        from_model_name="Helsinki-NLP/opus-mt-en-de",
        to_model_name="Helsinki-NLP/opus-mt-de-en",
    )
    result = back_translation_aug.augment(text)[0]
    printIfDebug(f"Result of BACKTRANSLATION:\n{result}")
    printIfDebug("#" * 20)
    return result


def gen2DifferentRandIntsInRange(maxIndex):
    w1 = None
    w2 = None
    w1 = random.randint(0, maxIndex)
    while w1 == None or w2 == None or w1 == w2:
        w2 = random.randint(0, maxIndex)
    return (
        w1,
        w2,
    )


def augWithSwapWords(text):
    words = text.split(" ")
    maxIndex = len(words) - 1
    index1, index2 = gen2DifferentRandIntsInRange(maxIndex)
    words[index1], words[index2] = words[index2], words[index1]
    return " ".join(words)


# mask_list = ["SOMERANDOMMASK", "TGHUVJ", "Grimvald", "*******************"]
mask = ""


def maskPhrase(phrase, targetWord):
    printIfDebug(f"Received phrase:\n{phrase}\n to mask.")
    # The mask must have a space after it to prevent being excluded from the phrase during synonymAugmentation
    compiled = re.compile(re.escape(targetWord), re.IGNORECASE)
    maskedPhrase = compiled.sub(mask, phrase)
    # maskedPhrase = phrase.replace(targetWord, mask + " ")
    printIfDebug(f"Result of phrase masking for word: {targetWord}:\n{maskedPhrase}")
    return maskedPhrase


def escape_regex(text):
    # List of reserved regex characters that need to be escaped
    reserved_chars = r"\^$.|?*+()[]{}"

    # Escape each reserved character in the text
    escaped_text = re.sub(f"([{re.escape(reserved_chars)}])", r"\\\1", text)

    return escaped_text


def unmaskPhrase(phrase, targetWord):
    printIfDebug(f"Received phrase:\n{phrase}\n to UNmask.")
    # compiled = re.compile(re.escape(mask), re.IGNORECASE)
    compiled = re.compile(re.escape(mask), re.IGNORECASE)
    unmaskedPhrase = compiled.sub(targetWord, phrase)
    wordIsInPhrase = targetWord in unmaskedPhrase
    if not wordIsInPhrase:
        printIfDebug(
            f"Word: {targetWord} could not be found in phrase\n{unmaskedPhrase}\nduring unmasking process of phrase\n{phrase}"
        )
        separatePhrase(phrase + "### Failed during unmasking process.")
        if debug:
            exitPrintingLastIndexRead()
    printIfDebug(f"Result of UNmasking phrase:\n {phrase}:\n{unmaskedPhrase}")
    return unmaskedPhrase


def separatePhrase(phrase):
    with open("./badPhrasesDuringAugmentation.csv", "+a") as f:
        f.write(phrase + "\n")


def rowToTuple(row):
    return (
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
    )


def genTuple(phrase, tag, targetWord):
    addSpace = False
    targetWordRegexSafe = escape_regex(targetWord)
    match = re.search(
        rf"""\b{targetWordRegexSafe}(?=(\b| |'s\b|,|\.))""",
        phrase,
        re.IGNORECASE,
    )
    if match == None:
        addSpace = True
        match = re.search(
            rf"""{targetWordRegexSafe}""",
            phrase,
            re.IGNORECASE,
        )
    if match == None:
        print(
            f"Failed to find word {targetWord} in phrase:\n{phrase} during tuple generation phase"
        )
        separatePhrase(phrase + "### Failed during tuple generation.")
    if addSpace:
        before = phrase[: match.start()]
        after = phrase[match.end() :]
        phrase = before + " " + targetWord + " " + after
        match = re.search(
            rf"""{targetWordRegexSafe}""",
            phrase,
            re.IGNORECASE,
        )
    return (
        phrase,
        match.start(),
        match.end(),
        targetWord,
        tag,
    )

mask_list = ["SOMERANDOMMASK", "TGHUVJ", "Grimvald", "1998"]
def augmentMaskingTarget(phrase, targetWord, augmentFunction):
    global mask
    global mask_list
    printIfDebug(f"Augmenting Using Masks for {augmentFunction}")
    mask_index = 0
    while True:
        mask = mask_list[mask_index]
        maskedPhrase = maskPhrase(phrase, targetWord)
        augmentedMaskedPhrase = augmentFunction(maskedPhrase)
        unmaskedPhrase = unmaskPhrase(augmentedMaskedPhrase, targetWord)
        if targetWord not in unmaskedPhrase:
            mask_index += 1
            if mask_index > len(mask_list) - 1:
                print(f"All masks have failed to augment phrase:\n{phrase}.")
                exitPrintingLastIndexRead()
        else:
            return unmaskedPhrase

shouldPrint = True
def printIfShouldPrint(text):
    if shouldPrint:
        print(text)
        print('###########')
        
def completeAug(row):
    printIfShouldPrint(row)
    # Should receive a row and return 8 rows
    phrase1 = row[0]
    word = row[3]
    tag = row[4]
    print(">>>>>>>>>>START")
    printIfShouldPrint(phrase1)
    print("BREAK")
    
    # 1 - BackTranslate
    phrase2 = augmentMaskingTarget(phrase1, word, augWithBackTranslation)
    printIfShouldPrint(phrase2)
    print("BREAK")
    # 2 - WordSwap Each of the 2 phrases
    phrase3 = augmentMaskingTarget(phrase1, word, augWithSwapWords)
    phrase4 = augmentMaskingTarget(phrase2, word, augWithSwapWords)
    printIfShouldPrint(phrase3)
    printIfShouldPrint(phrase4)
    print("BREAK")
    # 3 - Aug all the 4 phrases with synonym substitution
    phrase5 = augmentMaskingTarget(phrase1, word, augWithSynonym)
    phrase6 = augmentMaskingTarget(phrase2, word, augWithSynonym)
    phrase7 = augmentMaskingTarget(phrase3, word, augWithSynonym)
    phrase8 = augmentMaskingTarget(phrase4, word, augWithSynonym)
    
    printIfShouldPrint(phrase5)
    printIfShouldPrint(phrase6)
    printIfShouldPrint(phrase7)
    printIfShouldPrint(phrase8)
    shouldPrint = False
    print(">>>>>>>>>> END ########################################################################################")
    
    fullListOfPhrases = [
        phrase1,
        phrase2,
        phrase3,
        phrase4,
        phrase5,
        phrase6,
        phrase7,
        phrase8,
    ]
    return [genTuple(cat, tag, word) for cat in fullListOfPhrases]


def load_dataset(debug):
    df = None
    if not debug:
        df = pd.read_csv("./train.csv", header=None, sep=";")
    if debug:
        df = pd.read_csv("./miniTrainDebug.csv", header=None, sep=";")
    return df


def setOutputPath(debug):
    if debug:
        return "./miniTrainOutput.csv"
    return "./augmented_train.csv"


def saveLastReadIndexToDisk():
    with open("./lastIndexRead.txt", "w") as f:
        f.write(f"{last_index_read}")


def loadLastIndexSaved():
    global last_index_save
    try:
        with open("./lastIndexRead.txt", "r") as f:
            lis = f.readlines()[0]
            print(f"Last index saved: {lis}")
            last_index_save = int(lis)+1
    except FileNotFoundError as e:
        print("No saved index to load")
        last_index_save = 0


if __name__ == "__main__":
    loadLastIndexSaved()
    last_index_save += 1 # Começar a partir do proximo índice após o salvo!
    debug = False
    # debug = True
    outputPath = setOutputPath(debug)
    df = load_dataset(debug)
    truncateFile(outputPath)
    totalLength = df.shape[0]
    df.columns = ["phrase", "start", "end", "word", "tag"]
    list_of_phrases = []
    count = 0
    for index, row in df.iterrows():
        if index != last_index_save:
            continue
        last_index_save += 1
        last_index_read = index
        tag = row[4]
        if "resource" in tag.lower():
            tp = rowToTuple(row)
            list_of_phrases.append(tp)
            continue
        newRows = completeAug(row)
        list_of_phrases.extend(newRows)
        if len(list_of_phrases) >= 1000:
            augmented_df = pd.DataFrame(list_of_phrases)
            augmented_df.to_csv(outputPath, index=None, header=None, sep=";", mode="a+")
            count = count + len(list_of_phrases)
            list_of_phrases = []
            print(f"Stored {count/8} rows out of {totalLength}")
            saveLastReadIndexToDisk()

    # Flush list if there is anything left
    if len(list_of_phrases) != 0:
        augmented_df = pd.DataFrame(list_of_phrases)
        augmented_df.to_csv(outputPath, index=None, header=None, sep=";", mode="a+")
        count = count + len(list_of_phrases)
        list_of_phrases = []
        print(f"Stored {count/8} rows out of {totalLength}")
    print(f"Length of the original DataFrame: {df.shape[0]}")
    print(f"Length of the new DataFrame: {count}")
    with open('./FIM.txt', "a+") as f:
        f.write(f'Finished all the work!')
