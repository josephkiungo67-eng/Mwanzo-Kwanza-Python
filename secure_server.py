import http.server
import socketserver
import os

PORT = 8000
# Lazimisha server kusoma mafaili ya folda hili tu tulilopo (Current Directory)
ALLOWED_DIR = os.getcwd()

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Mbinu ya kiusalama: Sanitize path ili kuzuia mashambulizi ya '../../'
        normalized_path = super().translate_path(path)
        # Kama mtumiaji anajaribu kutoka nje ya folda lililoruhusiwa, mzuie
        if not normalized_path.startswith(ALLOWED_DIR):
            return "/dev/null" # Inarudisha ukurasa tupu au kosa
        return normalized_path

print(f"[+] Secure Web Server inawaka kwenye Port {PORT}...")
try:
    with socketserver.TCPServer(("", PORT), SecureHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n[-] Secure Web Server imezimwa.")
