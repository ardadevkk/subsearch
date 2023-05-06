import requests
import sys

if len(sys.argv) != 2:
    print(f"Kullanım: python {sys.argv[0]} <domain>")
    sys.exit(1)

domain = sys.argv[1]

try:
    print('Scanned Al Subdomains Wait please...')
    response = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
    subdomains = set()
    for certificate in response.json():
        subdomains.add(certificate["name_value"])
    for subdomain in sorted(subdomains):
        print(subdomain)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    sys.exit(1)
