import pathlib
import csv
import pandas as pd
input_dir = 'history/states'
# 保存するファルダ
output_dir = './'

# フォルダ内に保存されているファイル一覧
state_list = list(pathlib.Path(input_dir).glob('**/*.txt'))

# print(state_list)
for i in range (len(state_list)):

    with open(state_list[i],"r",encoding="utf-8") as f:
        df = pd.Series(f.readlines())
        print(df)
        df.drop(df[df.str.contains('owner')].index,inplace=True)
        df.drop(df[df.str.contains('add_core_of')].index,inplace=True)
        lines = df.to_list()

    with open(state_list[i],"w",encoding="utf-8") as f:
        
        f.write("")
        for j in range(len(lines)):
            f.write(str(lines[j]))
