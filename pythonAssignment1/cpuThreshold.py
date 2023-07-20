import psutil
import time

def monitor_cpu_usage(threshold):
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU usage: {cpu_usage}%")

            if cpu_usage > threshold:
                print("**Alert**: CPU usage has been exceeded more than threshold value")
                
                

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        time.sleep(5)  

if __name__ == '__main__':
    threshold = 80  
    monitor_cpu_usage(threshold)