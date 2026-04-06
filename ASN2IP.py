"""ASN to IP conversion script.

This utility reads a list of Autonomous System Numbers (ASNs) from the
``only number.txt`` file (one ASN per line), queries the public API at
``https://asn.ipinfo.app`` for the list of CIDR blocks associated with each
ASN, and writes a consolidated, deduplicated list of CIDR blocks to
``blocklist.netset``. The script prints progress information to the console
and, at the end, reports the total number of unique CIDR entries collected.

**Usage**::

    python ASN2IP.py

The script expects the following files to be present in the working
directory:

* ``only number.txt`` – a plain‑text file containing ASNs, one per line.
* ``blocklist.netset`` – the output file that will be created/overwritten.

**Requirements**

* Python 3.6+.
* The :pypi:`requests` library (install with ``pip install requests``).
* An active Internet connection to reach the ``asn.ipinfo.app`` API.

The script is intended for security‑related workflows such as generating
firewall blocklists, so ensure the input list of ASNs is trusted before
running the script.
"""

import requests

cidr_set = set()

with open('only number.txt') as f:
    asns = [line.strip() for line in f if line.strip()]

for asn in asns:
    print(f"Collecting IPs from {asn}")
    try:
        response = requests.get(
            f"https://asn.ipinfo.app/api/text/list/AS{asn}", 
            timeout=30
        )
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
