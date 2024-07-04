#!/usr/bin/env python3
 
import http.server
import ssl
from pathlib import Path
import subprocess
import sys
import os

# Function to generate a self-signed certificate
def generate_certificate(domain):
    key_file = f"{domain}.key"
    cert_file = f"{domain}.crt"

    # Check if the certificate already exists
    if not Path(key_file).exists() or not Path(cert_file).exists():
        print(f"Generating self-signed certificate for {domain}...")
        subprocess.run([
            "openssl", "req", "-x509", "-newkey", "rsa:4096", "-sha256", "-days", "365",
            "-nodes", "-keyout", key_file, "-out", cert_file,
            "-subj", f"/CN={domain}"
        ])
    else:
        print(f"Using existing certificate for {domain}")

    return key_file, cert_file

# Function to clean up certificate files
def cleanup_files(files):
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except FileNotFoundError:
            pass

# Check for command-line arguments
if len(sys.argv) != 3:
    print("Usage: python3 script.py <domain> <port>")
    sys.exit(1)

# Get domain and port from command-line arguments
domain = sys.argv[1]
port = int(sys.argv[2])

# Generate certificate for the provided domain
key_file, cert_file = generate_certificate(domain)

# Set up the HTTP server
server_address = ('', port)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap the server with SSL
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=key_file, certfile=cert_file, server_side=True)

try:
    print(f"Serving on https://{domain}:{port}...")
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server...")
finally:
    # Clean up certificate files
    cleanup_files([key_file, cert_file])
    print("Server stopped.")
