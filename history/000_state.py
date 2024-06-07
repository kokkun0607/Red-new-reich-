import pathlib

input_dir = 'history/states'
# 保存するファルダ
output_dir = './'

# フォルダ内に保存されているファイル一覧
state_list = list(pathlib.Path(input_dir).glob('**/*.txt'))

# print(state_list)
for i in range (len(state_list)):
    with open (state_list[i],"w") as f:
        f.write("\n")
    print(state_list[i])