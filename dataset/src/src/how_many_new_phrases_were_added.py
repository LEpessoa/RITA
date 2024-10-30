import pandas as pd
import numpy as np
col_names = ['phrase','start','end','ico','tag']
df_original = pd.read_csv('./original_list.csv',sep=';',names=col_names,header=None)
df_new = pd.read_csv('./complete_dataset_with_subtypes_COMPLETE.csv',sep=';', header=None, names=col_names)

unique_icos_original = df_original['ico'].unique().tolist()
unique_icos_new_df = df_new['ico'].unique().tolist()
original_set = set(unique_icos_original)
new_set = set(unique_icos_new_df)
new_icos_set = new_set - original_set
print(f'New icos: {len(new_icos_set)}')

# Filter phrases with ICOs present in new_icos_set
phrases_with_new_icos = df_new[df_new['ico'].isin(new_icos_set)]



# Write filtered phrases to CSV
# phrases_with_new_icos.to_csv('phrases_with_new_icos.csv', index=False)