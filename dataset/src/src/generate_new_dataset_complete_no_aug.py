import pandas as pd

original_df = pd.read_csv('../original.csv',sep=';')
augmented_df = pd.read_csv('../new.csv',sep=';')

columns = ['phrase','start','end','target','label']
original_df.columns = columns
augmented_df.columns = columns

unique_original_icos = original_df['target'].unique()
unique_augmented_icos = augmented_df['target'].unique()
unique_new_icos = [cat for cat in unique_augmented_icos if cat not in unique_original_icos]
print(unique_new_icos) 
print(len(unique_new_icos)) # 1357

df_only_new_phrases = augmented_df[augmented_df['target'].isin(unique_new_icos)]
print(df_only_new_phrases.shape) # (56966, 5)
# Given 56966 / 8 = 7120.75 lets remove 6 phrases to

# get 5 phrases per 

print("")
print(len(unique_augmented_icos))



