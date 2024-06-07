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
    pd.read_table(state_list[i],encoding="utf_8")