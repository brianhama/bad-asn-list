import requests

cidr_set = set()

with open('only number.txt') as f:
    asns = [line.strip() for line in f if line.strip()]

for asn in asns:
    print(f"Collecting IPs from {asn}")
    try:
        response = requests.get(f"https://asn.ipinfo.app/api/text/list/AS{asn}")
        response.raise_for_status()
        cidrs = response.text.strip().splitlines()
        for cidr in cidrs:
            cidr_set.add(cidr.strip())
    except Exception as e:
        print(f"Failed with {asn}: {e}")

with open("blocklist.netset", "w") as f:
    for cidr in sorted(cidr_set):
        f.write(cidr + "\n")

print(f"\nTotal CIDR: {len(cidr_set)}")
