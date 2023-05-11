import os
# if not os.path.exists("data"):
#     os.mkdir("data")
# for i in range(1,11):
#     # os.mkdir(f"data/day{i}")
#     os.rename(f'data/day{i}',f'data/tut{i}')
# os.mkdir('data')
folders=os.listdir('data')
for i in folders:
    print(i)
    print(os.listdir(f'data/{i}'))
# print(os.getcwd)
# os.chdir("/python_with_harry")
# print(os.getcwd)