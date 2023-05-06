import requests
import sys
import os

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <domain>")
    sys.exit(1)

domain = sys.argv[1]
output_dir = "output"
output_file = os.path.join(output_dir, f"{domain}.txt")

try:
    print('Scanned Al Subdomains Wait please...')
    response = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
    subdomains = set()
    for certificate in response.json():
        subdomains.add(certificate["name_value"])
    for subdomain in sorted(subdomains):
        print(subdomain)
    with open(output_file, "w") as f:
        for subdomain in sorted(subdomains):
            f.write(subdomain + "\n")
except requests.exceptions.RequestException as e:
    print(f"Hata: {e}")
    sys.exit(1)
