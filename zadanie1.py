import psutil

print("USER PID COMMAND")

for proc in psutil.process_iter(['username', 'pid', 'name']):
    try:
        user = proc.info['username']
        pid = proc.info['pid']
        command = proc.info['name']
        
        if user is None:
            user = "unknown"
            
        print(f"{user} {pid} {command}")
        
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue
    
    