# The purpose of this script:
# The purpose of this script is to select 100 phrases from the test dataset
# These phrases will be the base to create FunctionalRequirements example phrases and userStories example phrases

# How is the selection going to occur?
# We are going to equally divide 100 by the number of labels, in this case we have 7 (smart_camera, on_device_resource, network_resource, actuator, tag, service, sensor), and from these labels we are going to get the number of phrases needed, making a point to select phrases with different words (Adafruit 1234, BeagleBone, Raspberry Pi, etc).

# Load complete dataset
import pandas as pd

df_complete = pd.read_csv("./test.csv", sep=";")
columns = ["phrase", "start", "end", "word", "label"]
df_complete.columns = columns
num_labels = 7
phrases_to_get = 100
phrases_per_label = int(phrases_to_get / num_labels)  # 14

list_of_labels = df_complete["label"].unique()

chosen_phrases = []

for label in list_of_labels:
    print(f'Getting phrases for label "{label}"')
    filt = df_complete["label"] == label
    df_current_label = df_complete.loc[filt]
    list_of_words_on_this_label = df_current_label["word"].unique()
    count = 0
    for word in list_of_words_on_this_label:
        filt_word = df_current_label["word"] == word
        df_current_word = df_current_label.loc[filt_word]
        row = df_current_word.iloc[0]
        chosen_phrases.append(row)
        count += 1
        if count == phrases_per_label:
            count = 0
            break

df_chosen_phrases = pd.DataFrame(chosen_phrases, columns=columns)
df_chosen_phrases["phrase_kind"] = "Storyline"
df_chosen_phrases = df_chosen_phrases.loc[
    :,
    ["phrase_kind", "label", "phrase", "word"],
]
print(df_chosen_phrases.head())

print("Saving chosen phrases to disk")
df_chosen_phrases.to_csv("./chosen_phrases.csv", sep=";", header=None, index=None)
print(f"Final dataframe shape: {df_chosen_phrases.shape}")
