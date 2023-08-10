# bad-asn-list
An open source list of ASNs known to belong to cloud, managed hosting, and colo facilities.

## Adding ASN to list

You are free to add suspicious ASNs providing Hosting / VPN services.

To add ASN to the list,

- Add suspicious ASN to any line of `bad-asn-list.csv`

- Install Node.js, run `node ./index.js` to sort and update both `bad-asn-list.csv` and `bad-asn-list.json`

- After sorting it, feel free to submit the PR!

Also, rasing issues for adding bad ASN is also allowed, please describe why ASN should be listed, the ASN number, and the Entity information.

## The Problem

This list came after spending far too long searching for a good way to keep automated bots, spammers, and scammers off the social network I created, Nearby. I found that after we hit a certain size (around 500K monthly active users), the flood of these bad actors became entirely unmanagable. I tried countless detection methods, but most of them resulted in too many missed and/or false positives. 

I tried offloading the account creation process to depend on the user having a Facebook profile, thinking that would solve the problem. It didn't help at all. Next I tried Google sign-in, but it also was entirely ineffective. I eventually tried to outsource the problem to a company called MaxMind. Their API actually worked very well, but it was prohibitively expensive for our purposes. 

## The Solution

I continued to deepen my understanding of the bad traffic and I eventually realized that almost all the bad traffic was coming from hosting/colo facilities and cloud service providers. Even traffic coming from VPNs was originating from a hosting facility where the VPN provider was located. I built a list of ASNs which belong to known hosting/colo/cloud providers. Whenever a new account was being created, I looked-up the ASN that owns the IP address. I then checked if that ASN was included in the list I had created and if so, prevented the account from being created.

You might think that this would block a lot of good traffic, but from all of my tests, that doesn't appear to be the case at all. Furthermore, the problem was about 90% solved.  Almost all the bad traffic vanished.

I've been testing out this solution for a few months now and it's been going amazingly well. I know that I am not the only person who has faced this problem, so I decided to open-source my list. Feel free to submit pull requests if you have any updates to the list you'd like to share.

## Implementation

1. Load this list into a database or in-memory.
2. When a request comes in, determine the ASN for the request's ip address. There are a number of ways to do this. For example, MaxMind offers a free database that maps IP address to ASN: http://dev.maxmind.com/geoip/geoip2/geolite2/
3. Check if the IP address' ASN is included in the list from step 1.  If so, block the request, increase fraud score, etc.

Hopefully this will help save someone from wasting as many hours I have trying to solve this problem!

Brian Hamachek (brian@brianhama.com)
