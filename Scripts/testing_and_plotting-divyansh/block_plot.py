import matplotlib.pyplot as plt
import numpy as np

num_blocks = [32,64,128,256,512]

for_legend = ["original num_ways", "twice the original num_ways"]

# name = "Number of ways, cache size = constant\nkissat-inc-high-30K-1802B.champsimtrace.xz"
# arr_ipc_1 = [0.292542, 0.307061, 0.316259, 0.319704, 0.316691]
# arr_ipc_2 = [0.296222, 0.31192, 0.322131, 0.327148, 0.326885]

# x_axis_vals = [1,2,3,4,5]

# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1+arr_ipc_2)
# my_max = np.max(arr_ipc_1+arr_ipc_2)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")
# plt.plot(x_axis_vals,arr_ipc_2, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)
# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()





# for_legend = ["original num_ways", "twice the original num_ways"]

# name = "Number of ways, cache size = constant\ncadical-high-60K-134B.champsimtrace.xz"
# arr_ipc_1 = [0.159511, 0.166361, 0.172719, 0.172569, 0.16093]
# arr_ipc_2 = [0.160416, 0.167166, 0.173782, 0.174018, 0.16387]

# x_axis_vals = [1,2,3,4,5]

# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1+arr_ipc_2)
# my_max = np.max(arr_ipc_1+arr_ipc_2)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")
# plt.plot(x_axis_vals,arr_ipc_2, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()


# for_legend = ["original num_ways", "twice the original num_ways"]

# name = "Number of ways, cache size = constant\ncadical-high-60K-1227B.champsimtrace.xz"
# arr_ipc_1 = [0.144645, 0.155806, 0.170528, 0.176373, 0.162735]
# arr_ipc_2 = [0.146284, 0.157284, 0.172613, 0.17954, 0.169801]

# x_axis_vals = [1,2,3,4,5]

# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1+arr_ipc_2)
# my_max = np.max(arr_ipc_1+arr_ipc_2)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")
# plt.plot(x_axis_vals,arr_ipc_2, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()



# for_legend = ["original num_sets"]

# name = "Number of sets, cache size = constant\ncadical-high-60K-134B.champsimtrace.xz"
# arr_ipc_1 = [0.159514, 0.166361, 0.172699, 0.172477, 0.160753]

# x_axis_vals = [1,2,3,4,5]

# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1)
# my_max = np.max(arr_ipc_1)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()



# for_legend = ["original num_sets"]

# name = "Number of sets, cache size = constant\nkissat-inc-high-30K-1802B.champsimtrace.xz"
# arr_ipc_1 = [0.292548, 0.307061, 0.316239, 0.319547, 0.315132]

# x_axis_vals = [1,2,3,4,5]

# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1)
# my_max = np.max(arr_ipc_1)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()


# for_legend = ["original num_sets"]

# name = "Number of sets, cache size = constant\ncadical-high-60K-1227B.champsimtrace.xz"
# arr_ipc_1 = [0.144607, 0.155806, 0.170469, 0.176178, 0.164273]

# x_axis_vals = [1,2,3,4,5]

# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1)
# my_max = np.max(arr_ipc_1)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()


# for_legend = ["original num_ways", "twice the original num_ways"]

# name = "Number of ways, sets = constant, Variable Cache Size\nkissat-inc-high-30K-1802B.champsimtrace.xz"
# arr_ipc_1 = [0.2905, 0.307061, 0.322082, 0.340323, 0.371676]
# arr_ipc_2 = [0.292548, 0.31192, 0.332831, 0.361991, 0.416521]

# x_axis_vals = [1,2,3,4,5]


# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1+arr_ipc_2)
# my_max = np.max(arr_ipc_1+arr_ipc_2)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")
# plt.plot(x_axis_vals,arr_ipc_2, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()




# for_legend = ["original num_ways", "twice the original num_ways"]

# name = "Number of ways, sets = constant, Variable Cache Size\ncadical-high-60K-134B.champsimtrace.xz"
# arr_ipc_1 = [0.159066, 0.166361, 0.173761, 0.175938, 0.172501]
# arr_ipc_2 = [0.159514, 0.167166, 0.174948, 0.177705, 0.175576]

# x_axis_vals = [1,2,3,4,5]


# plt.title(f'{name}')
# my_min = np.min(arr_ipc_1+arr_ipc_2)
# my_max = np.max(arr_ipc_1+arr_ipc_2)
# diff = my_max-my_min
# plt.plot(x_axis_vals,arr_ipc_1, "-o")
# plt.plot(x_axis_vals,arr_ipc_2, "-o")

# plt.legend(for_legend)
# plt.xticks(x_axis_vals,num_blocks)

# plt.xlabel('Num Blocks')
# plt.ylabel('IPC')
# plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
# plt.show()

for_legend = ["original num_ways", "twice the original num_ways"]

name = "Number of ways, sets = constant, Variable Cache Size\ncadical-high-60K-1227B.champsimtrace.xz"
arr_ipc_1 = [0.143944, 0.155806, 0.172575, 0.183821, 0.187683]
arr_ipc_2 = [0.144607, 0.157284, 0.175901, 0.189414, 0.197212]

x_axis_vals = [1,2,3,4,5]


plt.title(f'{name}')
my_min = np.min(arr_ipc_1+arr_ipc_2)
my_max = np.max(arr_ipc_1+arr_ipc_2)
diff = my_max-my_min
plt.plot(x_axis_vals,arr_ipc_1, "-o")
plt.plot(x_axis_vals,arr_ipc_2, "-o")

plt.legend(for_legend)
plt.xticks(x_axis_vals,num_blocks)

plt.xlabel('Num Blocks')
plt.ylabel('IPC')
plt.ylim(max(0,my_min-diff/10), my_max+diff/10)
plt.show()