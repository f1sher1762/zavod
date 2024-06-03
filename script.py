import subprocess
import os
import re

def ping_ip(ip):
    subprocess.run(['ping', '-n', '1', '-w', '100', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_arp_table():
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    return result.stdout

def parse_arp_table(arp_output):
    mac_pattern = re.compile(r'((?:[0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2})')
    return mac_pattern.findall(arp_output)

def read_known_macs(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return set(file.read().splitlines())
    return set()

def write_macs(file_path, macs):
    with open(file_path, 'w') as file:
        for mac in macs:
            file.write(f"{mac}\n")

def main():
    old_macs_file = 'known_macs.txt'
    new_macs_file = 'new_macs.txt'
    start_ip = 100
    end_ip = 110
    base_ip = '192.168.0.'

    for i in range(start_ip, end_ip + 1):
        ip = f"{base_ip}{i}"
        ping_ip(ip)

    arp_output = get_arp_table()
    current_macs = set(parse_arp_table(arp_output))

    known_macs = read_known_macs(old_macs_file)

    new_macs = current_macs - known_macs

    if new_macs:
        print("Новые MAC-адреса найдены:")
        for mac in new_macs:
            print(mac)
        write_macs(new_macs_file, new_macs)

    # Записываем текущие MAC-адреса в known_macs.txt для следующего запуска
    write_macs(old_macs_file, current_macs)

    input("Для продолжения нажмите любую клавишу . . .")

if __name__ == "__main__":
    main()
