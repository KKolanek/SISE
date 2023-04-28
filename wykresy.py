import os

folder_path = 'C:\\Users\\Krzys\\PycharmProjects\\SISE\\Stats'
avgLen = 0
avgDepth = 0
size = 0

for filename in os.listdir(folder_path):
    if 'dfs' in filename:
        size += 1
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    if line[0] != '-1\n':
                        avgLen += int(line[0])
                    avgDepth += int(line[1].strip())
print(avgLen/size)
print(avgDepth/size)
