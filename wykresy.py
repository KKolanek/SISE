import os
import re
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt


def stats(name, *strategy):
    folder_path = 'C:\\Users\\Krzys\\PycharmProjects\\SISE\\Stats'
    stats_dict = defaultdict(lambda: {'L': [], 'C': [], 'F': [], 'D': [], 'T': []})
    stan = '([a-z]{4})'
    if strategy:
        stan = strategy[0]

    lineregex = re.compile(r'4x4_(\d{2})_\d{5}_' + name + '_' + stan + '_stats.txt')
    for filename in os.listdir(folder_path):
        mat = lineregex.match(filename)
        if mat:
            size = mat.group(1)
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    x, y, z, k, m = f.readlines()
                    if x != -1:
                        stats_dict[size]['L'].append(int(x))
                        stats_dict[size]['C'].append(int(y))
                        stats_dict[size]['F'].append(int(z))
                        stats_dict[size]['D'].append(int(k))
                        stats_dict[size]['T'].append(float(m))

    avgL = [sum(stats_dict[size]['L']) / len(stats_dict[size]['L']) for size in stats_dict]
    avgClosed = [sum(stats_dict[size]['C']) / len(stats_dict[size]['C']) for size in stats_dict]
    avgFrontier = [sum(stats_dict[size]['F']) / len(stats_dict[size]['F']) for size in stats_dict]
    avgDepth = [sum(stats_dict[size]['D']) / len(stats_dict[size]['D']) for size in stats_dict]
    avgTime = [sum(stats_dict[size]['T']) / len(stats_dict[size]['T']) for size in stats_dict]

    return avgL, avgClosed, avgFrontier, avgDepth, avgTime


names = ['1', '2', '3', '4', '5', '6', '7']
plt.rcParams["figure.figsize"] = [9, 13]
fig, ax = plt.subplots(4, 2, tight_layout=True)
names_axis = np.arange(len(names))
ax[0, 0].bar(names_axis - 0.2, stats('bfs')[0], 0.2, color='blue')
ax[0, 0].bar(names_axis, stats('dfs')[0], 0.2, color='orange')
ax[0, 0].bar(names_axis + 0.2, stats('astr')[0], 0.2, color='green')
ax[0, 0].set_ylabel("Długość znalezionego rozwiązania")
ax[0, 0].set_xticks(names_axis, names)
ax[0, 0].set_yticks([0, 2, 4, 6, 8, 10, 12, 14])
ax[0, 0].set_title("Ogółem")
ax[0, 0].legend(['BFS', 'DFS', 'A*'])

ax[0, 1].bar(names_axis - 0.2, stats('astr', 'hamm')[0], 0.2, color='blue')
ax[0, 1].bar(names_axis, stats('astr', 'manh')[0], 0.2, color='orange')
ax[0, 1].set_title("A*")
ax[0, 1].set_xticks(names_axis, names)
ax[0, 1].set_yticks([0, 1, 2, 3, 4, 5, 6, 7])
ax[0, 1].legend(['Hamming', 'Manhattan'])


ax[1, 0].bar(names_axis - 0.4, stats('bfs', 'rdul')[0], 0.1, color='blue')
ax[1, 0].bar(names_axis - 0.3, stats('bfs', 'rdlu')[0], 0.1, color='orange')
ax[1, 0].bar(names_axis - 0.2, stats('bfs', 'drul')[0], 0.1, color='green')
ax[1, 0].bar(names_axis - 0.1, stats('bfs', 'drlu')[0], 0.1, color='red')
ax[1, 0].bar(names_axis, stats('bfs', 'ludr')[0], 0.1, color='purple')
ax[1, 0].bar(names_axis + 0.1, stats('bfs', 'lurd')[0], 0.1, color='brown')
ax[1, 0].bar(names_axis + 0.2, stats('bfs', 'uldr')[0], 0.1, color='pink')
ax[1, 0].bar(names_axis + 0.3, stats('bfs', 'ulrd')[0], 0.1, color='gray')
ax[1, 0].set_ylabel("Długość znalezionego rozwiązania")
ax[1, 0].set_xticks(names_axis, names)
ax[1, 0].set_yticks([1, 2, 3, 4, 5, 6, 7])
ax[1, 0].set_title("BFS")
ax[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], prop={'size': 8.5})
ax[1, 0].set_xlabel("Głębokość")

ax[1, 1].bar(names_axis - 0.4, stats('dfs', 'rdul')[0], 0.1, color='blue')
ax[1, 1].bar(names_axis - 0.3, stats('dfs', 'rdlu')[0], 0.1, color='orange')
ax[1, 1].bar(names_axis - 0.2, stats('dfs', 'drul')[0], 0.1, color='green')
ax[1, 1].bar(names_axis - 0.1, stats('dfs', 'drlu')[0], 0.1, color='red')
ax[1, 1].bar(names_axis, stats('dfs', 'ludr')[0], 0.1, color='purple')
ax[1, 1].bar(names_axis + 0.1, stats('dfs', 'lurd')[0], 0.1, color='brown')
ax[1, 1].bar(names_axis + 0.2, stats('dfs', 'uldr')[0], 0.1, color='pink')
ax[1, 1].bar(names_axis + 0.3, stats('dfs', 'ulrd')[0], 0.1, color='gray')
ax[1, 1].set_xticks(names_axis, names)
ax[1, 1].set_yticks([0, 2, 4, 6, 8, 10, 12, 14])
ax[1, 1].set_title("DFS")
ax[1, 1].set_xlabel("Głębokość")

ax[2, 0].bar(names_axis - 0.2, stats('bfs')[1], 0.2, color='blue', log=True)
ax[2, 0].bar(names_axis, stats('dfs')[1], 0.2, color='orange', log=True)
ax[2, 0].bar(names_axis + 0.2, stats('astr')[1], 0.2, color='green', log=True)
ax[2, 0].set_ylabel("Ilość odwiedzonych stanów")
ax[2, 0].set_xticks(names_axis, names)
ax[2, 0].set_title("Ogółem")
ax[2, 0].legend(['BFS', 'DFS', 'A*'])

ax[2, 1].bar(names_axis - 0.2, stats('astr', 'hamm')[1], 0.2, color='blue')
ax[2, 1].bar(names_axis, stats('astr', 'manh')[1], 0.2, color='orange')
ax[2, 1].set_title("A*")
ax[2, 1].set_xticks(names_axis, names)
ax[2, 1].legend(['Hamming', 'Manhattan'])

ax[3, 0].bar(names_axis - 0.4, stats('bfs', 'rdul')[1], 0.1, color='blue', log=True)
ax[3, 0].bar(names_axis - 0.3, stats('bfs', 'rdlu')[1], 0.1, color='orange', log=True)
ax[3, 0].bar(names_axis - 0.2, stats('bfs', 'drul')[1], 0.1, color='green', log=True)
ax[3, 0].bar(names_axis - 0.1, stats('bfs', 'drlu')[1], 0.1, color='red', log=True)
ax[3, 0].bar(names_axis, stats('bfs', 'ludr')[1], 0.1, color='purple', log=True)
ax[3, 0].bar(names_axis + 0.1, stats('bfs', 'lurd')[1], 0.1, color='brown', log=True)
ax[3, 0].bar(names_axis + 0.2, stats('bfs', 'uldr')[1], 0.1, color='pink', log=True)
ax[3, 0].bar(names_axis + 0.3, stats('bfs', 'ulrd')[1], 0.1, color='gray', log=True)
ax[3, 0].set_ylabel("Ilość odwiedzonych stanów")
ax[3, 0].set_xticks(names_axis, names)
ax[3, 0].set_yticks([1, 10, 100, 1000])
ax[3, 0].set_title("BFS")
ax[3, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], prop={'size': 8.5})
ax[3, 0].set_xlabel("Głębokość")

ax[3, 1].bar(names_axis - 0.4, stats('dfs', 'rdul')[1], 0.1, color='blue', log=True)
ax[3, 1].bar(names_axis - 0.3, stats('dfs', 'rdlu')[1], 0.1, color='orange', log=True)
ax[3, 1].bar(names_axis - 0.2, stats('dfs', 'drul')[1], 0.1, color='green', log=True)
ax[3, 1].bar(names_axis - 0.1, stats('dfs', 'drlu')[1], 0.1, color='red', log=True)
ax[3, 1].bar(names_axis, stats('dfs', 'ludr')[1], 0.1, color='purple', log=True)
ax[3, 1].bar(names_axis + 0.1, stats('dfs', 'lurd')[1], 0.1, color='brown', log=True)
ax[3, 1].bar(names_axis + 0.2, stats('dfs', 'uldr')[1], 0.1, color='pink', log=True)
ax[3, 1].bar(names_axis + 0.3, stats('dfs', 'ulrd')[1], 0.1, color='gray', log=True)
ax[3, 1].set_xticks(names_axis, names)
ax[3, 1].set_yticks([1, 10, 100, 1000, 10000, 100000])
ax[3, 1].set_title("DFS")
ax[3, 1].set_xlabel("Głębokość")

plt.savefig('wykresy.png')
plt.clf()
fig1, ax1 = plt.subplots(4, 2, tight_layout=True)

ax1[0, 0].bar(names_axis - 0.2, stats('bfs')[2], 0.2, color='blue', log=True)
ax1[0, 0].bar(names_axis, stats('dfs')[2], 0.2, color='orange', log=True)
ax1[0, 0].bar(names_axis + 0.2, stats('astr')[2], 0.2, color='green', log=True)
ax1[0, 0].set_ylabel("Ilość przetworzonych stanów")
ax1[0, 0].set_xticks(names_axis, names)
ax1[0, 0].set_title("Ogółem")
ax1[0, 0].legend(['BFS', 'DFS', 'A*'])

ax1[0, 1].bar(names_axis - 0.2, stats('astr', 'hamm')[2], 0.2, color='blue')
ax1[0, 1].bar(names_axis, stats('astr', 'manh')[2], 0.2, color='orange')
ax1[0, 1].set_title("A*")
ax1[0, 1].set_xticks(names_axis, names)
ax1[0, 1].legend(['Hamming', 'Manhattan'])
ax1[0, 1].set_yticks([0, 2, 4, 6, 8, 10])

ax1[1, 0].bar(names_axis - 0.4, stats('bfs', 'rdul')[2], 0.1, color='blue', log=True)
ax1[1, 0].bar(names_axis - 0.3, stats('bfs', 'rdlu')[2], 0.1, color='orange', log=True)
ax1[1, 0].bar(names_axis - 0.2, stats('bfs', 'drul')[2], 0.1, color='green', log=True)
ax1[1, 0].bar(names_axis - 0.1, stats('bfs', 'drlu')[2], 0.1, color='red', log=True)
ax1[1, 0].bar(names_axis, stats('bfs', 'ludr')[2], 0.1, color='purple', log=True)
ax1[1, 0].bar(names_axis + 0.1, stats('bfs', 'lurd')[2], 0.1, color='brown', log=True)
ax1[1, 0].bar(names_axis + 0.2, stats('bfs', 'uldr')[2], 0.1, color='pink', log=True)
ax1[1, 0].bar(names_axis + 0.3, stats('bfs', 'ulrd')[2], 0.1, color='gray', log=True)
ax1[1, 0].set_ylabel("Ilość przetworzonych stanów")
ax1[1, 0].set_xticks(names_axis, names)
ax1[1, 0].set_yticks([1, 10, 100, 1000])
ax1[1, 0].set_title("BFS")
ax1[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], prop={'size': 8.5})
ax1[1, 0].set_xlabel("Głębokość")

ax1[1, 1].bar(names_axis - 0.4, stats('dfs', 'rdul')[2], 0.1, color='blue', log=True)
ax1[1, 1].bar(names_axis - 0.3, stats('dfs', 'rdlu')[2], 0.1, color='orange', log=True)
ax1[1, 1].bar(names_axis - 0.2, stats('dfs', 'drul')[2], 0.1, color='green', log=True)
ax1[1, 1].bar(names_axis - 0.1, stats('dfs', 'drlu')[2], 0.1, color='red', log=True)
ax1[1, 1].bar(names_axis, stats('dfs', 'ludr')[2], 0.1, color='purple', log=True)
ax1[1, 1].bar(names_axis + 0.1, stats('dfs', 'lurd')[2], 0.1, color='brown', log=True)
ax1[1, 1].bar(names_axis + 0.2, stats('dfs', 'uldr')[2], 0.1, color='pink', log=True)
ax1[1, 1].bar(names_axis + 0.3, stats('dfs', 'ulrd')[2], 0.1, color='gray', log=True)
ax1[1, 1].set_xticks(names_axis, names)
ax1[1, 1].set_title("DFS")
ax1[1, 1].set_xlabel("Głębokość")

ax1[2, 0].bar(names_axis - 0.2, stats('bfs')[3], 0.2, color='blue')
ax1[2, 0].bar(names_axis, stats('dfs')[3], 0.2, color='orange')
ax1[2, 0].bar(names_axis + 0.2, stats('astr')[3], 0.2, color='green')
ax1[2, 0].set_ylabel("Maksymalna osiągnięta głębokość rekursji")
ax1[2, 0].set_xticks(names_axis, names)
ax1[2, 0].set_title("Ogółem")
ax1[2, 0].legend(['BFS', 'DFS', 'A*'])
ax1[2, 0].set_yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

ax1[2, 1].bar(names_axis - 0.2, stats('astr', 'hamm')[3], 0.2, color='blue')
ax1[2, 1].bar(names_axis, stats('astr', 'manh')[3], 0.2, color='orange')
ax1[2, 1].set_title("A*")
ax1[2, 1].set_xticks(names_axis, names)
ax1[2, 1].legend(['Hamming', 'Manhattan'])

ax1[3, 0].bar(names_axis - 0.4, stats('bfs', 'rdul')[3], 0.1, color='blue')
ax1[3, 0].bar(names_axis - 0.3, stats('bfs', 'rdlu')[3], 0.1, color='orange')
ax1[3, 0].bar(names_axis - 0.2, stats('bfs', 'drul')[3], 0.1, color='green')
ax1[3, 0].bar(names_axis - 0.1, stats('bfs', 'drlu')[3], 0.1, color='red')
ax1[3, 0].bar(names_axis, stats('bfs', 'ludr')[3], 0.1, color='purple')
ax1[3, 0].bar(names_axis + 0.1, stats('bfs', 'lurd')[3], 0.1, color='brown')
ax1[3, 0].bar(names_axis + 0.2, stats('bfs', 'uldr')[3], 0.1, color='pink')
ax1[3, 0].bar(names_axis + 0.3, stats('bfs', 'ulrd')[3], 0.1, color='gray')
ax1[3, 0].set_ylabel("Maksymalna osiągnięta głębokość rekursji")
ax1[3, 0].set_xticks(names_axis, names)
ax1[3, 0].set_title("BFS")
ax1[3, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], prop={'size': 8.5})
ax1[3, 0].set_xlabel("Głębokość")

ax1[3, 1].bar(names_axis - 0.4, stats('dfs', 'rdul')[3], 0.1, color='blue')
ax1[3, 1].bar(names_axis - 0.3, stats('dfs', 'rdlu')[3], 0.1, color='orange')
ax1[3, 1].bar(names_axis - 0.2, stats('dfs', 'drul')[3], 0.1, color='green')
ax1[3, 1].bar(names_axis - 0.1, stats('dfs', 'drlu')[3], 0.1, color='red')
ax1[3, 1].bar(names_axis, stats('dfs', 'ludr')[3], 0.1, color='purple')
ax1[3, 1].bar(names_axis + 0.1, stats('dfs', 'lurd')[3], 0.1, color='brown')
ax1[3, 1].bar(names_axis + 0.2, stats('dfs', 'uldr')[3], 0.1, color='pink')
ax1[3, 1].bar(names_axis + 0.3, stats('dfs', 'ulrd')[3], 0.1, color='gray')
ax1[3, 1].set_xticks(names_axis, names)
ax1[3, 1].set_title("DFS")
ax1[3, 1].set_xlabel("Głębokość")
plt.savefig('wykresy1.png')
plt.clf()

fig2, ax2 = plt.subplots(4, 2, tight_layout=True)
ax2[0, 0].bar(names_axis - 0.2, stats('bfs')[4], 0.2, color='blue', log=True)
ax2[0, 0].bar(names_axis, stats('dfs')[4], 0.2, color='orange', log=True)
ax2[0, 0].bar(names_axis + 0.2, stats('astr')[4], 0.2, color='green', log=True)
ax2[0, 0].set_ylabel("Czas trwania procesu obliczeniowego [s]")
ax2[0, 0].set_xticks(names_axis, names)
ax2[0, 0].set_yticks([0.01, 0.1, 1, 10, 100])
ax2[0, 0].set_title("Ogółem")
ax2[0, 0].legend(['BFS', 'DFS', 'A*'])

ax2[0, 1].bar(names_axis - 0.2, stats('astr', 'hamm')[4], 0.2, color='blue')
ax2[0, 1].bar(names_axis, stats('astr', 'manh')[4], 0.2, color='orange')
ax2[0, 1].set_title("A*")
ax2[0, 1].set_xticks(names_axis, names)
ax2[0, 1].set_yticks([0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14])
ax2[0, 1].legend(['Hamming', 'Manhattan'])

ax2[1, 0].bar(names_axis - 0.4, stats('bfs', 'rdul')[4], 0.1, color='blue')
ax2[1, 0].bar(names_axis - 0.3, stats('bfs', 'rdlu')[4], 0.1, color='orange')
ax2[1, 0].bar(names_axis - 0.2, stats('bfs', 'drul')[4], 0.1, color='green')
ax2[1, 0].bar(names_axis - 0.1, stats('bfs', 'drlu')[4], 0.1, color='red')
ax2[1, 0].bar(names_axis, stats('bfs', 'ludr')[4], 0.1, color='purple')
ax2[1, 0].bar(names_axis + 0.1, stats('bfs', 'lurd')[4], 0.1, color='brown')
ax2[1, 0].bar(names_axis + 0.2, stats('bfs', 'uldr')[4], 0.1, color='pink')
ax2[1, 0].bar(names_axis + 0.3, stats('bfs', 'ulrd')[4], 0.1, color='gray')
ax2[1, 0].set_ylabel("Czas trwania procesu obliczeniowego [s]")
ax2[1, 0].set_xticks(names_axis, names)
ax2[1, 0].set_title("BFS")
ax2[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], prop={'size': 8.5})
ax2[1, 0].set_xlabel("Głębokość")

ax2[1, 1].bar(names_axis - 0.4, stats('dfs', 'rdul')[4], 0.1, color='blue', log=True)
ax2[1, 1].bar(names_axis - 0.3, stats('dfs', 'rdlu')[4], 0.1, color='orange', log=True)
ax2[1, 1].bar(names_axis - 0.2, stats('dfs', 'drul')[4], 0.1, color='green', log=True)
ax2[1, 1].bar(names_axis - 0.1, stats('dfs', 'drlu')[4], 0.1, color='red', log=True)
ax2[1, 1].bar(names_axis, stats('dfs', 'ludr')[4], 0.1, color='purple', log=True)
ax2[1, 1].bar(names_axis + 0.1, stats('dfs', 'lurd')[4], 0.1, color='brown', log=True)
ax2[1, 1].bar(names_axis + 0.2, stats('dfs', 'uldr')[4], 0.1, color='pink', log=True)
ax2[1, 1].bar(names_axis + 0.3, stats('dfs', 'ulrd')[4], 0.1, color='gray', log=True)
ax2[1, 1].set_xticks(names_axis, names)
ax2[1, 1].set_title("DFS")
ax2[1, 1].set_xlabel("Głębokość")

plt.savefig('wykresy2.png')
plt.clf()