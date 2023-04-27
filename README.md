# CS230 Project - Cache Hierarchy Optimisations for SAT Solver
### Members: Aditya Nemiwal(210050004), Ashwin Goyal(210050024), Divyansh Singhal(210050045)
On all the traces provided, the following various parameters(or policies) were altered and the resulting changes were observed like IPC or miss rates:
- Cache Inclusion Policies: Inclusive, Exclusive, and NINE(Non Inclusive Non Exclusive)
- Cache Replacement Policies like LRU, DRRIP, SRRIP
- The size of a single cache block while keeping memory constant
- Size of L1, L2, L3 Caches
- Associativity of Caches
- Function of access latency as the size of cache

The detailed results obtained are reported in the following presentation link: https://docs.google.com/presentation/d/1N8Zs5aVaZxt0kvnf_Ilo4hQ3ojCOf8v4WMMcJ9L6qaI/edit?usp=sharing.

Link to Youtube Presentation: [Presentation](https://youtu.be/vA2bejdUDPA)

To collect and visualise the above required data, python scripts were used which are present in the directory **[Scripts](https://github.com/Divyansh5647/ChampSim232/tree/main/Scripts)**.
