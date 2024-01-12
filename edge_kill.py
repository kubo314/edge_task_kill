import subprocess
from time import sleep

while True:
    proc = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        task_info = line.decode("shift-jis").split()
        if "msedge.exe" in task_info:
            pid = int(task_info[1])
            subprocess.Popen(["taskkill", "/F", "/PID", str(pid)], creationflags=subprocess.CREATE_NO_WINDOW)
    
    sleep(1)