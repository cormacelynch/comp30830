#Script to find and printout system information

import socket
import os
import platform
import psutil

machine_name = socket.gethostname()
os_name = platform.system()
os_version = platform.version()
num_cpus = os.cpu_count()
memory = round(psutil.virtual_memory()[0]/(1024*1024*1024),2)
ip_address = socket.gethostbyname(machine_name)

print("Name of machine: ", machine_name)
print("Operating system name: ", os_name) 
print("Operating system version: ", os_version) 
print("Number of CPU's: ", num_cpus)
print("Amount of memory: ",memory,"GB")
print("IP address of machine: " , ip_address)

#Script to measure the strength of the CPU

import timeit
import math
import itertools

def bench_pidigits(ndigits=1000,loops=100):
    
    def calc_ndigits(n):
        def gen_x():
            return map(lambda k: (k,4*k+2,0,2*k+1),itertools.count(1))
        
        def compose(a,b):
            aq, ar, as_, at = a
            bq, br, bs, bt = b
            return (aq * bq,
                    aq * br + ar * bt,
                    as_ * bq + at * bs,
                    as_ * br + at * bt)
        
        def extract(z, j):
            q, r, s, t = z
            return (q*j + r) // (s*j + t)
        
        def pi_digits():
            z = (1,0,0,1)
            x = gen_x()
            while 1:
                y = extract(z, 3)
                while y != extract(z, 4):
                    z = compose(z, next(x))
                    y = extract(z,3)
                z = compose((10,-10*y,0,1), z)
                yield y
                
        return list(itertools.islice(pi_digits(),n))
    
    for _ in range(loops):
        calc_ndigits(ndigits)
    return

if __name__ == '__main__':
    t_default = 6.388216104
    start_time = timeit.default_timer()
    bench_pidigits(ndigits=1000,loops=100)
    elapsed_time = timeit.default_timer() - start_time
    print("Relative Elapsed: ", round(elapsed_time/t_default,2))