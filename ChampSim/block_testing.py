import os
import math
path = ""

'''
cache.h : 

// L1 INSTRUCTION CACHE
#define L1I_SET 64
#define L1I_WAY 8
#define L1I_LATENCY 4

// L1 DATA CACHE
#define L1D_SET 64
#define L1D_WAY 12
#define L1D_LATENCY 5 

// L2 CACHE
#define L2C_SET 1024
#define L2C_WAY 8
#define L2C_LATENCY 10  // 4/5 (L1I or L1D) + 10 = 14/15 cycles

// LAST LEVEL CACHE
#define LLC_SET NUM_CPUS*2048
#define LLC_WAY 16
#define LLC_LATENCY 20 
'''

blocks_m = [1,2,4,8,16]   # m is the multiplying factor for change in block size
# blocksize *= m^2
# set and way /= m

repl = "lru"
size1 = 30
size2 = 30

# tracename="cadical-high-60K-113B.champsimtrace.xz"
# tracename="cadical-high-60K-134B.champsimtrace.xz"
tracename="cadical-high-60K-1227B.champsimtrace.xz"
# tracename = "kissat-inc-high-30K-1802B.champsimtrace.xz"
llc_set = 2048*2
llc_way = 16*2*2
l2c_set = 1024*2
l2c_way = 8*2*2
l1d_set = 64*2
l1d_way = 12*2*2

# CASE - 1 TESTING B.S = c, W = c
# CASE - 2 TESTING B.W = c, S = c
# CASE - 3 TESTING S = c, W = c
for case in [1,3]:
    if case==1:
        for m in blocks_m:
            with open("inc/cache.h", 'r') as f:
                data = f.read()
            with open("inc/cache.h", 'w') as f:
                llc_start = data.index('#define LLC_SET NUM_CPUS*')
                llc_end = data.index('#define LLC_RQ_SIZE NUM_CPUS*L2C_MSHR_SIZE', llc_start)
                data2 = f'{data[:llc_start]}#define LLC_SET NUM_CPUS*{llc_set//m}\n#define LLC_WAY {llc_way//2}\n{data[llc_end:]}'

                l2c_start = data2.index('#define L2C_SET')
                l2c_end = data2.index('#define L2C_RQ_SIZE', l2c_start)
                data3 = f'{data2[:l2c_start]}#define L2C_SET {l2c_set//m}\n#define L2C_WAY {l2c_way//2}\n{data2[l2c_end:]}'

                l1d_start = data3.index('#define L1D_SET')
                l1d_end = data3.index('#define L1D_RQ_SIZE', l1d_start)
                data4 = f'{data3[:l1d_start]}#define L1D_SET {l1d_set//m}\n#define L1D_WAY {l1d_way//2}\n{data3[l1d_end:]}'
                f.write(data4)

            with open("inc/champsim.h", 'r') as f:
                data = f.read()
            with open("inc/champsim.h", 'w') as f:
                cache_start = data.index('#define BLOCK_SIZE')
                cache_end = data.index('#define MAX_READ_PER_CYCLE', cache_start)
                data2 = f'{data[:cache_start]}#define BLOCK_SIZE {32*m}\n#define LOG2_BLOCK_SIZE {5+int(math.log2(m))}\n{data[cache_end:]}'
                f.write(data2)

            os.system(f"./build_champsim.sh bimodal no no no no {repl} 1 2> log.txt")
            os.system(f"./run_champsim.sh bimodal-no-no-no-no-{repl}-1core {size1} {size2} {tracename}")

            with open(f"results_{size2}M/{tracename}-bimodal-no-no-no-no-{repl}-1core.txt") as f:
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
            with open(f"output_setblockvar_{tracename}_{repl}_{size1}_{size2}.txt", 'a') as f:
                f.write(f'BLOCK SIZE : {32*m}\n{llc_set//m}, {llc_way//2}, {l2c_set//m}, {l2c_way//2}, {l1d_set//m}, {l1d_way//2}, {ipc_val},\n {llc_miss_freq}, {llc_latency}, {l2c_miss_freq}, {l2c_latency}, {l1d_miss_freq}, {l1d_latency}\n\n')

    elif case == 2:
        for m in blocks_m:
            with open("inc/cache.h", 'r') as f:
                data = f.read()
            with open("inc/cache.h", 'w') as f:
                llc_start = data.index('#define LLC_SET NUM_CPUS*')
                llc_end = data.index('#define LLC_RQ_SIZE NUM_CPUS*L2C_MSHR_SIZE', llc_start)
                data2 = f'{data[:llc_start]}#define LLC_SET NUM_CPUS*{llc_set//2}\n#define LLC_WAY {llc_way//m}\n{data[llc_end:]}'

                l2c_start = data2.index('#define L2C_SET')
                l2c_end = data2.index('#define L2C_RQ_SIZE', l2c_start)
                data3 = f'{data2[:l2c_start]}#define L2C_SET {l2c_set//2}\n#define L2C_WAY {l2c_way//m}\n{data2[l2c_end:]}'

                l1d_start = data3.index('#define L1D_SET')
                l1d_end = data3.index('#define L1D_RQ_SIZE', l1d_start)
                data4 = f'{data3[:l1d_start]}#define L1D_SET {l1d_set//2}\n#define L1D_WAY {l1d_way//m}\n{data3[l1d_end:]}'
                f.write(data4)

            with open("inc/champsim.h", 'r') as f:
                data = f.read()
            with open("inc/champsim.h", 'w') as f:
                cache_start = data.index('#define BLOCK_SIZE')
                cache_end = data.index('#define MAX_READ_PER_CYCLE', cache_start)
                data2 = f'{data[:cache_start]}#define BLOCK_SIZE {32*m}\n#define LOG2_BLOCK_SIZE {5+int(math.log2(m))}\n{data[cache_end:]}'
                f.write(data2)

            os.system(f"./build_champsim.sh bimodal no no no no {repl} 1 2> log.txt")
            os.system(f"./run_champsim.sh bimodal-no-no-no-no-{repl}-1core {size1} {size2} {tracename}")

            with open(f"results_{size2}M/{tracename}-bimodal-no-no-no-no-{repl}-1core.txt") as f:
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
            with open(f"output_wayblockvar_{tracename}_{repl}_{size1}_{size2}.txt", 'a') as f:
                f.write(f'BLOCK SIZE : {32*m}\n{llc_set//2}, {llc_way//m}, {l2c_set//2}, {l2c_way//m}, {l1d_set//2}, {l1d_way//m}, {ipc_val},\n {llc_miss_freq}, {llc_latency}, {l2c_miss_freq}, {l2c_latency}, {l1d_miss_freq}, {l1d_latency}\n\n')

    elif case ==3:
        for m in blocks_m:
            with open("inc/cache.h", 'r') as f:
                data = f.read()
            with open("inc/cache.h", 'w') as f:
                llc_start = data.index('#define LLC_SET NUM_CPUS*')
                llc_end = data.index('#define LLC_RQ_SIZE NUM_CPUS*L2C_MSHR_SIZE', llc_start)
                data2 = f'{data[:llc_start]}#define LLC_SET NUM_CPUS*{llc_set//2}\n#define LLC_WAY {llc_way//2}\n{data[llc_end:]}'

                l2c_start = data2.index('#define L2C_SET')
                l2c_end = data2.index('#define L2C_RQ_SIZE', l2c_start)
                data3 = f'{data2[:l2c_start]}#define L2C_SET {l2c_set//2}\n#define L2C_WAY {l2c_way//2}\n{data2[l2c_end:]}'

                l1d_start = data3.index('#define L1D_SET')
                l1d_end = data3.index('#define L1D_RQ_SIZE', l1d_start)
                data4 = f'{data3[:l1d_start]}#define L1D_SET {l1d_set//2}\n#define L1D_WAY {l1d_way//2}\n{data3[l1d_end:]}'
                f.write(data4)

            with open("inc/champsim.h", 'r') as f:
                data = f.read()
            with open("inc/champsim.h", 'w') as f:
                cache_start = data.index('#define BLOCK_SIZE')
                cache_end = data.index('#define MAX_READ_PER_CYCLE', cache_start)
                data2 = f'{data[:cache_start]}#define BLOCK_SIZE {32*m}\n#define LOG2_BLOCK_SIZE {5+int(math.log2(m))}\n{data[cache_end:]}'
                f.write(data2)

            os.system(f"./build_champsim.sh bimodal no no no no {repl} 1 2> log.txt")
            os.system(f"./run_champsim.sh bimodal-no-no-no-no-{repl}-1core {size1} {size2} {tracename}")

            with open(f"results_{size2}M/{tracename}-bimodal-no-no-no-no-{repl}-1core.txt") as f:
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
            with open(f"output_sizeblockvar_{tracename}_{repl}_{size1}_{size2}.txt", 'a') as f:
                f.write(f'BLOCK SIZE : {32*m}\n{llc_set//2}, {llc_way//2}, {l2c_set//2}, {l2c_way//2}, {l1d_set//2}, {l1d_way//2}, {ipc_val},\n {llc_miss_freq}, {llc_latency}, {l2c_miss_freq}, {l2c_latency}, {l1d_miss_freq}, {l1d_latency}\n\n')

    else :
        pass
