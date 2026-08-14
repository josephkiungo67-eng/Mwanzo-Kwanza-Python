import http.server
import socketserver

# 1. Weka namba ya port ambapo tovuti yako itapatikana
PORT = 8000

# 2. Amuru Python kutumia mfumo wa kawaida wa kuhudumia kurasa za wavuti
Handler = http.server.SimpleHTTPRequestHandler

print(f"[+] Web Server inawaka...")
print(f"[+] Fungua Browser yako kisha nenda: http://127.0.0.1:{PORT}")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        # Hapa tunaiambia server iendelee kukimbia bila kuzima
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n[-] Web Server imezimwa.")
