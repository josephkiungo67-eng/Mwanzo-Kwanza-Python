import socket

target = input("Weka IP Address au Tovuti (mfano: 127.0.0.1): ")
port_to_check = int(input("Weka namba ya port unayotaka kuichunguza (mfano: 6100): "))

print(f"\n[-] Inachunguza Port {port_to_check} kwenye target: {target}...")
print("-" * 50)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)  # Sekunde 3 ili kupa huduma muda wa kujibu
    
    # Jaribu kuunganisha
    s.connect((target, port_to_check))
    
    # Tuma ombi fupi la salamu (HTTP Request au Empty String) ili kuamsha majibu
    s.sendall(b"Hello\r\n\r\n")
    
    # Pokea bytes 1024 za kwanza za majibu kutoka kwenye port
    banner = s.recv(1024)
    
    print(f"[+] Port {port_to_check} ipo WAZI!")
    # decode('utf-8', errors='ignore') inabadilisha data kuwa maandishi ya kawaida
    print(f"[+] Huduma inayokimbia (Banner):\n{banner.decode('utf-8', errors='ignore').strip()}")

except socket.timeout:
    print(f"[!] Port {port_to_check} ipo wazi lakini haijatuma majibu yoyote (Timeout).")
except Exception as e:
    print(f"[x] Imeshindwa kuunganisha: {e}")
finally:
    s.close()

print("-" * 50)

