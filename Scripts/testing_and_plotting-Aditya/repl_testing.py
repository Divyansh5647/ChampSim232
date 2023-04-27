## This file is to test different replacement policies and inclusion policies
import os


# os.system("")


path = ""


# run build then run



# tracename="cadical-high-60K-134B.champsimtrace.xz"
# tracename="cadical-high-60K-113B.champsimtrace.xz"
# tracename = "kissat-inc-high-30K-1802B.champsimtrace.xz"
# repl = "drrip"
size1 = 30
size2 = 30
llc_set = 2048
llc_way = 16
l2c_set = 1024
l2c_way = 8
l1d_set = 64
l1d_way = 12

for tracename in ["kissat-inc-high-30K-1802B.champsimtrace.xz",  "cadical-high-60K-134B.champsimtrace.xz" , "cadical-high-60K-1227B.champsimtrace.xz"]:
    for repl in ["lru", "drrip", "srrip", "ship", "rnd", "mru"]:
        for incl in ["incl","excl","NINE"]:

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
            with open("src/cache.cc", 'r') as f:
                data = f.read()
            with open("src/cache.cc", 'w') as f:
                incl_start = data.index('#define IS_INC')
                incl_end = data.index('\n', incl_start)
                data4 = f'{data[:incl_start]}#define IS_INC 0{data[incl_end:]}'
                
                incl_start = data4.index('#define IS_NINE')
                incl_end = data4.index('\n', incl_start)
                data4 = f'{data4[:incl_start]}#define IS_NINE 0{data4[incl_end:]}'
                
                incl_start = data4.index('#define IS_EXC')
                incl_end = data4.index('\n', incl_start)
                data4 = f'{data4[:incl_start]}#define IS_EXC 0{data4[incl_end:]}'

                if(incl=="incl"):
                    incl_start = data4.index('#define IS_INC')
                    incl_end = data4.index('\n', incl_start)
                    data5 = f'{data4[:incl_start]}#define IS_INC 1{data4[incl_end:]}'
                elif(incl=="excl"):
                    incl_start = data4.index('#define IS_EXC')
                    incl_end = data4.index('\n', incl_start)
                    data5 = f'{data4[:incl_start]}#define IS_EXC 1{data4[incl_end:]}'
                elif(incl=="NINE"):
                    incl_start = data4.index('#define IS_NINE')
                    incl_end = data4.index('\n', incl_start)
                    data5 = f'{data4[:incl_start]}#define IS_NINE 1{data4[incl_end:]}'

                f.write(data5)

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
            with open(f"output_incl-excl_repl_{tracename}_{size1}_{size2}.txt", 'a') as f:
                f.write(f'{incl} {repl}\n{llc_set}, {llc_way}, {l2c_set}, {l2c_way}, {l1d_set}, {l1d_way}, {ipc_val},\n {llc_miss_freq}, {llc_latency}, {l2c_miss_freq}, {l2c_latency}, {l1d_miss_freq}, {l1d_latency}\n\n')





