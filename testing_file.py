import os


# os.system("")


path = ""


# run build then run



os.system("./build_champsim.sh bimodal no no no no lru 1")
os.system("./run_champsim.sh bimodal-no-no-no-no-lru-1core 2 3 cadical-high-60K-113B.champsimtrace.xz")

with open("results_3M/cadical-high-60K-113B.champsimtrace.xz-bimodal-no-no-no-no-lru-1core.txt") as f:
    s = f.read()
    ipc_start = s.index('CPU 0 cumulative IPC: ')
    ipc_end = s.index(' instructions:', ipc_start)
    ipc_val = float(s[ipc_start+21:ipc_end].strip()) 
    total_start = s.index('LLC TOTAL     ACCESS:')
    total_end = s.index('HIT:', total_start)
    total = int(s[total_start+21:total_end].strip())
    misses_start = s.index('MISS: ', total_end)
    missed_end = s.index('LLC LOAD      ACCESS:', misses_start)
    misses = int(s[misses_start+5:missed_end].strip())
    latency_start = s.index('LLC AVERAGE MISS LATENCY:')
    latency_end = s.index("cycles\nMajor fault")
    latency = float(s[latency_start+25:latency_end].strip())
#LLC AVERAGE MISS LATENCY: 219.825 cycles

    print(ipc_val, misses, total, misses/total, latency)












