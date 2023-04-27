# README


There are various scripts and outputs in this directory. They are named according to the tasks in planning.txt:



1) Cache size and latency:

Take 1 trace and - 
	1. Vary cache ratio(associativity) keeping size constant - only for llc and l2c(only one at a time). Plot miss rate? miss latency? IPC?
	2. Vary cache size and associativity keeping number of sets constant.
	3. Vary cache size keeping associativity constant. 
		a) vary all 3 caches independently within their ranges of comfort - keep latencies constant, we just want to see trends. Likely that llc size will cause more differences than others. Plot corresponding miss 
		rate and ipc.
		b) Alter llc cache size(keeping associativity constant) and llc latency according to A. logarithmic B. linear. In linear make multiple plots for different slopes and show optimal slope value where
		 negligible change wrt size.

2) Block size:
	1. Keep ratio constant, vary block size with sets and ways. Total memory is constant
	2. Keep sets constant, vary block size with ways. Total memory is constant
	3. Keep ways constant, vary block size with sets. Total memory constant
	4. Vary block and size both while keeping set,way constant

3) Inclusion Exclusion:
	1. Show for n traces, m cache sizes each that inclusion exclusion doesn't help
	

4) Replacement Policies:
	1. Show variation between LFU, LRU, DRRIP for any n traces, const cache size or try multiple cache sizes.



For example, the output generator for cache and latency 3a is Ashwin_Testing3a..... and so on. 


The plotters for the same are available, use the names to understand what they are plotting. The structure of the output data and the data points to be plotted often varied hence we had to copy paste numeric values into the plotters. Some plotters that start with 'plot' instead fo 'plotter' plot multiple parameters on one curve. plot_func plots the latency variation with cache size functions.

Some of the result data is also provided in the files. The data is of the form:

f'{llc\_set}, {llc\_way}, {l2c\_set}, {l2c\_way}, {l1d\_set}, {l1d\_way}, {ipc\_val},\n {llc\_miss\_freq}, {llc\_latency}, {l2c\_miss\_freq}, {l2c\_latency}, {l1d\_miss\_freq}, {l1d\_latency}\n\n















