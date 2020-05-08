# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state'] = df['state'].apply(lambda x:x.lower())
df['total'] = df['Jan']+df['Feb']+df['Mar']
sum_row = [df['Jan'].sum(), df['Feb'].sum(), df['Mar'].sum(), df['total'].sum()]
df_final = df.append(pd.DataFrame(data=sum_row, index=['Jan', 'Feb', 'Mar', 'total']).T, verify_integrity=False, ignore_index=True, sort=False)

# Code ends here


# --------------
import requests

# Code starts here


# Code starts here
url = r"https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1.columns = df1.iloc[11]
df1 = df1.iloc[12:]
df1['United States of America'] = df1['United States of America'].apply(lambda x:x.replace(" ",""))



# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
#df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
#df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = pd.Series(df1['US'].values, index=df1['United States of America']).to_dict()
if 'abbr' not in df_final.columns:
    df_final.insert(6,"abbr",None)
df_final['abbr'] = df_final['state'].apply(lambda x:mapping.get(x, None))



# Code ends here


# --------------
# Code stars here
df_final.loc[df_final['state']=='mississipi','abbr'] = 'MS'
df_final.loc[df_final['state']=='tenessee','abbr'] = 'TN'
# Code ends here


# Code ends here


# --------------
# Code starts here
df_sub = df_final.groupby('abbr')[[ 'Jan', 'Feb', 'Mar', 'total']].sum()
formatted_df = df_sub.applymap(lambda x:"$"+str(x))



# Code ends here


# --------------
# Code starts here
sum_row = pd.DataFrame(df_final[['Jan', 'Feb', 'Mar', 'total']].sum(),index=['Jan', 'Feb', 'Mar', 'total'])
df_sub_sum = sum_row.T
df_sub_sum = df_sub_sum.applymap(lambda x:"$"+str(x))
final_table = formatted_df.append(df_sub_sum)
print(final_table)
final_table.rename(index={0:'Total'}, inplace=True)


# Code ends here


# --------------
# Code starts here

df_sub['total'].plot(kind='pie')
# Code ends here


