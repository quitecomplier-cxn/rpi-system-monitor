from system_info import get_system_info

def main():
    info = get_system_info()
    print("\n DzifCha Systems Raspberry Pi System Monitor")
    print("-" * 30)
    print(f"CPU Usage: {info['cpu']}%")
    print(f"Memory Usage: {info['memory']}%")
    print(f"Disk Usage: {info['disk']}%")
    print(f"Temperature: {info['temperature']}")
    print(f"Uptime: {info['uptime']} seconds\n")

if __name__ == "__main__":
    main()
