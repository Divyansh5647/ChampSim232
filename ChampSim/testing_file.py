import os


# os.system("")


path = ""


# run build then run

'''
#define LLC_SET NUM_CPUS*1024
#define LLC_WAY 16
cryptominisat-high-30K-2423B.champsimtrace.xz-bimodal-no-no-no-no-lru-1core.txt
'''

tracename="cadical-high-60K-113B.champsimtrace.xz"

# tracename = "kissat-inc-high-30K-1802B.champsimtrace.xz"
# tracename = "cryptominisat-high-30K-2423B.champsimtrace.xz"
repl = "drrip"

for llc_set in [4096]:
    for llc_way in [256]:
        for l2c_set in [2048]:
            for l2c_way in [256]:
                for l1d_set in [64]:
                    for l1d_way in [8]:

                        with open("inc/cache.h", 'r') as f:
                            data = f.read()
                        with open("inc/cache.h", 'w') as f:
                            llc_start = data.index('#define LLC_SET NUM_CPUS*')
                            llc_end = data.index('#define LLC_RQ_SIZE NUM_CPUS*L2C_MSHR_SIZE', llc_start)
                            data2 = f'{data[:llc_start]}#define LLC_SET NUM_CPUS*{llc_set}\n#define LLC_WAY {llc_way}\n{data[llc_end:]}'

                            l2c_start = data2.index('#define L2C_SET')
                            l2c_end = data2.index('#define L2C_RQ_SIZE', l2c_start)
                            data3 = f'{data2[:l2c_start]}#define L2C_SET {l2c_set}\n#define L2C_WAY {l2c_way}\n{data2[l2c_end:]}'

                            l1d_start = data3.index('#define L1D_SET')
                            l1d_end = data3.index('#define L1D_RQ_SIZE', l1d_start)
                            data4 = f'{data3[:l1d_start]}#define L1D_SET {l1d_set}\n#define L1D_WAY {l1d_way}\n{data3[l1d_end:]}'
                            f.write(data4)
                        
                            # ipc_val = float(s[ipc_start+21:ipc_end].strip())
                            

                        os.system(f"./build_champsim.sh bimodal no no no no {repl} 1 2> log.txt")
                        os.system(f"./run_champsim.sh bimodal-no-no-no-no-{repl}-1core 2 3 {tracename}")

                        with open(f"results_3M/{tracename}-bimodal-no-no-no-no-{repl}-1core.txt") as f:
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
                            latency_end = s.index("cycles\nMajor fault", latency_start)
                            latency = float(s[latency_start+25:latency_end].strip())
                        #LLC AVERAGE MISS LATENCY: 219.825 cycles
                            llc_latency, llc_miss_freq = latency, misses/total


                            total_start = s.index('L2C TOTAL     ACCESS:')
                            total_end = s.index('HIT:', total_start)
                            total = int(s[total_start+21:total_end].strip())
                            misses_start = s.index('MISS: ', total_end)
                            missed_end = s.index('L2C LOAD      ACCESS:', misses_start)
                            misses = int(s[misses_start+5:missed_end].strip())
                            latency_start = s.index('L2C AVERAGE MISS LATENCY:')
                            latency_end = s.index("cycles\nLLC TOTAL     ACCESS:", latency_start)
                            latency = float(s[latency_start+25:latency_end].strip())
                            l2c_latency, l2c_miss_freq = latency, misses/total


                            total_start = s.index('L1D TOTAL     ACCESS:')
                            total_end = s.index('HIT:', total_start)
                            total = int(s[total_start+21:total_end].strip())
                            misses_start = s.index('MISS: ', total_end)
                            missed_end = s.index('L1D LOAD      ACCESS:', misses_start)
                            misses = int(s[misses_start+5:missed_end].strip())
                            latency_start = s.index('L1D AVERAGE MISS LATENCY:')
                            latency_end = s.index("cycles\nL1I TOTAL     ACCESS", latency_start)
                            latency = float(s[latency_start+25:latency_end].strip())
                            l1d_latency, l1d_miss_freq = latency, misses/total



                            # print(ipc_val, misses, total, misses/total, latency)
                        with open(f"output_complete_{tracename}_{repl}.txt", 'a') as f:
                            f.write(f'{llc_set}, {llc_way}, {l2c_set}, {l2c_way}, {l1d_set}, {l1d_way}, {ipc_val},\n {llc_miss_freq}, {llc_latency}, {l2c_miss_freq}, {l2c_latency}, {l1d_miss_freq}, {l1d_latency}\n\n')












