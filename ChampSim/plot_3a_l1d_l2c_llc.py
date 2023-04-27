import matplotlib.pyplot as plt
import numpy as np

path = f'Q2_res/'
num_ways = [1,4,16,32]
names = ['400.perlbench-41B', '403.gcc-16B', '436.cactusADM-1804B', '482.sphinx3-1100B']
replacements = ['lfu', 'fifo', 'rnd']
arr = np.array([1,2,3,4])
width = 0.2
# for name in names:
#     ## filename format = <name>.champsimtrace.xz-bimodal-no-no-no-no-<replacement>-1core.txt
#     arr_ipc = np.zeros((4,3))
#     arr_miss_rate = np.zeros((4,3))
#     for num_way in range(len(num_ways)):
#         for replacement in range(len(replacements)):
#             file_path = path+f'{num_ways[num_way]}/results_30M/{name}.champsimtrace.xz-bimodal-no-no-no-no-{replacements[replacement]}-1core.txt'
#             f = open(file_path, 'r')
#             s = f.read()
#             ipc_start = s.index('CPU 0 cumulative IPC: ')
#             ipc_end = s.index(' instructions:', ipc_start)
#             ipc_val = float(s[ipc_start+21:ipc_end].strip())
#             total_start = s.index('LLC TOTAL     ACCESS:')
#             total_end = s.index('HIT:', total_start)
#             total = int(s[total_start+21:total_end].strip())
#             misses_start = s.index('MISS: ', total_end)
#             missed_end = s.index('LLC LOAD      ACCESS:', misses_start)
#             misses = int(s[misses_start+5:missed_end].strip())
#             # print(ipc_val, misses/total)
#             arr_ipc[num_way, replacement] = ipc_val
#             arr_miss_rate[num_way, replacement] = misses/total
#             f.close()

# name = "cadical-high-60K-134B.champsimtrace.xz"

for_legend = ["l1d","l2c","llc"]

name = "kissat-inc-high-30K-1802B.champsimtrace.xz"
arr_ipc_1 = [0.312383,0.312407,0.312414]
arr_ipc_2 = [0.312344,0.312407,0.31251]
arr_ipc_3 = [0.307637,0.312407,0.320768]


x_axis_vals = [1,2,3]
x_axis_labels_1 = ['(64,12)','(128,12)','(256,12)']
x_axis_labels_2 = ['(1024,8)','(2048,8)','(4096,8)']
x_axis_labels_3 = ['(2048,16)','(4096,16)','(8192,16)']



plt.title(f'IPC:{name}')
my_min = np.min(arr_ipc_1+arr_ipc_2+arr_ipc_3)
my_max = np.max(arr_ipc_1+arr_ipc_2+arr_ipc_3)
diff = my_max-my_min
plt.plot(x_axis_vals,arr_ipc_1)
plt.plot(x_axis_vals,arr_ipc_2)
plt.plot(x_axis_vals,arr_ipc_3)

plt.legend(for_legend)
# plt.yscale('log')
# plt.xticks([])
# plt.bar(arr-0.2, arr_ipc[:,0], width)
# plt.bar(arr, arr_ipc[:,1], width)
# plt.bar(arr+0.2, arr_ipc[:,2], width)
# plt.xticks(x_axis_vals,x_axis_labels)
for i in range(len(x_axis_vals)):
    plt.annotate(f"{x_axis_labels_1[i]}", (x_axis_vals[i], arr_ipc_1[i]))
    plt.annotate(f"{x_axis_labels_2[i]}", (x_axis_vals[i], arr_ipc_2[i]))
    plt.annotate(f"{x_axis_labels_3[i]}", (x_axis_vals[i], arr_ipc_3[i]))

plt.xlabel('Num Ways')
plt.ylabel('IPC')
# plt.legend(replacements)
plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.savefig(f'plots/IPC{name}.png', dpi = 'figure', format = None)
plt.show()

# plt.title(f'Miss Rates:{name}')
# my_min = np.min(arr_miss_rate_1+arr_miss_rate_2)
# my_max = np.max(arr_miss_rate_1+arr_miss_rate_2)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_miss_rate_1)
# plt.plot(x_axis_vals,arr_miss_rate_2)
# plt.legend(for_legend)
# # plt.xscale('log')
# # plt.bar(arr-0.2, arr_miss_rate[:,0], width)
# # plt.bar(arr, arr_miss_rate[:,1], width)
# # plt.bar(arr+0.2, arr_miss_rate[:,2], width)
# # plt.xticks(x_axis_vals,x_axis_labels)
# for i in range(len(x_axis_vals)):
#     plt.annotate(f"{x_axis_labels_1[i]}", (x_axis_vals[i], arr_miss_rate_1[i]))
#     plt.annotate(f"{x_axis_labels_2[i]}", (x_axis_vals[i], arr_miss_rate_2[i]))

# plt.xlabel('Num Ways')
# plt.ylabel('Miss rates')
# # plt.legend(replacements)
# plt.ylim(max(0,my_min-diff), min(1,my_max+diff))
# # plt.savefig(f'plots/Miss Rates{name}.png', dpi = 'figure', format = None)
# plt.show()
