import psutil
import time
import subprocess

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return int(uptime_seconds)

def get_temperature():
    try:
        temp = subprocess.check_output(
            ["vcgencmd", "measure_temp"]
        ).decode()
        return temp.replace("temp=", "")
    except Exception:
        return "N/A"

def get_system_info():
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "uptime": get_uptime(),
        "temperature": get_temperature()
    }

