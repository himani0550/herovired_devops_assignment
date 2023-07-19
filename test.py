import psutil
PID = 80
p   = psutil.Process(PID)
tot_load_from_process = p.cpu_percent()/psutil.cpu_count()
print(tot_load_from_process)
print(psutil.cpu_pecent())
if __name__ == '__main__':
    PID = 80  
    